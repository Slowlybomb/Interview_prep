def judge_circle(moves: str) -> bool:
    """
    The robot moves with instructions like "U", "D", "L", "R" (up, down, left, right). 
    Return True if the robot returns to the origin after executing all moves.

    Input: "UDLR"

    Output: True"""
    x = 0
    y = 0

    for char in moves:
        match char:
            case 'U':
                y += 1
            case 'D':
                y -= 1
            case 'L':
                y -= 1
            case 'R':
                y += 1
    if x == 0 and y == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    moves = "UDLR"
    print(judge_circle(moves))