"""
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
"""

"""
递归
判断第一个字符是否匹配
如果p第一个字符为*号，匹配0个或者多个
0个忽略p中的前两个元素
多个忽略s中的第一个元素

"""
def isMatch(s: str, p: str) -> bool:
	if not p:
		 return not s
	# 第一个字符是否匹配
	first_match = bool(s and (p[0] in (s[0], '.')))
	# 判断第二个字符号是否为*
	if len(p) >= 2 and p[1] == '*':
		return isMatch(s, p[2:]) or first_match and isMatch(s[1:], p)
	else:
		return first_match and isMatch(s[1:], p[1:])

if __name__ == '__main__':
	s = "mississippi"
	p = "mis*is*p*."
	print(isMatch(s, p))
	s = "ab"
	p = ".*c"
	print(isMatch(s, p))