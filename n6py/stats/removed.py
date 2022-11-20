from typing import Union

def removed(
    new: Union[int, float, str, list, tuple],
    old: Union[int, float, str, list, tuple]
):
    """
    Returns a stats string about the difference between the old value and the new one.

    Parameters
    ----------
    new: int, float, str, list or tuple
        Number of new values or new values
    old: int, float, str, list or tuple
        Number of new values or new values

    Examples
    --------
    >>> rm_stat = removed(50, 100)
    >>> print(rm_stat)
    Removed: 50/100 - 50.00%

    >>> rm_stat = removed([1, 2], [1, 2, 3, 4])
    >>> print(rm_stat)
    Removed: 50/100 - 50.00%
    """
    is_type_numeric = type(new) in [int, float] and type(old) in [int, float]

    if (not is_type_numeric):
        new = len(new)
        old = len(old)

    removed = old - new
    removed_percentage = 100 / old * removed

    return f'Remaining: {new}/{old} | Removed: {removed} - {removed_percentage:.2f}%'
