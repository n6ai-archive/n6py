"""box module"""

# pylint: disable=too-few-public-methods

from typing import Iterable

# fmt: off
default_lines = ("┌", "─", "┐",
                 "│",      "│",
                 "└", "─", "┘")
# fmt: on


class Box:
    """
    A class that builds a string representation of a box
    around the provided content.
    """

    def __init__(self, content: str, lines: Iterable[str] = default_lines):
        """
        Parameters
        ----------
        content : str
            A text string.
        lines : List
            A tuple of symbols representing the edges of a box.

        Examples
        --------
        >>> lines = ("┌", "─", "┐",
        ...          "│",      "│",
        ...          "└", "─", "┘")
        >>> box = Box("Hello World!", lines)
        >>> print(box)
        ┌──────────────┐
        │ Hello World! │
        └──────────────┘
        """
        self.content = content
        self.lines = lines

    def __str__(self):
        return self._layout

    @property
    def _layout(self):
        """
        The box reprsentation of the provided content string.
        """
        content = f" {self.content} "
        # pylint: disable=invalid-name
        tl, t, tr, l, r, bl, b, br = self.lines

        def line(x):
            return "".join([x for _ in range(len(content))])

        t = line(t)
        b = line(b)
        # pylint: enable=invalid-name

        top = f"{tl}{t}{tr}"
        middle = f"{l}{content}{r}"
        bottom = f"{bl}{b}{br}"

        return f"{top}\n{middle}\n{bottom}"


def box(content: str):
    """
    Returns the provided content as a stylized box string.

    Parameters
    ----------
    content : str
        A text string.

    Returns
    -------
    str :
        Stylized boxed string.

    Examples
    --------
    >>> print(box("Hello World!"))
    ┌──────────────┐
    │ Hello World! │
    └──────────────┘
    """
    return Box(content)
