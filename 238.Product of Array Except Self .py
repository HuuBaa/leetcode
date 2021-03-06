# Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Solve it without division and in O(n).

# For example, given [1,2,3,4], return [24,12,8,6].

# Follow up:
# Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

#第一次从左至右遍历，每个元素乘以它左边所有元素的积
#第二次从右至左遍历，每个元素乘以它右边所有元素的积 
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p=1
        l=len(nums)
        res=[1]*l
        for i in range(l):
            res[i]*=p
            p*=nums[i]
        p=1
        for i in range(l-1,-1,-1):
            res[i]*=p
            p*=nums[i]
        return res