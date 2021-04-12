'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
'''
# O(log(n)) -> binary search
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        N=len(nums)
        l,r =0, N-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                l,r=mid,mid
                while l>0:
                    if nums[l-1]==target:
                        l-=1
                    else:
                        break
                while r<N-1:
                    if nums[r+1]==target:
                        r+=1
                    else:
                        break
                return[l,r]
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return [-1,-1]
