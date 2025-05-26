import time

def majorityElement_hashmap(nums: list[int]) -> int:
    """Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times. 
    You may assume that the majority element always exists in the array.
    
    Example 1:

    Input: nums = [3,2,3]
    Output: 3
    Example 2:

    Input: nums = [2,2,1,1,1,2,2]
    Output: 2"""

    # Time Complexity: O(n), Space Complexity: O(n).
    n_dict = {}
    for num in nums:
        n_dict[num] = n_dict.get(num, 0) + 1
        if n_dict[num] > len(nums) // 2:
            return num

def majorityElement_moores(nums: list[int]) -> int:
    candidate = -1
    votes = 0
    
    # Time Complexity: O(n), Space Complexity: O(1).
    for i in range(len(nums)):
        
        if votes == 0:
            candidate = nums[i]
            votes = 1
        else:
            if (nums[i] == candidate):
                votes += 1
            else:
                votes -= 1
    return candidate


if __name__ == "__main__":
    nums = [2,2,1,1,1,2,2,1,1,1,1,1,12,233,2,3,3,3,1,1,12,2,2,23,4,66,6,6,6,6,6,6,66,5,3,14,9,9,7,3,2,1,2,3,4,5,6,7,8,9,0,1,2,3,3,3,3,6,6,6,6,6,6,6,63,6,7,9,0,5,2,1,1]

    # Hashmap
    start_time = time.perf_counter()
    print("Hashmap result:", majorityElement_hashmap(nums))
    end_time = time.perf_counter()
    print(f"Hashmap time: {(end_time - start_time):.6f} seconds")

    # Moore's Voting
    start_time = time.perf_counter()
    print("Moore's result:", majorityElement_moores(nums))
    end_time = time.perf_counter()
    print(f"Moore's time: {(end_time - start_time):.6f} seconds")