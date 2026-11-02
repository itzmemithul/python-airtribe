class Solution:
    def findEquilibrium(self, arr):
        total_sum = sum(arr)
        left_sum = 0
        for i in range(1, len(arr)):
            left_sum += arr[i - 1]
            right_sum = total_sum - left_sum - arr[i]
            if left_sum == right_sum:
                return i
        return -1




print(Solution().findEquilibrium([-7, 1, 5, 2, -4, 3, 0]))

# def find_equilibrium(arr):
#     left_sum = 0
#     for i in range(1, len(arr)):
#         left_sum += arr[i - 1]
#         right_sum = sum(arr[i + 1:])
#         if left_sum == right_sum:
#             return i
#     return -1


# print(find_equilibrium([1, 2, 0, 3]))
# # print(find_equilibrium([1, 2, 0, 3]))