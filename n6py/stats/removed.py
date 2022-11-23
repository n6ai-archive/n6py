"""
Removed module
"""
from typing import Collection, Sequence, Union


def removed(
    new: Union[Union[int, float], Sequence, Collection],
    old: Union[Union[int, float], Sequence, Collection],
):
    """
    Return a stats string about the difference between the old value and the new one.

    Parameters
    ----------
    new : int, float, Sequence or Collection
        Number of new values or new values.
    old : int, float, Sequence or Collection
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
    \u200B
    >>> rm_stat = removed([1, 2], [1, 2, 3, 4])
    >>> print(rm_stat)
    Remaining: 2/4 | Removed: 2 - 50.00%
    """
    rm_num: Union[int, float] = 0
    rm_percentage: Union[int, float] = 0

    if isinstance(new, (int, float)) and isinstance(old, (int, float)):
        rm_num = old - new
        rm_percentage = 100 / old * rm_num
    elif isinstance(new, (Sequence, Collection)) and isinstance(
        old, (Sequence, Collection)
    ):
        rm_num = len(old) - len(new)
        rm_percentage = 100 / len(old) * rm_num

    return f"Remaining: {new}/{old} | Removed: {rm_num} - {rm_percentage:.2f}%"
