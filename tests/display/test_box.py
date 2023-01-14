"""box unit test"""

from n6py.display import Box, box

TEXT = "┌──────────────┐\n│ Hello World! │\n└──────────────┘"


def test_box_class():
    """
    Should match the previously defined text.
    """
    assert str(Box("Hello World!")) == TEXT


def test_box():
    """
    Should match the previously defined text.
    """
    assert str(box("Hello World!")) == TEXT
