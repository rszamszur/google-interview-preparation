"""https://leetcode.com/problems/fibonacci-number"""


def fibonacci_recursive(n):
    """
    Use recursion to compute the Fibonacci number of a given integer.

    Time complexity: O(2^n)
    This is the slowest way to solve the Fibonacci Sequence because it takes
    exponential time. The amount of operations needed, for each level of
    recursion, grows exponentially as the depth approaches N.

    Space complexity: O(n)
    We need space proportional to N to account for the max size of the stack,
    in memory. This stack keeps track of the function calls to fib(N).
    This has the potential to be bad in cases that there isn't enough physical
    memory to handle the increasingly growing stack, leading to a
    StackOverflowError.

    Args:
        n: Nth Fibonacci number from the sequence.

    Returns:
        F(n)
    """
    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_bottom_up(n):
    """
    Iteratively compute and store the values, only returning once we reach the
    result.

    Time complexity: O(n)
    Each number, starting at 2 up to and including N, is visited, computed and
    then stored for O(1) access later on.

    Space complexity: O(n)
    The size of the data structure is proportional to N.

    Args:
        n: Nth Fibonacci number from the sequence.

    Returns:
        F(n)
    """
    if n <= 1:
        return n

    cache = [0] * (n + 1)
    cache[1] = 1
    for i in range(2, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2]

    return cache[n]


def fibonacci_top_up(n, cache={0: 0, 1: 1}):
    """
    Solve for all of the sub-problems, use memoization to store the pre-computed
    answers, then return the answer for N. We will leverage recursion, but in
    a smarter way by not repeating the work to calculate existing values.

    Time complexity: O(n)
    Each number, starting at 2 up to and including N, is visited, computed
    and then stored for O(1) access later on.

    Space complexity: O(n)
    The size of the data structure is proportional to N.

    Args:
        n: Nth Fibonacci number from the sequence.

    Returns:
        F(n)
    """
    if n <= 1:
        return cache[n]

    cache[n] = fibonacci_top_up(n - 1, cache) + fibonacci_top_up(n - 2, cache)
    return cache[n]


def fibonacci_iterative_bottom_up(n):
    """
    Modified bottom up approach to get rid of the need to use all of that space
    and instead use the minimum amount of space required.

    Time complexity: O(n)
    Each value from 2 to N is computed once. Thus, the time it takes to find
    the answer is directly proportional to N.

    Space complexity: O(1)
    This requires 1 unit of space for the integer N and 3 units of space to
    store the computed values (current, prev1, and prev2) for every loop
    iteration. The amount of space used is independent of N, so this approach
    uses a constant amount of space.

    Args:
        n: Nth Fibonacci number from the sequence.

    Returns:
        F(n)
    """
    if n <= 1:
        return n

    current = 0
    prev1 = 1
    prev2 = 0

    for x in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return current


def fibonacci_math(n):
    """
    Solution using golden ratio, a.k.a Binet's forumula:
    https://en.wikipedia.org/wiki/Fibonacci_number#Binet's_formula
    https://demonstrations.wolfram.com/GeneralizedFibonacciSequenceAndTheGoldenRatio/
    https://en.wikipedia.org/wiki/Golden_ratio#Relationship_to_Fibonacci_sequence

    Time complexity: O(log(n))
    Raising the golden_ratio to the power of N requires O(logN) time.

    Space complexity: O(1)
    The space used is for the variable to store the golden ratio.

    Args:
        n: Nth Fibonacci number from the sequence.

    Returns:
        F(n)
    """
    golden_ratio = (1 + (5 ** 0.5)) / 2
    return int(round((golden_ratio ** n) / (5 ** 0.5)))
