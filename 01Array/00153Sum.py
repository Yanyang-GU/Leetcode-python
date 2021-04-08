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
        
