"""https://leetcode.com/problems/letter-tile-possibilities"""


def letter_tile_possibilities(tiles):
    """
    Time complexity: O(V + E) where V: vertices, E: edges.
    Space complexity: O(V)

    Args:
        tiles(str): Given str with n tiles, where each tile has one letter
            tiles[i] printed on it.

    Returns:
        The number of possible non-empty sequences of letters you can make
        using the letters printed on those tiles.

    """
    paths = set()
    stack = [(tiles[i], tiles[:i] + tiles[i + 1:]) for i in range(len(tiles))]

    while stack:
        path, available = stack.pop()

        if path in paths:
            continue

        paths.add(path)

        for i in range(len(available)):
            stack.append(
                (path + available[i], available[:i] + available[i + 1:])
            )

    return len(paths)
