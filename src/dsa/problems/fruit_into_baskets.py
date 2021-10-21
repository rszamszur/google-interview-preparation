"""https://leetcode.com/problems/fruit-into-baskets/"""


def total_fruit(fruits):
    """
    Time complexity: O(n)
    Space complexity: O(1)

    You want to collect as much fruit as possible. However, the owner has some
    strict rules that you must follow:

    1) You only have two baskets, and each basket can only hold a single type
    of fruit. There is no limit on the amount of fruit each basket can hold.
    2) Starting from any tree of your choice, you must pick exactly one fruit
    from every tree (including the start tree) while moving to the right.
    The picked fruits must fit in one of your baskets.
    3) Once you reach a tree with fruit that cannot fit in your baskets, you
    must stop.

    Args:
        fruits(List[int]): An integer array of fruits where fruits[i] is the
            tree type.

    Returns:
        The maximum number of fruits you can pick.

    """
    max_fruits = 0
    count = 0
    i = 0
    baskets = []

    while i < len(fruits):
        if not baskets:
            baskets.append(fruits[i])
            count += 1
        elif len(baskets) == 1:
            count += 1

            if baskets[0] != fruits[i]:
                baskets.append(fruits[i])
        else:
            if fruits[i] in baskets:
                count += 1
            else:
                baskets = []
                count = 0
                i -= 1
                while fruits[i] == fruits[i - 1]:
                    i -= 1

                if (len(fruits) - i) <= max_fruits:
                    break

                continue

        i += 1
        max_fruits = max(max_fruits, count)

    return max_fruits
