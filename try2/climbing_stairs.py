def climb_stairs(n: int) -> int:
    """
    You can climb 1 or 2 steps. Count how many distinct ways you can climb to the top (step n).
    
    Input: n = 4
    Output: 5
    Explanation: [1+1+1+1], [1+1+2], [1+2+1], [2+1+1], [2+2]
    """

    if n <= 2:
        return n

    # Using dynamic programming / iteration
    a, b = 1, 2  # base cases: 1 way to climb 1 step, 2 ways to climb 2 steps
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    n = 4
    print(climb_stairs(n))  # Output: 5



def climb_stairs(n: int) -> int:
    def recursion_count(k, n):
        if k == n:
            return 1
        if k > n:
            return 0
        return recursion_count(k + 1, n) + recursion_count(k + 2, n)

    return recursion_count(0, n)


if __name__ == "__main__":
    n = 4
    print(climb_stairs(n))  # Output: 5
