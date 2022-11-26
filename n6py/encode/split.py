"""
split module
"""
from typing import Union

import numpy as np
from numpy.typing import NDArray


def split(
    values: Union[list, tuple, NDArray],
    values_to_keep: Union[list, tuple, NDArray],
    remainder: Union[str, int, float, None] = "other",
) -> Union[list, tuple, NDArray]:
    """
    Keep the provided values and encode everything else as the provided remainder.

    Parameters
    ----------
    values : list, tuple or NDArray
        A list, tuple or numpy array of values.
    values_to_keep : list, tuple or NDArray
        A list, tuple or numpy array containing values to keep.
    remainder : str, int, float or None, default 'other'
        The value the remaing values will be replaced with.

    Returns
    -------
    list, tuple, NDArray :
        A processed list, tuple or numpy array.

    Examples
    --------
    >>> x = [1, 2, 3, 4]
    >>> split(x, [1, 2])
    [1, 2, 'other', 'other']
    """
    splitted_values: Union[list, tuple, NDArray] = [
        x if x in values_to_keep else remainder for x in values
    ]

    if isinstance(values, tuple):
        splitted_values = tuple(splitted_values)

    elif isinstance(values, np.ndarray):
        splitted_values = np.array(splitted_values)

    return splitted_values
