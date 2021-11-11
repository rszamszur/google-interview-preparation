"""https://leetcode.com/problems/text-justification"""


def text_justification(words, max_width):
    """
    Time complexity: O(n)
    Space complexity: O(n)

    Args:
        words(List[str]): An array of strings words.
        max_width(int): Each line has exactly maxWidth characters.

    Returns:
        An array of justified text where each entry is a separate line.

    """
    lines = []
    width = 0
    line = []

    for word in words:
        if (len(word) + width + len(line)) <= max_width:
            width += len(word)
            line.append(word)
            continue

        if len(line) == 1:
            lines.append(
                "{0: <{width}}".format(" ".join(line), width=max_width)
            )
        else:
            space, extra = divmod(
                max_width - width,
                len(line) - 1
            )

            i = 0
            while extra > 0:
                line[i] += " "
                extra -= 1
                i += 1

            lines.append(
                (" " * space).join(line)
            )

        line = [word]
        width = len(word)

    lines.append(
        "{0: <{width}}".format(" ".join(line), width=max_width)
    )

    return lines
