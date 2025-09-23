# 在文本串 text 中查找模式串 pattern，返回所有成功匹配的位置（pattern[0] 在 text 中的下标）
def kmp(text: str, pattern: str):
    m = len(pattern)
    pi = [0] * m
    cnt = 0
    for i in range(1, m):
        b = pattern[i]
        while cnt and pattern[cnt] != b:
            cnt = pi[cnt - 1]
        if pattern[cnt] == b:
            cnt += 1
        pi[i] = cnt

    pos = []
    cnt = 0
    for i, b in enumerate(text):
        while cnt and pattern[cnt] != b:
            cnt = pi[cnt - 1]
        if pattern[cnt] == b:
            cnt += 1
        if cnt == len(pattern):
            pos.append(i - m + 1)
            cnt = pi[cnt - 1]
    return pos


# 计算并返回 z 数组，其中 z[i] = |LCP(s[i:], s)|
def calc_z(s: str):
    n = len(s)
    z = [0] * n
    box_l = box_r = 0
    for i in range(1, n):
        if i <= box_r:
            z[i] = min(z[i - box_l], box_r - i + 1)
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            box_l, box_r = i, i + z[i]
            z[i] += 1
    z[0] = n
    return z


def longestPalindrome(s: str) -> str:
    t='#'.join('^'+s+'$')
    # half_len[i] 表示在 t 上的以 t[i] 为回文中心的最长回文子串的回文半径
    half_len=[1]*(len(t)-2) #从第一个#开始遍历,在最后一个#结束,所以长度为2n-2
    # 举例s=aba,改造后t=^#a#b#a#$,则t[1]=#(单个字符长度为1)
    box_m=box_r=mx=0
    for i in range(2,len(half_len)):
        hl=1
        if i<box_r: #i在右边界内
            hl=min(half_len[box_m*2-i],box_r-i)
        while t[i-hl]==t[i+hl]:
            hl+=1
            box_m,box_r=i,i+hl

        #更新最大长度
        half_len[i]=hl
        if hl>half_len[mx]:
            #出现最大长度回文子串的下标
            mx=i
    hl=half_len[mx]
    #原字符串s中的下标i在t中映射为2(i+1),则t中下标i'=2*(i+1)=2i+2,(i'-2)//2=i
    #hl-1=最大回文串的长度,(mx-2)//2=i,mx+hl
    return s[(mx-hl)//2:(mx+hl)//2-1] #本质上是s[(mx-hl)//2]到s[(mx+hl-1)//2],hl为包括中心到右边界的长度