from typing import Union
from collections import Counter

def split_most_common(
    values: Union[list, tuple],
    num_to_keep: int = 10,
    remainder: Union[str, int, float, None] = 'other'
) -> list:
    """
    Keep the x most common values and encode everything else as the provided remainder.

    Parameters
    ----------
    values : list or tuple
        A list or tuple of values.
    num_to_keep : int, default 10
        How many of the most frequent values to keep.
    remainder : str, int, float or None, default 'other'
        The value the remaing values will be replaced with.
    """
    counter = Counter(values).most_common(num_to_keep)
    most_common = [x[0] for x in counter]

    return [x if x in most_common else remainder for x in values]
