#灵神模板整理:https://github.com/Jipcon/Template.git
class XorBasis:
    def __init__(self,n):
        self.b=[0]*n

    def insert(self,x):
        b=self.b
        for i in range(len(b)-1,-1,-1):
            if x>>i and not b[i]:
                b[i]=x
                return
            x^=b[i]

    def max_xor(self):
        b=self.b
        res=0
        for i in range(len(b)-1,-1,-1):
            if res^b[i]>res:
                res^=b[i]
        return res
