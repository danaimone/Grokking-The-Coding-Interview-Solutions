def pair_with_target_sum(arr, target_sum):
    """
    Pair with Target Sum

    Problem Statement:
        - Given an array of sorted numbers and a target sum, find a pair in the array whose sum is
          equal to the given target.

    Notes:
        - Using the two pointer method, we can make this algorithm run in O(n) time, since their will
        be n numbers visited in the worst case of no existing target_sum.
        - Our current sum starts at the front and end of the array, and based on how close we are to
        our target summer, we either decrement for smaller numbers, or increment for larger numbers.

    :param arr: A sorted array of ints
    :param target_sum: The target sum that two elements could add up to
    :return:
    """
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return [left, right]

        if current_sum > target_sum:
            right -= 1
        else:
            left += 1
    return [-1, -1]


arr, target = [1, 2, 3, 4, 6], 6
assert pair_with_target_sum(arr, target) == [1, 3]

arr, target = [2, 5, 9, 11], 11
assert pair_with_target_sum(arr, target) == [0, 2]
