#ifndef _FSNAME_H_
#define _FSNAME_H_

#include <stdint.h>
#include <stdlib.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_FSNAME_BIN_LENGTH 18
#define MAX_FSNAME_STR_LENGTH 24

#pragma pack(2)
typedef struct _filebits_t {
    uint16_t salt_a;
    uint32_t app_id;
    uint16_t salt_b;
    uint64_t file_id;
    uint16_t salt_c;
} filebits_t;
#pragma pack()

const char* encode_fsname(uint32_t appid, uint64_t fid);
int decode_fsname(const char* fsname, size_t fsname_len, filebits_t* ptr);

#ifdef __cplusplus
}
#endif

#endif // _FSNAME_H_
