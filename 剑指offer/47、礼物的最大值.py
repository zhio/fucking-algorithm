from typing import List


def maxValue(gird: List[List[int]]) -> int:
    m, n = len(gird), len(gird[0])
    for j in range(1, n):
        gird[0][j] += gird[0][j - 1]
    for i in range(1, m):
        gird[i][0] += gird[i - 1][0]
    for i in range(1, m):
        for j in range(1, n):
            gird[i][j] += max(gird[i][j - 1], gird[i - 1][j])
    return gird[-1][-1]
