#!/usr/bin/env python3

import hashlib
import itertools

required_start = "000000"
salt = 'yzbqklnj'.encode('utf-8')

for i in itertools.count(1):
    tohash = salt + i.to_bytes((i.bit_length() + 7) // 8, 'big')
    m = hashlib.md5(tohash)
    hash = m.hexdigest()

    if hash[0:6] == required_start:
        print(i, hash)
        break