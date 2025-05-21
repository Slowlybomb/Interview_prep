"""Space Complexity:

O(m × n) for the memo table (2D list).
O(m + n) for recursion stack in the worst case 
(since at most m + n calls will be active at once in the recursion tree)."""

def unique_paths(m: int, n: int) -> int:
    """Prompt:

    Given a [m x n] grid, a robot can only move either down or right. 
    
    Count how many unique paths it can take from top-left to bottom-right.
    
    Example:
    m = 3, n = 2
    Output: 3"""
    def countPaths(m, n, memo):
        if n == 1 or m == 1:
            memo[m][n] = 1
            return 1

        # Add the element in the memo table
        # If it was not computed before
        if  memo[m][n] == 0:
            memo[m][n] = countPaths(m-1,n, memo) + \
                countPaths(m,n-1, memo)

        return  memo[m][n]
    
    def number_of_paths(m, n):
  	
        memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        ans = countPaths(m, n, memo)
        return ans

    return number_of_paths(m, n)

if __name__ == "__main__":
    n, m = 3, 3

    res = unique_paths(m, n)
    print(res)