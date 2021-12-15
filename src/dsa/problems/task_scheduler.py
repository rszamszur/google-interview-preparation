"""https://leetcode.com/problems/task-scheduler"""
from collections import Counter


def task_scheduler(tasks, n):
    """
    Time complexity: O(n)
    Space complexity: O(1)

    Args:
        tasks(List[str]): A characters array tasks, representing the tasks a
            CPU needs to do, where each letter represents a different task.
        n(int): A non-negative integer n that represents the cooldown period
            between two same tasks.

    Returns:
         The least number of units of times that the CPU will take to finish
         all the given tasks.

    """
    if n == 0:
        return len(tasks)

    orig_len = len(tasks)
    tasks = Counter(tasks)
    max_count = tasks.most_common(1)[0][1]
    max_count_times = 1

    for task, count in tasks.most_common()[1:]:
        if count != max_count:
            break

        max_count_times += 1

    units = (max_count - 1) * (n + 1) + max_count_times

    return max(units, orig_len)
