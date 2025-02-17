def cycle_reorder(lst):
    """
    cycle_reorder

    This method organizes a list by recognizing value cycles 
    and placing elements in their correct positions by cycling through them.

    Concept: The list can be broken into independent cycles, 
    each of which is sorted individually by rotating elements.


    Average-Time Complexity: O(N^2)
    Worst-Case Time Complexity: O(N^2)
    Best-Case Time Complexity: O(N^2)
    Space Complexity: O(1) (Sorts in-place)
    """
    size = len(lst)

    for start in range(size - 1):
        val = lst[start]
        target_idx = start

        # Determine the correct position for val
        for i in range(start + 1, size):
            if lst[i] < val:
                target_idx += 1

        # If already positioned correctly, move to the next one 
        if target_idx == start:
            continue

        # Skip duplicate values
        while val == lst[target_idx]:
            target_idx += 1
        lst[target_idx], val = val, lst[target_idx]

        # Continue rotating elements until the cycle is complete
        while target_idx != start:
            target_idx = start
            for i in range(start + 1, size):
                if lst[i] < val:
                    target_idx += 1

            while val == lst[target_idx]:
                target_idx += 1
            lst[target_idx], val = val, lst[target_idx]
        # End of cycle
    return lst
