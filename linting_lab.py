"""Module containing a function to count occurrences of an item."""

def count_occurrences(sequence, item):
    """
    Count the number of occurrences of an item in a sequence.

    Args:
        sequence (Iterable): The sequence to search.
        item (Any): The item to count occurrences of.

    Returns:
        int: The number of occurrences of the item in the sequence.
    """
    count = 0
    for element in sequence:
        if element == item:
            count += 1
    return count
