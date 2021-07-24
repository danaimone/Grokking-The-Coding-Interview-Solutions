import unittest
from collections import deque

class SubarraysProductLessThanTargetTest(unittest.TestCase):
  def test_triplet_close_to_target(self):
    self.assertEqual(find_subarrays([2, 5, 3, 10], 30),
                     [[2], [5], [2, 5], [3], [5, 3], [10]])
    self.assertEqual(find_subarrays([8, 2, 6, 5], 50),
                     [[8], [2], [8, 2], [6], [2, 6], [5], [6, 5]])


def find_subarrays(arr, target):
  result = []
  product = 1
  left = 0
  for right in range(len(arr)):
    product *= arr[right]
    while (product >= target and left < len(arr)):
      product /= arr[left]
      left += 1
    temp_list = deque()
    for i in range(right, left-1, -1):
      temp_list.appendleft(arr[i])
      result.append(list(temp_list))
  return result

