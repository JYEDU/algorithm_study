class Solution(object):
    def twoSum(self, nums, target):
        """
        link : https://leetcode.com/problems/two-sum/
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        no=len(nums)
        for i in range(no):
            for j in range(no):
                if i!=j and nums[i]+nums[j]==target:
                    return [i, j]
            