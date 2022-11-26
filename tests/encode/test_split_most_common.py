"""split_most_common unit test"""

from collections import Counter

import numpy as np
import pandas as pd

from n6py.encode import split_most_common

data = [
    [1, 1, 1, 2, 2, 3],
    (1, 1, 1, 2, 2, 3),
    np.array([1, 1, 1, 2, 2, 3]),
    pd.Series([1, 1, 1, 2, 2, 3]),
]


def test_split_most_common():
    """
    Should return the same type as input.
    Should keep only the two most common values and encode everything else as 0.
    """
    for entry in data:
        returned_value = split_most_common(entry, 2, 0)
        counter = Counter(returned_value)
        assert type(entry) is type(returned_value)
        assert counter[1] == 3
        assert counter[2] == 2
        assert counter[0] == 1
