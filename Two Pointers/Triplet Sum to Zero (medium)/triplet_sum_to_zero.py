import unittest


class TripletTest(unittest.TestCase):
    def test_triplet_sum_to_zero(self):
        self.assertEqual(search_triplets([-3, 0, 1, 2, -1, 1, -2]),
                         [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]])

        self.assertEqual(search_triplets([-5, 2, -1, -2, 3]),
                         [[-5, 2, 3], [-2, -1, 3]])


def search_triplets(arr):
    arr.sort()
    triplets = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:  # skipping any duplicates that may occur
            continue
        search_pair(arr, -arr[i], i + 1, triplets)

    return triplets


def search_pair(arr: list, target_sum: int, left: int, triplets: list):
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:  # duplicate found
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1

        elif target_sum > current_sum:
            left += 1
        else:
            right -= 1
