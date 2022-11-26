"""split_most_common unit test"""

from collections import Counter

from n6py.encode import split_most_common

data = [[1, 1, 1, 2, 2, 3], (1, 1, 1, 2, 2, 3)]


def test_split_most_common():
    """
    Should return the same type as input.
    Should keep only the two most common values and encode everything else as None.
    """
    for entry in data:
        returned_value = split_most_common(entry, 2, None)
        counter = Counter(returned_value)
        assert type(entry) is type(returned_value)
        assert counter[1] == 3
        assert counter[2] == 2
        assert counter[None] == 1