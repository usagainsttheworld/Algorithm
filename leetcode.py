"""
#1 "Reverse digits of an integer"

Example1: x = 123, return 321
Example2: x = -123, return -321

Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

class Solution:
	# @param {integer} x
	# @return {integer}
	def reverse(self, x):
		reversed_abs = int(str(abs(x))[::-1])
		if reversed_abs > 2147483647:
			return 0
		else:
			if x < 0:
				reversed_int = - reversed_abs
			else:
				reversed_int = reversed_abs
			return reversed_int

"""
#2 "Length of Last Word"
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.
"""
class Solution:
	# @param {string} s
	# @return {integer}
	def lengthOfLastWord(self, s):
		idx_i = 1
		if s == "":
			return 0
		else:
			while idx_i != len(s) and s[-idx_i] == " ":
				idx_i += 1
			idx_j = idx_i
			while idx_j <= len(s) and s[-idx_j] != " ":
				idx_j += 1
			return idx_j - idx_i

"""
#3 "Contains Duplicate"

Given an array of integers, find if the array contains any duplicates. 

Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.
"""
class Solution:
	# @param {integer[]} nums
	# @return {boolean}
	def containsDuplicate(self, nums):
		no_dup = list(set(nums))
		if len(no_dup) == len(nums):
			return False 
		else:
			return True 

"""
#4 "Contains Duplicate II"

Given an array of integers and an integer k, 

find out whether there are two distinct indices i and j in the array 
such that nums[i] = nums[j] and the difference between i and j is at most k.
"""
class Solution:
	# @param {integer[]} k
	# @param {integer} k
	# @return {boolean}
	def containsNearbyDuplicate(self, nums, k):
		if len(list(set(nums))) == len(nums):
			return False 
		else:
			for idx_i in range (len(nums)):
				for idx_j in range (idx_i+1, len(nums)):
					if nums[idx_i] == nums[idx_j] and idx_j - idx_i <= k:
						return True
			return False

"""
#5 "Happy Number"

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by the sum of the squares 
of its digits, and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 

Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

"""
list = set()
class Solution:
	# @param {integer} n
	# @return {boolean} 
	
	def qua_sum(self, number):
		global list
		sum = 0
		for each_num in str(number):
			sum += int(each_num)*int(each_num)
		print "list is", list
		if sum in list:
			return False
		else:
				list.add(sum)
		return sum

	def isHappy(self, n):
		if n == 1:
			return True
		else:
			result = self.qua_sum(n)
			if  result == False:
				return False
			else:
				return self.isHappy(result)

"""
#6 "Majority Element"

Given an array of size n, find the majority element. 

The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""
class Solution:
	# @param {integer[]} nums
	# @return {integer}
	def majorityElement(self, nums):
		



test = Solution()
print test.isHappy(7)

