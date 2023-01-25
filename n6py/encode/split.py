"""split module"""

from typing import Union

import numpy as np
import pandas as pd
from numpy.typing import NDArray


def split(
    values: Union[list, tuple, NDArray, pd.Series],
    values_to_keep: Union[list, tuple, NDArray, pd.Series],
    remainder: Union[str, int, float, None] = "other",
) -> Union[list, tuple, NDArray, pd.Series]:
    """
    Keeps the provided values and encodes everything else as the provided remainder.

    Parameters
    ----------
    values: A list, tuple, numpy array or pandas series of values.
    values_to_keep: A list, tuple, numpy array or pandas series containing values to keep.
    remainder: The value the remaing values will be replaced with.

    Returns
    -------
    A processed list, tuple, numpy array or pandas series.

    Examples
    --------
    >>> x = [1, 2, 3, 4]
    >>> split(x, [1, 2])
    [1, 2, 'other', 'other']
    """
    splitted_values: Union[list, tuple, NDArray, pd.Series] = [
        x if x in list(values_to_keep) else remainder for x in list(values)
    ]

    if isinstance(values, tuple):
        splitted_values = tuple(splitted_values)

    elif isinstance(values, np.ndarray):
        splitted_values = np.array(splitted_values)

    elif isinstance(values, pd.Series):
        splitted_values = pd.Series(splitted_values)

    return splitted_values
