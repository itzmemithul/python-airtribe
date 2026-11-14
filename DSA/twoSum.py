nums = [3,2,4]
target = 6
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []

def twoSumHashMap(nums: list[int], target: int) -> list[int]:
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
        print(f"num_map: {num_map}, complement: {complement}, i: {i}")
    return []

print(twoSumHashMap(nums, target))  # Output: [1, 2]