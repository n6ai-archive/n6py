"""
Removed module
"""
from typing import Collection, Sequence, Union

import numpy as np
import pandas as pd
from numpy.typing import NDArray


def removed(
    new: Union[int, Sequence, Collection, NDArray, pd.Series, pd.DataFrame],
    old: Union[int, Sequence, Collection, NDArray, pd.Series, pd.DataFrame],
):
    """
    Return a stats string about the difference between the old value and the new one.

    Parameters
    ----------
    new : int, Sequence, Collection, NDArray, pd.Series or pd.DataFrame
        Number of new values or new values.
    old : int, Sequence, Collection, NDArray, pd.Series or pd.DataFrame
        Number of new values or new values.

    Returns
    -------
    str :
        A string of calculated stats.

    Examples
    --------
    >>> rm_stat = removed(50, 100)
    >>> print(rm_stat)
    Remaining: 50/100 | Removed: 50 - 50.00%

    >>> rm_stat = removed([1, 2], [1, 2, 3, 4])
    >>> print(rm_stat)
    Remaining: 2/4 | Removed: 2 - 50.00%
    """
    rm_old: int = 0
    rm_new: int = 0
    rm_num: int = 0
    rm_percentage: Union[int, float] = 0

    if isinstance(new, int) and isinstance(old, int):
        rm_old = old
        rm_new = new
        rm_num = rm_old - rm_new
        rm_percentage = 100 / old * rm_num
    elif isinstance(
        new, (Sequence, Collection, np.ndarray, pd.Series, pd.DataFrame)
    ) and isinstance(old, (Sequence, Collection, np.ndarray, pd.Series, pd.DataFrame)):
        rm_old = len(old)
        rm_new = len(new)
        rm_num = rm_old - rm_new
        rm_percentage = 100 / len(old) * rm_num

    return f"Remaining: {rm_new}/{rm_old} | Removed: {rm_num} - {rm_percentage:.2f}%"
