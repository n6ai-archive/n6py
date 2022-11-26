"""split unit test"""

from n6py.encode import split

data = [
    {"old": [1, 2, 3], "keep": [1, 2]},
    {"old": (1, 2, 3), "keep": (1, 2)},
]


def test_split():
    """
    Should return the same type as input plus encode any values not provided in keep.
    """
    for entry in data:
        returned_value = split(entry["old"], entry["keep"], None)
        assert type(entry["old"]) is type(returned_value)
        assert returned_value[0] == 1 and returned_value[1] == 2
        assert returned_value[2] is None
