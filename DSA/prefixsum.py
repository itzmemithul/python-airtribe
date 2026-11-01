arr = [8,2,9,4,6,8,5]
def prefix_sum(arr, i , j):
    prefixSum = [0 for _ in range(len(arr))]
    prefixSum[0] = arr[0]
    for k in range(1, len(arr)):
        prefixSum[k] = prefixSum[k - 1] + arr[k]
    if i == 0:
        return prefixSum[j]
    else:
        return prefixSum[j] - prefixSum[i-1]

print(prefix_sum(arr, 2, 5))
