'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]
'''
# 13(<-pivot)[54(<-swap)32]: 
# 1. from right to left find the first non ascending pivot number; 
# 2. find the fist number that is greater than pivot in the [bracket], and swap
# 3. sort the [bracket]
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 32321
        pivot = 0
        swap = -1
        for i in range(len(nums)-1,0,-1):
            if nums[i-1] < nums[i]:
                pivot = i-1
                break
            else:
                if i==1:
                    nums.sort()
                    return
        
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[pivot]:
                break
            swap -= 1

        nums[pivot],nums[swap] = nums[swap],nums[pivot]
        nums[pivot+1:]=sorted(nums[pivot+1:])
