def subarray_sum_equals_k(nums: list[int], k: int) -> int:
    """ Subarray Sum Equals K

    Given an array of integers and an integer k, 
    return the total number of continuous subarrays 
    whose sum equals to k.

    Input: nums = [1, 1, 1], k = 2 

    Output: 2

    Explanation: [1,1] occurs twice."""

    count = 0
    current_sum = 0
    prefix_sums = {0: 1}
    
    for num in nums:
        current_sum += num
        count += prefix_sums.get(current_sum - k, 0)
        prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
    
    return count

if __name__ == "__main__":
    nums = [3, 4, 7, 2, -3, 1, 4, 2]
    k = 7
    print(subarray_sum_equals_k(nums, k))

