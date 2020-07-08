# -*- coding: utf-8 -*-
"""
    @file: f4_string_fully_arranged.py
    @date: 2020-07-08 11:24 AM

    @answer: https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/solution/mian-shi-ti-38-zi-fu-chuan-de-pai-lie-hui-su-fa-by/
"""

from typing import List


# abcd -> ab

def permutation(s: str) -> List[str]:
    c, res = list(s), []

    def dfs(x):
        if x == len(c) - 1:
            res.append(''.join(c))  # 添加排列方案
            return
        # dic = set()
        for i in range(x, len(c)):
            # if c[i] in dic: continue  # 重复，因此剪枝
            # dic.add(c[i])
            c[i], c[x] = c[x], c[i]  # 交换，将 c[i] 固定在第 x 位
            dfs(x + 1)  # 开启固定第 x + 1 位字符
            c[i], c[x] = c[x], c[i]  # 恢复交换

    dfs(0)
    return res


if __name__ == '__main__':
    r = permutation("abcde")
    print(r)

    # ['abcde', 'abced',
    #  'abdce', 'abdec', 'abedc', 'abecd', 'acbde', 'acbed', 'acdbe', 'acdeb', 'acedb', 'acebd', 'adcbe', 'adceb', 'adbce', 'adbec', 'adebc', 'adecb', 'aecdb', 'aecbd', 'aedcb', 'aedbc', 'aebdc', 'aebcd', 'bacde', 'baced', 'badce', 'badec', 'baedc', 'baecd', 'bcade', 'bcaed', 'bcdae', 'bcdea', 'bceda', 'bcead', 'bdcae', 'bdcea', 'bdace', 'bdaec', 'bdeac', 'bdeca', 'becda', 'becad', 'bedca', 'bedac', 'beadc', 'beacd', 'cbade', 'cbaed', 'cbdae', 'cbdea', 'cbeda', 'cbead', 'cabde', 'cabed', 'cadbe', 'cadeb', 'caedb', 'caebd', 'cdabe', 'cdaeb', 'cdbae', 'cdbea', 'cdeba', 'cdeab', 'ceadb', 'ceabd', 'cedab', 'cedba', 'cebda', 'cebad', 'dbcae', 'dbcea', 'dbace', 'dbaec', 'dbeac', 'dbeca', 'dcbae', 'dcbea', 'dcabe', 'dcaeb', 'dceab', 'dceba', 'dacbe', 'daceb', 'dabce', 'dabec', 'daebc', 'daecb', 'decab', 'decba', 'deacb', 'deabc', 'debac', 'debca', 'ebcda', 'ebcad', 'ebdca', 'ebdac', 'ebadc', 'ebacd', 'ecbda', 'ecbad', 'ecdba', 'ecdab', 'ecadb', 'ecabd', 'edcba', 'edcab', 'edbca', 'edbac', 'edabc', 'edacb', 'eacdb', 'eacbd', 'eadcb', 'eadbc', 'eabdc', 'eabcd']
