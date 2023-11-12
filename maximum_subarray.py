# https://leetcode.com/problems/maximum-subarray/

def maxSubArray(nums: list[int]) -> int:
    curr_max = nums[0]
    max_sum = nums[0]

    for n in nums[1:]:
        curr_max = max(curr_max + n, n)
        max_sum = max(max_sum, curr_max)

    return max_sum

# print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])) #6
# print(maxSubArray([5, 4, -1, 7, 8])) #23
