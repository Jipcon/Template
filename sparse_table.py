import time
import numpy as np

class SparseTable:
    def __init__(self,a,op):
        n=len(a)
        w=n.bit_length()
        st=[[0]*n for _ in range(w)]
        st[0]=a[:]
        for i in range(1,w):
            for j in range(n-(1<<(i-1))):
                st[i][j]=op(st[i-1][j],st[i-1][j+(1<<(i-1))])
        self.st=st
        self.op=op

    def query(self,l,r):
        k=(r-l).bit_length()-1
        return self.op(self.st[k][l],self.st[k][r-(1<<k)])

nums=[3,1,4,1,5,9,2,6]
st=SparseTable(nums,max)
print(st.query(1,4))
print(st.query(0,5))