'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.


Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

# O(n^2) -> Two-pointer problem left++ and right--
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 1001
        result = 0
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                if res > abs(sum3 - target):
                    res = abs(sum3-target)
                    result=sum3
                if sum3 - target == 0:
                    return target
                elif sum3 - target > 0:
                    r -= 1
                else:
                    l += 1
        return result
