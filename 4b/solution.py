#!/usr/bin/env python3

import hashlib
import itertools

required_start = "0" * 6

salt = 'yzbqklnj'.encode('utf-8')

for i in itertools.count(1):
    tohash = salt + str(i).encode('utf-8')

    m = hashlib.md5(tohash)
    hash = m.hexdigest()

    if hash[0:6] == required_start:
        print(i, hash)
        break
