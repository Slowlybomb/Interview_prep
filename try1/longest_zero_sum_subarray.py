"""Time Complexity:

O(n) where n is the length of the array.

You traverse the array only once (for i in range(len(arr))) 
and perform O(1) operations inside the loop 
(dictionary lookups and updates are constant time on average)."""

def longest_zero_sum_subarray(arr: list[int]) -> int:
    s_dict = {}
    max_length = 0
    counter = 0

    for i in range(len(arr)):
        counter += arr[i]

        if counter == 0:
            max_length = i + 1
        elif counter in s_dict:
            max_length = max(max_length, i - s_dict[counter])
        else:
            s_dict[counter] = i

    return max_length

if __name__ == "__main__":
    arr = [1, 2, -3, 3, -1, 2, -2]
    print(longest_zero_sum_subarray(arr))
