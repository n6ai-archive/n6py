"""n_changed module"""

from typing import Collection, Sequence, Union

import numpy as np
import pandas as pd
from numpy.typing import NDArray


def n_changed(
    prev: Union[int, Sequence, Collection, NDArray, pd.Series, pd.DataFrame],
    curr: Union[int, Sequence, Collection, NDArray, pd.Series, pd.DataFrame],
):
    """
    Returns a stats string about the difference between the previous and current values.

    Parameters
    ----------
    prev : int, Sequence, Collection, NDArray, pd.Series or pd.DataFrame
        Number of previous values or previous values.
    curr : int, Sequence, Collection, NDArray, pd.Series or pd.DataFrame
        Number of current values or current values.

    Returns
    -------
    str :
        A string of calculated stats.

    Examples
    --------
    >>> change = n_changed(100, 50)
    >>> print(change)
    Current: 50 - Previous: 100 | Change: 50 - 50.00%

    >>> change = n_changed([1, 2, 3, 4], [1, 2])
    >>> print(change)
    Current: 2 - Previous: 4 | Change: 2 - 50.00%
    """
    T = (Sequence, Collection, np.ndarray, pd.Series, pd.DataFrame)

    prev = len(prev) if isinstance(prev, T) else prev
    curr = len(curr) if isinstance(curr, T) else curr

    num = abs(curr - prev)
    percentage = num / prev * 100

    return f"Current: {curr} - Previous: {prev} | Change: {num} - {percentage:.2f}%"
