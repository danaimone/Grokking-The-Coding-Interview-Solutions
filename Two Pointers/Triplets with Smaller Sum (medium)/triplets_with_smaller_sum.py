import math
import unittest


class TripletSmallerSumTest(unittest.TestCase):
    def test_triplet_smaller_sum(self):
        self.assertEqual(triplet_with_smaller_sum([-1, 0, 2, 3], 3), 2)
        self.assertEqual(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5), 4)


def triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0
    for i in range(len(arr) - 2):
        count += search_pair(arr, target - arr[i], i)
    return count


def search_pair(arr, target, i):
    count = 0
    left, right = i + 1, len(arr) - 1
    while left < right:
        if arr[left] + arr[right] < target:
            # the count of pairs is anything in between the left and right, since
            # any number between must be less than the target at this point
            count += right - left
            left += 1
        else:
            right -= 1
    return count
