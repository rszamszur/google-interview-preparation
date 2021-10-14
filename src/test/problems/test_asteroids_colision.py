import pytest
from dsa.problems.asteroids_collision import Solution


solution = Solution()


@pytest.mark.parametrize("asteroids, expected", [
    ([8, -8], []),
    ([5,10,-5], [5,10]),
    ([10,2,-5], [10]),
    ([-2,-1,1,2], [-2,-1,1,2]),
    ([2,1,-1,-2], []),
    ([2, 10, 8, -8], [2, 10]),
    ([50, 2, 3, 4, 6, 7, - 5, -10], [50]),
])
def test_asteroids_collision(asteroids, expected):
    assert solution.asteroid_collision(asteroids) == expected
