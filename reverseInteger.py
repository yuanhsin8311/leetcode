"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
"""
"""
[Hint]
123  3*10*10 + 2 *10 + 1
123  remainder = 123 % 10 = 3
     123/10 = 12...3

     12 % 10 = 2
     12/10=1..2

	 1 % 10 = 0
	 1/10 = 0..1

	 0 % 10 = 0
	 0/10 = 0 ..0
"""
class Solution(object):
	def reverse(self, x):
		result = 0
		# step1: judge result is positive or negative
		if x > 0 :
			sign = 1
		else:
			sign = -1
			x = -x
		# step2: reverse
		while x > 0:
			# get first remainder as reversed first digit
			value = x % 10
			result = result * 10 + value
			x = int(x/10)
		# step3: outflows
		if result > 2147483647 or result < -2147483648:
			result = 0
		# step4: return result
		return result * sign
def execute():
	sol = Solution()
	print (sol.reverse(-1234))
