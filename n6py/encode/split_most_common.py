"""split_most_common module"""

from collections import Counter
from typing import Union

import numpy as np
import pandas as pd
from numpy.typing import NDArray


def split_most_common(
    values: Union[list, tuple, NDArray, pd.Series],
    num_to_keep: int = 10,
    remainder: Union[str, int, float, None] = "other",
) -> Union[list, tuple, NDArray, pd.Series]:
    """
    Keeps the x most common values and encodes everything else as the provided remainder.

    Parameters
    ----------
    values : list, tuple, NDArray or pd.Series
        A list, tuple, NDArray or pd.Series of values.
    num_to_keep : int, default 10
        How many of the most frequent values to keep.
    remainder : str, int, float or None, default 'other'
        The value the remaing values will be replaced with.

    Returns
    -------
    list, tuple, NDArray, pd.Series :
        A processed list, tuple, NDArray or pd.Series.

    Examples
    --------
    >>> x = [1, 1, 1, 2, 2, 3, 4]
    >>> split_most_common(x, 2)
    [1, 1, 1, 2, 2, 'other', 'other']
    """
    counter = Counter(values).most_common(num_to_keep)
    most_common = [x[0] for x in counter]

    splitted_values: Union[list, tuple, NDArray, pd.Series] = [
        x if x in most_common else remainder for x in list(values)
    ]

    if isinstance(values, tuple):
        splitted_values = tuple(splitted_values)

    elif isinstance(values, np.ndarray):
        splitted_values = np.array(splitted_values)

    elif isinstance(values, pd.Series):
        splitted_values = pd.Series(splitted_values)

    return splitted_values
