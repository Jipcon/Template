#灵神模板整理:
class NumArray:
    __slots__ = 'nums', 'tree'

    def __init__(self, nums):
        n = len(nums)
        self.nums = [0] * n
        self.tree = [0] * (n + 1)
        for i, x in enumerate(nums):
            self.update(i, x)

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        i = index + 1
        while i < len(self.tree):
            self.tree[i] += delta
            i += (i & -i)  # lowbit

    def prefixSum(self, i):  # 右端点为i的数组前缀和
        s = 0
        while i:
            s += self.tree[i]
            i &= i - 1  # 等效 i-= i&-i (减去lowbit)
        return s

    def sumRange(self, left, right):
        return self.prefixSum(right + 1) - self.prefixSum(left)