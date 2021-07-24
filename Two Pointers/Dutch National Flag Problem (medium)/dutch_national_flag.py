import unittest


class DutchNationalFlagTest(unittest.TestCase):
    def test_dutch_national_flag_problem(self):
        self.assertEqual(dutch_flag_sort([1, 0, 2, 1, 0]),
                         [0, 0, 1, 1, 2])
        self.assertEqual(dutch_flag_sort([2, 2, 0, 1, 2, 0]),
                         [0, 0, 1, 2, 2, 2])


def dutch_flag_sort(arr):
    """
    Given an array containing 0, 1s, and 2s,
    this function sorts an array in place.
    It works on the invariant condition that
    anything before low is 0, and anything after high is
    2 such that all 1s are between low and high.
    :param arr:
    """
    low, high = 0, len(arr) - 1
    i = 0
    while i <= high:
        if arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]
            i += 1
            low += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i], arr[high] = arr[high], arr[i]
            high -= 1

    return arr
