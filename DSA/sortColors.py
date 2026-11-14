class Solution:
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                self.swap(nums, i, right)
                right -= 1
            else:
                self.swap(nums, i, left)
                left += 1
                i += 1

nums = [2, 0, 2, 1, 1, 0]
Solution().sortColors(nums)
print(nums)