"""num_changed unit test"""

import numpy as np
import pandas as pd

from n6py.stats import num_changed

data = [
    {"amount_1": 3, "amount_2": 2},
    {"amount_1": [1, 2, 3], "amount_2": [1, 2]},
    {"amount_1": (1, 2, 3), "amount_2": (1, 2)},
    {"amount_1": {1, 2, 3}, "amount_2": {1, 2}},
    {"amount_1": {"1": 1, "2": 2, "3": 3}, "amount_2": {"1": 1, "2": 2}},
    {"amount_1": np.array([1, 2, 3]), "amount_2": np.array([1, 2])},
    {"amount_1": pd.Series([1, 2, 3]), "amount_2": pd.Series([1, 2])},
    {"amount_1": pd.DataFrame([1, 2, 3]), "amount_2": pd.DataFrame([1, 2])},
]


def test_num_changed_removed():
    """
    Should return an identical stat string for each entry in list.
    """
    for entry in data:
        returned_value = num_changed(entry["amount_1"], entry["amount_2"])
        assert returned_value == "Current: 2 - Previous: 3 | Change: 1 - 33.33%"


def test_num_changed_added():
    """
    Should return an identical stat string for each entry in list.
    """
    for entry in data:
        returned_value = num_changed(entry["amount_2"], entry["amount_1"])
        assert returned_value == "Current: 3 - Previous: 2 | Change: 1 - 50.00%"


def test_num_changed_equal():
    """
    Should return an identical stat string for each entry in list.
    """
    for entry in data:
        returned_value = num_changed(entry["amount_1"], entry["amount_1"])
        assert returned_value == "Current: 3 - Previous: 3 | Change: 0 - 0.00%"
