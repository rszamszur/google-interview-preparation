"""https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm"""


class RollingHash:
    def __init__(self, string, size):
        self.str = string
        self.hash = 0

        for i in range(size):
            self.hash += ord(self.str[i])

        self.init = 0
        self.end = size

    def move_window(self):
        if self.end <= len(self.str) - 1:
            self.hash -= ord(self.str[self.init])
            self.hash += ord(self.str[self.end])
            self.init += 1
            self.end += 1

    def window_text(self):
        return self.str[self.init:self.end]


def karp_rabin(pattern, string):
    """Karp-Rabin algorithm implementation.

    Time complexity: O(s + p) where s is string, and p pattern
    Space complexity: O(s + p)

    Args:
        pattern(str): Pattern to find in provided string.
        string(str): String to search in.

    Returns:
        If found index in searched string, otherwise None.

    """
    if pattern == "" or string == "":
        return None
    if len(pattern) > len(string):
        return None

    rolling_hash = RollingHash(string, len(pattern))
    word_hash = RollingHash(pattern, len(pattern))

    for i in range(len(string) - len(pattern) + 1):
        if rolling_hash.hash == word_hash.hash:
            if rolling_hash.window_text() == pattern:
                return i

        rolling_hash.move_window()

    return None
