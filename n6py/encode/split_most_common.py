"""
split_most_common module
"""
from collections import Counter
from typing import Union


def split_most_common(
    values: Union[list, tuple],
    num_to_keep: int = 10,
    remainder: Union[str, int, float, None] = "other",
) -> Union[list, tuple]:
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

    Returns
    -------
    list, tuple :
        A processed list or tuple.

    Examples
    --------
    >>> x = [1, 1, 1, 2, 2, 3, 4]
    >>> split(x, 2)
    [1, 1, 1, 2, 2, "other", "other"]
    """
    counter = Counter(values).most_common(num_to_keep)
    most_common = [x[0] for x in counter]

    splitted_values: Union[list, tuple] = [
        x if x in most_common else remainder for x in values
    ]

    if isinstance(values, tuple):
        splitted_values = tuple(splitted_values)

    return splitted_values
