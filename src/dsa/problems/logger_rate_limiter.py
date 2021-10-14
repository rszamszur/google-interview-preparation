class Logger(object):
    __slots__ = ("_at")

    def __init__(self):
        self._at = {}

    def should_print_message(self, timestamp, message):
        """
        Time complexity: O(1)
        Space complexity: O(n)

        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if timestamp < self._at.get(message, 0):
            return False

        self._at[message] = timestamp + 10
        return True
