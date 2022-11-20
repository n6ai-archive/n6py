from typing import Union

def split(
  values: Union[list, tuple],
  values_to_keep: Union[list, tuple],
  remainder: Union[str, int, float, None] = 'other'
) -> list:
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
    """
    return [x if x in values_to_keep else remainder for x in values]
