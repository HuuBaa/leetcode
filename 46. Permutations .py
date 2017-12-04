一、Permutations

给定一个包含不同数字数组，返回这些数字全部全排列 
[1,2,3]=>[ [1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

import itertools
return list(map(list,itertools.permutations(nums)))    

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[[]]
        for num in nums:
            n_res=[]
            for r in res:
                for i in xrange(len(r)+1):
                    #n_res.append(r[:i]+[num]+r[i:])
                    copy=r[:]
                    copy.insert(i,num)
                    n_res.append(copy)
            res=n_res
        return res

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        return self.p([],[],nums)

    def p(self,res,tmp,nums):
        if len(tmp)==len(nums):
    #这里要用tmp[:],否则添加的是tmp的引用          
            res.append(tmp[:])
            return
        for num in nums:
            if num in tmp:
                continue
            tmp.append(num)
            self.p(res,tmp,nums)
            tmp.pop()
        return res

二、Permutations ||

包含重复数字的排列 
[1,1,2]=>[1,1,2] [1,2,1] [2,1,1]

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        used=[0]*len(nums)
        nums.sort()
        return self.p([],[],used,nums)

    def p(self,res,tmp,used,nums):
        if (len(tmp)==len(nums)):
            res.append(tmp[:])
            return
        for i in range(len(nums)):
            if used[i] or (i>0 and not used[i-1] and nums[i-1]==nums[i]):
                continue
            tmp.append(nums[i])
            used[i]=1
            self.p(res,tmp,used,nums)
            tmp.pop()
            used[i]=0
        return res

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[[]]
        for n in nums:
            n_res=[]
            for r in res:
                for i in xrange(len(r)+1):                   
                    copy=r[:]
                    copy.insert(i,n)
                    n_res.append(copy)
                    if i<len(r) and r[i]==n:
                        break
            res=n_res
        return res