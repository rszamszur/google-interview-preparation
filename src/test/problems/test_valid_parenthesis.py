import pytest
from dsa.problems.valid_parenthesis import valid_parenthesis


@pytest.mark.parametrize("string, expected", [
    ("{", False),
    ("{}", True),
    ("[]]", False),
    ("[]", True),
    ("()", True),
    ("()[]{}", True),
    ("()[]]{}", False),
    ("(((((((([[[[[[[[{{{{{{{{}}}}}}}}]]]]]]]]))))))))", True),
    ("(((((((([[[[[[[[{{{{{{{{}}}}}}}}]]]]]]]]))))))))}", False),
])
def test_valid_parenthesis(string, expected):
    assert valid_parenthesis(string) == expected
