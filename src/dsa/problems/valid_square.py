"""https://leetcode.com/problems/valid-square/

This solution is not most readable and in the tiniest lines of code, but I wanted to
solve it with pure math just for fun.
Valid square will be when its diagonals intersect at 90-degree angle, and the
point of intersection is in the middle of both diagonals. Since points provided
on input can be in any order; with this approach, I only need to check three
permutations of those points (possible square diagonals).
"""


def calc_line_len(x1, y1, x2, y2):
    """Calculate line section length.

    Time complexity: O(1)
    Space complexity: O(1)

    Args:
        x1(int): Line section start x value.
        y1(int): Line section start y value.
        x2(int): Line section end x value.
        y2(int): Line section end y value.

    Returns:
        Line section lenght (float).

    """
    line_len = ((abs(x2 - x1) ** 2) + (abs(y2 - y1) ** 2)) ** 0.5

    return line_len


def calc_line_equation(x1, y1, x2, y2):
    """Calculate linear equation coefficients.

    Time complexity: O(1)
    Space complexity: O(1)

    Args:
        x1(int): Line point A x value.
        y1(int): Line point A y value.
        x2(int): Line point B x value.
        y2(int): Line point B y value.

    Returns:
        Linear equation coefficients (float).

    """
    if x1 == x2:
        return 0, x1

    try:
        a = (y2 - y1) / (x2 - x1)
    except ZeroDivisionError:
        a = 0
    b = y1 - (a * x1)

    return a, b


def valid_square(p1, p2, p3, p4):
    """
    Time complexity: O(1)
    Space complexity: O(1)

    Args:
        p1(list[int]): Point 1 x, y coordinates.
        p2(list[int]): Point 2 x, y coordinates.
        p3(list[int]): Point 3 x, y coordinates.
        p4(list[int]): Point 4 x, y coordinates.

    Returns:
        True if the four points construct a square, otherwise false.

    """
    possible_diagonals = [
        ([p1, p4], [p2, p3]),
        ([p1, p2], [p3, p4]),
        ([p1, p3], [p2, p4]),
    ]

    for d1, d2 in possible_diagonals:
        if d1 == d2:
            return False

        a1, b1 = calc_line_equation(d1[0][0], d1[0][1], d1[1][0], d1[1][1])
        a2, b2 = calc_line_equation(d2[0][0], d2[0][1], d2[1][0], d2[1][1])

        if a1 == a2 == 0:
            cx = d1[0][0] if d1[0][0] == d1[1][0] else d2[0][0]
            cy = d1[0][1] if d1[0][1] == d1[1][1] else d2[0][1]
        elif round((a1 * a2), 4) == -1:
            try:
                cx = (b1 - b2) / (a2 - a1)
            except ZeroDivisionError:
                cx = 0
            try:
                cy = (a1 * cx) + b1
            except ZeroDivisionError:
                cy = 0
        else:
            continue

        l1 = round(calc_line_len(d1[0][0], d1[0][1], cx, cy), 4)
        l2 = round(calc_line_len(d1[1][0], d1[1][1], cx, cy), 4)
        l3 = round(calc_line_len(d2[0][0], d2[0][1], cx, cy), 4)
        l4 = round(calc_line_len(d2[1][0], d2[1][1], cx, cy), 4)

        if l1 == l2 == l3 == l4:
            return True

    return False
