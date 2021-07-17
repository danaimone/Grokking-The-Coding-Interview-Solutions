def remove_duplicates(arr):
    """
    Remove duplicates
    Given an array of sorted numbers, remove all duplicates from it using constant space (in-place).

    Notes:
        - Keep two pointers; one iterates through the array while the other keeps track of the next
        number that is non-duplicate.
        - While we move through the array, if the next number is not the same as the previous number,
        then it must be true that it is the next non-duplicate since we have a sorted array. Thus, that
        will be marked the current position of the next non-dupliocate. Otherwise, we'll continue our iteration
        through the array, keeping track of how many duplicates we've removed.
    :param arr: A sorted int array.
    :return: Length of the array with no duplicates.
    """
    assert len(arr) > 1
    next_non_duplicate = 1
    for i in range(1, len(arr)):
        previous_number = next_non_duplicate - 1
        if arr[previous_number] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1

    return next_non_duplicate

arr = [2, 3, 3, 3, 6, 9, 9]
print(remove_duplicates(arr))

arr = [2, 2, 2, 11]
print(remove_duplicates(arr))
