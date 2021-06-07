"""
找出数组中重复的数字。 


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请
找出数组中任意一个重复的数字。 

示例 1： 

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 




限制： 

2 <= n <= 100000 
Related Topics 数组 哈希表
"""
from typing import List


"""
使用hash
"""
def findRepeatNumber(nums: List[int]) -> int:
	n = len(nums)
	hash_map = {}
	for i in range(n):
		if nums[i] not in hash_map:
			hash_map[nums[i]] = 0
		else:
			hash_map[nums[i]] += 1
	return [k for k, v in hash_map.items() if v > 0][0]

"""
使用set
"""
def findRepeatNumberBySet(nums: List[int]) -> int:
	num_set = set()
	for num in nums:
		if num in num_set:
			return num
		num_set.add(num)
	return -1

"""
原地交换
"""
def findReqeatNumberByOther(nums :List[int]) -> int:
	i = 0
	while i < len(nums):
		if nums[i] == i:
			i += 1
			continue
		if nums[nums[i]] == nums[i]: return nums[i]
		nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
	return -1


if __name__ == '__main__':
	nums = [2, 3, 1, 0, 2, 5, 3]
	print(findRepeatNumber(nums))
	print(findRepeatNumberBySet(nums))
	print(findReqeatNumberByOther(nums))