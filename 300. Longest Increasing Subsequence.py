#  Given an unsorted array of integers, find the length of longest increasing subsequence.

# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

# Your algorithm should run in O(n2) complexity.

# Follow up: Could you improve it to O(n log n) time complexity? 

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return len(nums)
        
        import bisect
        s=[nums[0]]
        for n in nums:            
            if n <= s[0]:
                s[0]=n
            elif n>s[-1]:
                s.append(n)
            else:
                i=bisect.bisect_left(s,n)
                s[i]=n
        return len(s)                


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        dp=[1]*len(nums)
        for i in xrange(len(nums)):
            for j in xrange(i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
            res=max(res,dp[i])
        return res
            