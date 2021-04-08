'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [], target = 0
Output: []
'''

# O(n^3) -> Two-pointer solution
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)<4:
            return []
        nums.sort()
        result = []
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):

                k,m = j+1, len(nums)-1
                while k<m:
                    if nums[i]+nums[j]+nums[k]+nums[m]==target:
                        r = [nums[i],nums[j],nums[k],nums[m]]
                        r.sort()
                        if r not in result:
                            result.append(r)
                        k+=1

                    if nums[i]+nums[j]+nums[k]+nums[m]<target:
                        k+=1
                    if nums[i]+nums[j]+nums[k]+nums[m]>target:
                        m-=1
        return result
