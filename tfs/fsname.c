
#include <arpa/inet.h>
#include <string.h>
#include <time.h>

#include "fsname.h"

static const char* KEY_MASK = "CloudStorage";
static const int32_t KEY_MASK_LEN = 12;
static const char enc_table[] = "0JoU8EaN3xf19hIS2d.6pZRFBYurMDGw7K5m4CyXsbQjg_vTOAkcHVtzqWilnLPe";
static const char dec_table[] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,18,0,0,11,16,8,36,34,19,32,4,12,0,0,0,0,0,0,0,49,24,37,29,5,23,30,52,14,1,33,61,28,7,48,62,42,22,15,47,3,53,57,39,25,21,0,0,0,0,45,0,6,41,51,17,63,10,44,13,58,43,50,59,35,60,2,20,56,27,40,54,26,46,31,9,38,55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};

static uint64_t htonll(uint64_t n)
{
    uint32_t low, high;
    uint64_t result = 0;

    low = (uint32_t) (n & 0xffffffff);
    high = (uint32_t) ((n >> 32) & 0xffffffff);

    low = htonl(low);
    high = htonl(high);

    result = low;
    result = result << 32 | high;

    return result;
}

static uint64_t ntohll(uint64_t n)
{
    uint32_t low, high;
    uint64_t result = 0;

    low = (uint32_t) (n & 0xffffffff);
    high = (uint32_t) ((n >> 32) & 0xffffffff);

    low = ntohl(low);
    high = ntohl(high);

    result = low;
    result = result << 32 | high;

    return result;
}

static int xor_mask(const char* source, const int32_t len, char* target)
{
    int32_t i;
    for (i = 0; i < len; i++) {
        target[i] = source[i] ^ KEY_MASK[i % KEY_MASK_LEN];
    }
    return 0;
}

static int encode(const char *input, char *output)
{
    if (!input || !output) {
        return -1;
    }

    char buffer[MAX_FSNAME_BIN_LENGTH];
    xor_mask(input, MAX_FSNAME_BIN_LENGTH, buffer);

    int32_t i = 0;
    int32_t k = 0;
    uint32_t value = 0;
    for (i = 0; i < MAX_FSNAME_BIN_LENGTH; i += 3) {
        value = ((buffer[i] << 16) & 0xff0000) + ((buffer[i + 1] << 8) & 0xff00) + (buffer[i + 2] & 0xff);
        output[k++] = enc_table[value >> 18];
        output[k++] = enc_table[(value >> 12) & 0x3f];
        output[k++] = enc_table[(value >> 6) & 0x3f];
        output[k++] = enc_table[value & 0x3f];
    }
    return 0;
}

static int decode(const char *input, char *output)
{
    if (!input || !output) {
        return -1;
    }

    int32_t i = 0;
    int32_t k = 0;
    uint32_t value = 0;
    char buffer[MAX_FSNAME_BIN_LENGTH];
    for (i = 0; i < MAX_FSNAME_STR_LENGTH; i += 4) {
        value = (dec_table[input[i] & 0xff] << 18) + (dec_table[input[i + 1] & 0xff] << 12) +
          (dec_table[input[i + 2] & 0xff] << 6) + dec_table[input[i + 3] & 0xff];
        buffer[k++] = (char) ((value >> 16) & 0xff);
        buffer[k++] = (char) ((value >> 8) & 0xff);
        buffer[k++] = (char) (value & 0xff);
    }
    xor_mask(buffer, MAX_FSNAME_BIN_LENGTH, output);
    return 0;
}

const char* encode_fsname(uint32_t appid, uint64_t fid)
{
    static char output[MAX_FSNAME_STR_LENGTH + 1];
    filebits_t filebits;
    uint32_t rn;

    memset((void *) &filebits, 0, sizeof(filebits_t));
    filebits.app_id = htonl(appid);
    filebits.file_id = htonll(fid);

    srand( (unsigned int)time(0) );
    rn = (uint32_t) rand();
    filebits.salt_a = (uint16_t) (rn & 0xffff);
    filebits.salt_b = (uint16_t) ((rn >> 8) & 0xffff);
    filebits.salt_c = (uint16_t) ((rn >> 16) & 0xffff);

    memset((void *) output, 0, MAX_FSNAME_STR_LENGTH + 1);
    int ret = encode((const char *) &filebits, output);
    if (ret < 0) {
        return NULL;
    }
    return output;
}

int decode_fsname(const char* fsname, size_t fsname_len, filebits_t* ptr)
{
    int ret;

    if (!fsname || !ptr) {
        return -1;
    }
    if (fsname_len != MAX_FSNAME_STR_LENGTH) {
        return -1;
    }

    memset((void *) ptr, 0, sizeof(filebits_t));
    ret = decode(fsname, (char *) ptr);
    if (ret < 0) {
        return ret;
    }

    ptr->app_id = ntohl(ptr->app_id);
    ptr->file_id = ntohll(ptr->file_id);

    return 0;
}
