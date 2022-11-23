"""
split module
"""
from typing import Union


def split(
    values: Union[list, tuple],
    values_to_keep: Union[list, tuple],
    remainder: Union[str, int, float, None] = "other",
) -> Union[list, tuple]:
    """
    Keep the provided values and encode everything else as the provided remainder.

    Parameters
    ----------
    values : list or tuple
        A list or tuple of values.
    values_to_keep : list or tuple
        A list or tuple containing values to keep.
    remainder : str, int, float or None, default 'other'
        The value the remaing values will be replaced with.

    Returns
    -------
    list, tuple :
        A processed list or tuple.

    Examples
    --------
    >>> x = [1, 2, 3, 4]
    >>> split(x, [1, 2])
    [1, 2, "other", "other"]
    """
    splitted_values: Union[list, tuple] = [
        x if x in values_to_keep else remainder for x in values
    ]

    if isinstance(values, tuple):
        splitted_values = tuple(splitted_values)

    return splitted_values
