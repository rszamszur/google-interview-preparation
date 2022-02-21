"""https://leetcode.com/problems/majority-element"""


def majority_element(nums):
    """
    Time complexity: O(n)
    Space complexity: O(1)

    If using collections.Counter class this could be solved with one line:
    return Counter(nums).most_common(1)[0][0]

    Args:
        nums(List[int]): Given array nums of size n.

    Returns:
        The majority element is the element that appears more than ⌊n / 2⌋
        times. You may assume that the majority element always exists in the
        array.

    """
    count = 1
    maj_el = nums[0]

    for num in nums[1:]:
        if count == 0:
            maj_el = num

        if num == maj_el:
            count += 1
        else:
            count -= 1

    return maj_el
