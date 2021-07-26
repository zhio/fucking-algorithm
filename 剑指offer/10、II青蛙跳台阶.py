"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2
示例 2：

输入：n = 7
输出：21
示例 3：

输入：n = 0
输出：1
提示：

0 <= n <= 100
"""

"""
动态规划  
当为 1 级台阶： 剩 n-1 个台阶，此情况共有 f(n−1) 种跳法；
当为 2 级台阶： 剩 n-2 个台阶，此情况共有 f(n−2) 种跳法。

状态方程 f(n) = f(n-1) + f(n-2)
"""


def numWays(n: int) -> int:
    dp = {}
    dp[0] = 1
    dp[1] = 1
    if n > 1:
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n] % 1000000007


def numWays2(n: int) -> int:
    a, b = 1, 1
    for _ in range(n):
        a, b = b, (a + b) % 1000000007
    return a


if __name__ == '__main__':
    n = 7
    print(numWays(n))
    print(numWays2(n))
