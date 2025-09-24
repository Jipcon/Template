#灵神模板整理:https://github.com/Jipcon/Template.git
class UnionFind:
    def __init__(self, n: int):
        self._fa = list(range(n))
        self._size = [1] * n
        self.cc = n

    def find(self, x: int) -> int:
        if self._fa[x] != x:
            self._fa[x] = self.find(self._fa[x])
        return self._fa[x]

    def is_same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def merge(self, from_: int, to: int) -> bool:
        x, y = self.find(from_), self.find(to)
        if x == y:
            return False
        self._fa[x] = y
        self._size[y] += self._size[x]
        self.cc -= 1  #
        return True

    # 返回 x 所在集合的大小
    def get_size(self, x: int) -> int:
        return self._size[self.find(x)]
