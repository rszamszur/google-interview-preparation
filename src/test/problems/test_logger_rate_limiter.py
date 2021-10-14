import pytest
from dsa.problems.logger_rate_limiter import Logger


logger = Logger()


@pytest.mark.parametrize("timestamp, message, expected", [
    (1, "foo", True),
    (2, "bar", True),
    (3, "foo", False),
    (8, "bar", False),
    (10, "foo", False),
    (11, "foo", True)
])
def test_logger_rate_limiter(timestamp, message, expected):
    assert logger.shouldPrintMessage(timestamp, message) == expected
