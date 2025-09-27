# 灵神模板整理:https://github.com/Jipcon/Template.git
# 线段树有两个下标,一个是线段树节点的下标,另一个是线段树维护的区间的下标
# 节点的下标:从 1 开始
# 区间的下标:从 0 开始
class SegmentTree: #无区间更新线段树
    def __init__(self, nums,default=0):
        if isinstance(nums, int):
            nums=[default]*nums
        n = len(nums)
        self._n=n
        self._tree=[0]*(2<<(n-1).bit_length())
        self._build(nums,1,0,n-1)

    #用数组nums初始化线段树
    #时间复杂度O(n)
    def _build(self,nums,node,left,right):
        if left==right: #叶子节点
            self._tree[node]=nums[left]
            return
        mid=(left+right)>>1
        self._build(nums,node*2,left,mid)
        self._build(nums,node*2+1,mid+1,right)
        self._maintain(node)

    def _maintain(self,node):
        self._tree[node]=self._merge_val(self._tree[node*2],self._tree[node*2+1])

    def _merge_val(self,a,b):
        return max(a,b)

    def _update(self,node,left,right,idx,val):
        if left==right:
            self._tree[node]=self._merge_val(self._tree[node*2],val)
            return
        mid=(left+right)>>1
        if idx<=mid:
            self._update(node*2,left,mid,idx,val)
        else:
            self._update(node*2+1,mid+1,right,idx,val)
        self._maintain(node)

    #查询[ql,qr]内的最op值(max or min etc.)
    def _query(self,node,left,right,ql,qr):
        if ql<=left and qr>=right:
            return self._tree[node]
        mid=(left+right)>>1
        if qr<=mid: #[ql,qr]在左子树
            return self._query(node*2,left,mid,ql,qr)
        if ql>=mid: #[ql,qr]在右子树
            return self._query(node*2+1,mid+1,right,ql,qr)
        left_res=self._query(node*2,left,mid,ql,qr)
        right_res=self._query(node*2+1,mid+1,right,ql,qr)
        return self._merge_val(left_res,right_res)

    def update(self,idx,val):
        self._update(1,0,self._n-1,idx,val)

    def query(self,ql,qr):
        return self._query(1,0,self._n-1,ql,qr)

    def get_value(self,idx):
        return self._query(1,0,self._n-1,idx,idx)


class Node:
    __slots__ = 'val','todo'

class LazySegmentTree:
    _TODO_INIT=0 #根据题目修改

    def __init__(self, nums, default=0):
        if isinstance(nums, int):
            nums=[default]*nums
        n=len(nums)
        self._n=n
        self._tree=[Node() for _ in range(2<<(n-1).bit_length())]
        self._build(nums,1,0,n)

    def _build(self,nums,node,left,right):
        self._tree[node].todo=self._TODO_INIT
        if left==right:
            self._tree[node]=nums[left]
            return
        mid=(left+right)>>1
        self._build(nums,node*2,left,mid)
        self._build(nums,node*2+1,mid+1,right)
        self._maintain(node)

    def _maintain(self,node):
        self._tree[node]=self._merge_val(self._tree[node*2].val,self._tree[node*2+1].val)

    def _merge_val(self,a,b):
        return a+b #根据题目修改

    def _merge_todo(self,a,b):
        return a+b

