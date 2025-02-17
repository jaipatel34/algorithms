def cycle_sort(arr):
    """
    cycle_sort
    This is based on the idea that the permutations to be sorted
    can be decomposed into cycles, and the results can be individually sorted by cycling.

    Reference: https://en.wikipedia.org/wiki/Cycle_sort

    Average time complexity : O(N^2)
    Worst case time complexity : O(N^2)
    Space Complexity: O(1) (In-place sorting)
    """
    n = len(arr)

    # Finding cycles to rotate
    for cycle_start in range(n - 1):
        item = arr[cycle_start]

        # Find the correct position for item
        pos =cycle_start
        for i in range(cycle_start + 1, n):
            if arr[i] < item:
                pos += 1

        # If the item is already in the correct position, continue
        if pos == cycle_start:
            continue

        # Skip duplicate elements
        while item == arr[pos]:
            pos += 1
        arr[pos], item = item, arr[pos]

        # Rotate the cycle
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start+ 1, n):
                if arr[i] <item:
                    pos += 1

            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]

    return arr