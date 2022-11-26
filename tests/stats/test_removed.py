"""removed unit test"""

import numpy as np
import pandas as pd

from n6py.stats import removed

data = [
    {"old": 3, "new": 2},
    {"old": [1, 2, 3], "new": [1, 2]},
    {"old": (1, 2, 3), "new": (1, 2)},
    {"old": {1, 2, 3}, "new": {1, 2}},
    {"old": {"1": 1, "2": 2, "3": 3}, "new": {"1": 1, "2": 2}},
    {"old": np.array([1, 2, 3]), "new": np.array([1, 2])},
    {"old": pd.Series([1, 2, 3]), "new": pd.Series([1, 2])},
    {"old": pd.DataFrame([1, 2, 3]), "new": pd.DataFrame([1, 2])},
]


def test_remove():
    """
    Should return an identical stat string for each entry in list.
    """
    for entry in data:
        returned_value = removed(entry["new"], entry["old"])
        assert returned_value == "Remaining: 2/3 | Removed: 1 - 33.33%"
