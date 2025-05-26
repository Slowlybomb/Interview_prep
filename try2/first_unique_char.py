# Time Complexity: O(n)

def first_unique_char(s: str) -> int:
    """
    Given a string, return the index of the first non-repeating character. 
    If it doesn't exist, return -1.
    
    Example:
    Input: "lleetcode"
    Output: 2 (character 'e')
    """

    # Count each character
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first character with count == 1
    for index, char in enumerate(s):
        if char_count[char] == 1:
            return index

    return -1


if __name__ == "__main__":
    s = "leetcode"
    print(first_unique_char(s))  # Output: 0
