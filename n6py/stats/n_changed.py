"""n_changed module"""

from typing import Collection, Sequence, Union

import numpy as np
import pandas as pd
from numpy.typing import NDArray


def n_changed(
    previous: Union[int, Sequence, Collection, NDArray, pd.Series, pd.DataFrame],
    current: Union[int, Sequence, Collection, NDArray, pd.Series, pd.DataFrame],
):
    """
    Return a stats string about the difference between the previous value and the current one.

    Parameters
    ----------
    previous : int, Sequence, Collection, NDArray, pd.Series or pd.DataFrame
        Number of previous values or previous values.
    current : int, Sequence, Collection, NDArray, pd.Series or pd.DataFrame
        Number of current values or current values.

    Returns
    -------
    str :
        A string of calculated stats.

    Examples
    --------
    >>> rm_stat = n_changed(100, 50)
    >>> print(rm_stat)
    Current: 50 - Previous: 100 | Change: 50 - 50.00%

    >>> rm_stat = n_changed([1, 2, 3, 4], [1, 2])
    >>> print(rm_stat)
    Current: 2 - Previous: 4 | Change: 2 - 50.00%
    """
    T = (Sequence, Collection, np.ndarray, pd.Series, pd.DataFrame)

    previous = len(previous) if isinstance(previous, T) else previous
    current = len(current) if isinstance(current, T) else current

    num = abs(current - previous)
    percentage = num / previous * 100

    return (
        f"Current: {current} - Previous: {previous} | Change: {num} - {percentage:.2f}%"
    )
