"""split unit test"""

import numpy as np
import pandas as pd

from n6py.encode import split

data = [
    {"old": [1, 2, 3], "keep": [1, 2]},
    {"old": (1, 2, 3), "keep": (1, 2)},
    {"old": np.array([1, 2, 3]), "keep": np.array([1, 2])},
    {"old": pd.Series([1, 2, 3]), "keep": pd.Series([1, 2])},
]


def test_split():
    """
    Should return the same type as input plus encode any values not provided in keep as 0.
    """
    for entry in data:
        returned_value = split(entry["old"], entry["keep"], 0)
        assert type(entry["old"]) is type(returned_value)
        assert returned_value[0] == 1 and returned_value[1] == 2
        assert returned_value[2] == 0
