'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
'''
#

# Initial trial O(n^3)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    tri = [nums[i],nums[j],nums[k]]
                    tri.sort()
                    if i!=j and i!=k and j!=k and nums[i]+nums[j]+nums[k]==0 and tri not in result:
                        result.append(tri)
        
        return result
        
# O(n^2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l<r:
                sum3 = nums[i]+nums[l]+nums[r]
                if sum3==0:
                    if [nums[i], nums[l], nums[r]] not in result:
                        result.append([nums[i], nums[l], nums[r]])
                    l+=1
                elif sum3<0:
                    l+=1
                else:
                    r-=1
        return result
       
# Improved O(n^2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        length = len(nums)
        for i in range(length-2):
            # remove dulicate
            if i and nums[i]==nums[i-1]:
                continue
            l = i+1
            r = length-1
            while l<r:
                sum3 = nums[i]+nums[l]+nums[r]
                if sum3==0:
                    result.append([nums[i], nums[l], nums[r]])
                    l+=1
                    # remove duplicates
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                        continue
                elif sum3<0:
                    l+=1
                else:
                    r-=1
        return result
