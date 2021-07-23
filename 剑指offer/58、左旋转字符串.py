"""
 字符串切片 ， 列表遍历拼接 ， 字符串遍历拼接
"""

def reverseLeft(s:str,n:int) -> str:
    return s[n:] + s[:n]

def reverseLeft2(s:str,n:int) -> str:
    res = []
    for i in range(n,len(s)):
        res.append(s[i])
    for i in range(n):
        res.append(s[i])
    # for i in range(n,n+len(s)):
    #     res.append(s[i%len(s)])
    return ''.join(res)

def reverseLeftWords(s:str,n:int) -> str:
    res = ""
    for i in range(n,len(s)):
        res += s[i]
    for i in range(n):
        res += s[i]
    return res


