import base64
import heapq
import time
from bisect import bisect_left, bisect_right
from collections import deque, defaultdict
from functools import cache
from math import inf
from typing import List, Counter

import numpy as np
from networkx.utils.misc import pairwise
from sympy import primefactors
from UnionF import UnionFind
import math
from heapq import heappush, heappop,heapify
import chardet
from math import comb

MOD=10**9+7
MX = 10**5+1
lpf = [0] * MX
for i in range(2, MX):
    if lpf[i] == 0:
        for j in range(i, MX, i):
            if lpf[j] == 0:
                lpf[j] = i

def prime_factorization(x):
    res = []
    while x > 1:
        p = lpf[x]
        e = 1
        x //= p
        while x % p == 0:
            e += 1
            x //= p
        res.append((p, e))
    return res



class SegmentTree:
    def __init__(self, arr, default=0):
        if isinstance(arr, int):
            arr = [default] * arr
        n = len(arr)
        self._n = n
        self._tree = [0] * (2 << (n - 1).bit_length())
        self._build(arr, 1, 0, n - 1)


    def _merge_val(self, a: int, b: int) -> int:
        return max(a, b)


    def _maintain(self, node: int) -> None:
        self._tree[node] = self._merge_val(self._tree[node * 2], self._tree[node * 2 + 1])


    def _build(self, a: List[int], node: int, l: int, r: int) -> None:
        if l == r:  # 叶子
            self._tree[node] = a[l]
            return
        m = (l + r) // 2
        self._build(a, node * 2, l, m)
        self._build(a, node * 2 + 1, m + 1, r)
        self._maintain(node)

    def _update(self, node: int, l: int, r: int, i: int, val: int) -> None:
        if l == r:
            self._tree[node] = self._merge_val(self._tree[node], val)
            return
        m = (l + r) // 2
        if i <= m:
            self._update(node * 2, l, m, i, val)
        else:
            self._update(node * 2 + 1, m + 1, r, i, val)
        self._maintain(node)

    def _query(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        if ql <= l and r <= qr:
            return self._tree[node]
        m = (l + r) // 2
        if qr <= m:
            return self._query(node * 2, l, m, ql, qr)
        if ql > m:
            return self._query(node * 2 + 1, m + 1, r, ql, qr)
        l_res = self._query(node * 2, l, m, ql, qr)
        r_res = self._query(node * 2 + 1, m + 1, r, ql, qr)
        return self._merge_val(l_res, r_res)

    def update(self, i: int, val: int) -> None:
        self._update(1, 0, self._n - 1, i, val)

    def query(self, ql: int, qr: int) -> int:
        return self._query(1, 0, self._n - 1, ql, qr)

    def get(self, i: int) -> int:
        return self._query(1, 0, self._n - 1, i, i)



#xₙ₊₁ = (xₙ + a / xₙ) / 2
def mySqrt(x,epsilon=1e-6):
    if x<0:
        return "The x must be non negative"
    if not x:
        return x
    res=x
    tmp=res+epsilon*2
    while abs(res-tmp)>epsilon:
        tmp = res
        res=(res+x/res)/2
    return res


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        target = tuple(nums2)
        start = tuple(nums1)
        n = len(nums1)
        if start == target:
            return 0

        visited = set()
        queue = deque()
        queue.append((start, 0))
        visited.add(start)

        while queue:
            current, steps = queue.popleft()

            for L in range(n):
                for R in range(L, n):
                    sub = list(current[L:R + 1])
                    remaining = list(current[:L]) + list(current[R + 1:])
                    len_rem = len(remaining)
                    for insert_pos in range(len_rem + 1):
                        new_array = remaining[:insert_pos] + sub + remaining[insert_pos:]
                        new_tuple = tuple(new_array)
                        if new_tuple == target:
                            return steps + 1
                        if new_tuple not in visited:
                            visited.add(new_tuple)
                            queue.append((new_tuple, steps + 1))


a=np.array([],dtype=int)
start=time.time()
for i in range(114514):
    a=np.append(a,i)
print(a,len(a))
print(time.time()-start)

MX = 2*10**5
f = [1] * (MX+1)
g = [1] * (MX+1)
for i in range(2, MX+1):
    f[i] = f[i-1] * i % MOD
g[-1] = pow(f[-1], MOD-2, MOD)
for i in range(MX, 1, -1):
    g[i-1] = g[i] * i % MOD

comb = lambda m, n: f[m] * g[n] * g[m-n] % MOD

m, n, a, b = map(int, input().split())
x, y = a+1, b+1
ans = 0
while x <= m and y <= n:
    ans += comb(m-x+y-1,y-1)*comb(x-1+n-y,x-1)
    x += 1; y += 1
ans %= MOD
print(ans)