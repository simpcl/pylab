
import os
import struct
import config

class tsm_file_info:
    def __init__(self, f, fsize):
        self.f_ = f
        self.fsize_ = fsize
        self.magic_ = ''
        self.version = 0
        self.data_pos_ = 0
        self.index_pos_ = 0

    def parse(self):
        self.magic_ = self.f_.read(config.MAGIC_SIZE)
        version = self.f_.read(1)
        self.version_ = ord(version)


    def __repr__(self):
        pass


file_stat = os.stat('./000000002-000000002.tsm')
file_size = file_stat.st_size
print('file size:', file_size)

f = open('./000000002-000000002.tsm', 'rb')
magic = f.read(4)
print("magic:", magic)

s = f.read(1)
version = ord(s) #struct.unpack('c', s)
print('version:', version)

f.seek(file_size-8)
s = f.read(8)
(index_offset,) = struct.unpack('!Q', s)
print('index offset:', index_offset)

f.seek(index_offset)
s = f.read(2)
(key_len,) = struct.unpack('!H', s)
print('key len:', key_len)

key = f.read(key_len)
print('key:', key)

s = f.read(1)
block_type = ord(s)
print('block type:', block_type)

key_count = f.read(2)
(key_count,) = struct.unpack('!H', key_count)
print('key count:', key_count)

s = f.read(16)
(min_time, max_time) = struct.unpack('!QQ', s)
#min_time = f.read(8)
#max_time = f.read(8)
print('min time:', min_time)
print('max time:', max_time)

s = f.read(8)
(block_offset,) = struct.unpack('!Q', s)
print('block offset:', block_offset)

s = f.read(4)
(block_size,) = struct.unpack('!L', s)
print('block size:', block_size)

f.close()
