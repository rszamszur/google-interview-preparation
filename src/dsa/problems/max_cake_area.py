"""https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts"""


def max_cake_area(h, w, horizontal_cuts, vertical_cuts):
    """
    Time complexity: O(n*log(n))
    Space complexity: O(1)

    Args:
        h (int): Given cake height.
        w (int): Given cake width.
        horizontal_cuts (List[int]): The ``horizontal_cuts[i]`` is the distance
            from the top of the rectangular cake to the ``ith`` horizontal cut.
        vertical_cuts (List[int]): The ``vertical_cuts[j]`` is the distance from
            the left of the rectangular cake to the ``jth`` vertical cut.

    Returns:
        The maximum area of a piece of cake after you cut at each horizontal and
         vertical position provided in the arrays ``horizontal_cuts`` and
         ``vertical_cuts``. Since the answer can be a large number, return this
         modulo ``10**9 + 7``.

    """
    horizontal_cuts.append(0)
    vertical_cuts.append(0)
    horizontal_cuts.append(h)
    vertical_cuts.append(w)

    horizontal_cuts = sorted(horizontal_cuts)
    vertical_cuts = sorted(vertical_cuts)

    max_h = max_v = 0

    for i in range(len(horizontal_cuts) - 1):
        max_h = max(
            max_h,
            (horizontal_cuts[i + 1] - horizontal_cuts[i]),
        )

    for i in range(len(vertical_cuts) - 1):
        max_v = max(
            max_v,
            (vertical_cuts[i + 1] - vertical_cuts[i]),
        )

    return (max_v * max_h) % ((10 ** 9) + 7)
