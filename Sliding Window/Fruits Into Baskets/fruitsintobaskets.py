def fruits_into_baskets(fruits):
    """
    Fruits Into Baskets

    Problem Statement:
        Given two baskets, put a maximum number of fruits in each basket. Each basket can only have one
        type of fruit.

        You can't skip a tree once you have started. You will pick one fruit from each tree until you
        cannot, i.e. you will stop when you have to pick from a third fruit type.

    Notes:
        - Keep window end moving while there is only two unique fruits.
        - Similar to how we find k distinct characters, except we aren't given k.
        - We can use a hashmap to keep track of the frequency of a given fruit.
        - As we move through the array, we'll create a sliding window out of the fruit we add.
        - If we ever have more than 2 distinct fruit in our sliding window, we'll shrink the window
        until we have 2 distinct fruits in our hashmap.
        - We'll keep track of the maximum size of this window, as that represents the max amount of
        fruits we can have in two baskets given our constraints.

    Time Complexity:
        - O(N), since we only look at a maximum of N fruit in our for loop, and the while loop
        will only process each fruit once.

    Space Complexity:
        - O(1), since we store at max 3 different fruits in the hashmap

    :param fruits: A list of chars representing a fruit
    :return: The maximum amount of fruits that can be placed in both baskets.
    """
    window_start = 0
    max_fruits = 0
    fruit_frequency = {}
    k = 2

    for window_end in range(len(fruits)):
        right_char = fruits[window_end]
        if right_char not in fruit_frequency:
            fruit_frequency[right_char] = 0
        fruit_frequency[right_char] += 1

        while len(fruit_frequency) > k:
            left_char = fruits[window_start]
            fruit_frequency[left_char] -= 1
            if fruit_frequency[left_char] == 0:
                del fruit_frequency[left_char]
            window_start += 1

        max_fruits = max(max_fruits, window_end - window_start + 1)
    return max_fruits

fruits = ['A', 'B', 'C', 'A', 'C']
print(fruits_into_baskets(fruits))

fruits = ['A', 'B', 'C', 'B', 'B', 'C']
print(fruits_into_baskets(fruits))
