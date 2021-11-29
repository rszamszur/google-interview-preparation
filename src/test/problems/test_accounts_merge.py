import pytest
from dsa.problems.accounts_merge import accounts_merge


@pytest.mark.parametrize("accounts, expected", [
    (
        [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]],
        [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]],
    ),
    (
        [["David","Avid0@m.co","David0@m.co","David1@m.co"],["David","Gvid3@m.co","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]],
        [["David","Avid0@m.co","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co","Gvid3@m.co"]]
    )
])
def test_accounts_merge(accounts, expected):
    assert accounts_merge(accounts) == expected