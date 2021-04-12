'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
'''
#O(2log(n)) -> 2 mid searches, 1st finds the rotating pivot and 2nd finds the target's index
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        l,r=0,N-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            if nums[mid]<nums[r]:
                r=mid
        pivot = l
        l,r=0,N-1
        while l<=r:
            mid = (l+r)//2
            mid2 = (mid+pivot)%N
            if nums[mid2]==target:
                return mid2
            elif nums[mid2]<target:
                l=mid+1
            else:
                r=mid-1
        return -1
