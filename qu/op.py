# -*- coding: utf-8 -*-
"""
    @file: op.py
    @date: 2020-10-12 11:57 AM
"""

op = ['*', '//', '+', '-', '']


res = set()

for t in range(1000, 9999+1):
    n = str(t)

    if n[1] == '0' or n[2] == '0' or n[3] == '0':
        continue

    # 351
    for i in op:
        for j in op:
            for k in op:
                if i == '' and j == '' and k == '':
                    continue

                val = n[0] + i + n[1] + j + n[2] + k + n[3]

                # 351 == 153
                if str(eval(val)) == n[::-1]:
                    print(val)

