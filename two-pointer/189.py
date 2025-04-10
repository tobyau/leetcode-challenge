class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        reverse array and reverse sub array 
        space: O(1) in place 
        """
        k = k % len(nums) 

        def reverseArray(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1 
                end -= 1 

        reverseArray(0, len(nums)-1)
        reverseArray(0, k-1)
        reverseArray(k, len(nums)-1)

        return nums