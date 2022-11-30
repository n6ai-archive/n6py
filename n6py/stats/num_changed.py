"""num_changed module"""

from typing import Collection, Sequence, Union

import numpy as np
import pandas as pd
from numpy.typing import NDArray


def num_changed(
    previous: Union[int, Sequence, Collection, NDArray, pd.Series, pd.DataFrame],
    current: Union[int, Sequence, Collection, NDArray, pd.Series, pd.DataFrame],
):
    """
    Return a stats string about the difference between the old value and the new one.

    Parameters
    ----------
    previous : int, Sequence, Collection, NDArray, pd.Series or pd.DataFrame
        Number of new values or new values.
    current : int, Sequence, Collection, NDArray, pd.Series or pd.DataFrame
        Number of new values or new values.

    Returns
    -------
    str :
        A string of calculated stats.

    Examples
    --------
    >>> rm_stat = num_changed(100, 50)
    >>> print(rm_stat)
    Current: 50 - Previous: 100 | Change: 50 - 50.00%

    >>> rm_stat = num_changed([1, 2, 3, 4], [1, 2])
    >>> print(rm_stat)
    Current: 2 - Previous: 4 | Change: 2 - 50.00%
    """
    T = (Sequence, Collection, np.ndarray, pd.Series, pd.DataFrame)

    c_previous = len(previous) if isinstance(previous, T) else previous
    c_current = len(current) if isinstance(current, T) else current

    c_num = abs(c_current - c_previous)
    c_percentage = c_num / c_previous * 100

    return f"Current: {c_current} - Previous: {c_previous} | Change: {c_num} - {c_percentage:.2f}%"
