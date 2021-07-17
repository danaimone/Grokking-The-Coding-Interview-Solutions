import unittest

class TestMakeSquares(unittest.TestCase):
    def test_squares(self):
        self.assertEqual(make_squares([-2, -1, 0, 2, 3]), [0, 1, 4, 4, 9])
        self.assertEqual(make_squares([-3, -1, 0, 1, 2]), [0, 1, 1, 4, 9])

def make_squares(arr):
    n = len(arr)
    squares = [0 for _ in range(n)]
    highest_square_index = n - 1
    left, right = 0, n - 1

    while left <= right:
        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]
        if left_square > right_square:
            squares[highest_square_index] = left_square
            left += 1
        else:
            squares[highest_square_index] = right_square
            right -= 1
        highest_square_index -= 1

    return squares


if __name__ == '__main__':
    unittest.main()

