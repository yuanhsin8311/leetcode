"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
# Method 1: O(n)
class Solution(object):
	def twoSum(self, nums, target):
		for i in xrang(len(nums)):
			for j in xrange(i+1,len(nums)):
				if target - nums[j] == nums[i]:
					return [i,j]

# Method 2: heap table / O(1)
class Solution(object):
	def twoSum(self, nums, target):
		dict = {}
		for i, num in enumerate(nums):
			dict[num] = i
		for i, num in enumerate(nums):
			if target - num in dict and dict[target-num] != i:
				return (i,dict[target-num])

## 優化解法
class Solution(object):
	def twoSum(self, nums, target):
		dict = {}
		for i, num in enumerate(nums):
			if target - num in dict:
				return (i, dict[target-num])
			else:
				dict[num] = i
