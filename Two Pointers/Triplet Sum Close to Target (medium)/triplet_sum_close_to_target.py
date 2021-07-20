import math
import unittest


class TripletTargetTest(unittest.TestCase):
    def test_triplet_close_to_target(self):
        self.assertEqual(triplet_sum_close_to_target([-2, 0, 1, 2], 2), 1)
        self.assertEqual(triplet_sum_close_to_target([-3, -1, 1, 2], 1), 0)
        self.assertEqual(triplet_sum_close_to_target([1, 0, 1, 1], 100), 3)


def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    smallest_diff = math.inf
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            target_diff = target_sum - arr[i] - arr[left] - arr[right]
            if target_diff == 0:  # found a triplet with exact sum
                return target_sum - target_diff

            # the below covers the case that we have two solutions, so we pick the solution with
            # the smallest sum
            if abs(target_diff) < abs(smallest_diff) or (
                    abs(target_diff) == abs(smallest_diff) and target_diff > smallest_diff):
                smallest_diff = target_diff

            if target_diff > 0:
                left += 1 # need triplet with bigger sum
            else:
                right -= 1 # need triplet with smaller sum

    return target_sum - smallest_diff

