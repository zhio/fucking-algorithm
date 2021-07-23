from typing import List
from collections import deque


def maxSildingWindow(nums:List[int],k:int) -> List[int]:
    if not nums or k == 0: return []
    deques = deque()
    for i in range(k):
        while deques and deques[-1]< nums[i]:
            deques.pop()
        deques.append(nums[i])
    res = [deques[0]]

    for i in range(k,len(nums)):
        if deques[0] == nums[i-k]:
            deques.popleft()
        while deques and deques[-1]< nums[i]:
            deques.pop()
        deques.append(nums[i])
        res.append(deque[0])
    return res