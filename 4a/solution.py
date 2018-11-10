#!/usr/bin/env python3

import hashlib
import itertools

for i in itertools.count(1):
    tohash = 'yzbqklnj' + str(i)
    m = hashlib.md5(tohash.encode('utf-8'))
    hash = m.hexdigest()

    if hash[0:5] == "00000":
        print(i, hash)
        break