"""html module"""

# pylint: disable=too-few-public-methods
# pylint: disable=inconsistent-return-statements

from typing import Literal, List, Union

from IPython.display import display as IPythondisplay
from IPython.core.display import HTML as IPythonHTML

# Latest CDN version links
CDN = {
    "alpine": {"js": "https://unpkg.com/alpinejs@latest/dist/cdn.min.js"},
    "bootstrap": {
        "css": "https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/css/bootstrap.min.css",
        "js": "https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/js/bootstrap.bundle.min.js",
    },
    "tailwind": {"js": "https://cdn.tailwindcss.com"},
}

# Custom presets
PRESETS = {
    "alpine": {"js": [CDN["alpine"]["js"]]},
    "alpine-tailwind": {"js": [CDN["alpine"]["js"], CDN["tailwind"]["js"]]},
    "bootstrap": {"css": [CDN["bootstrap"]["css"]], "js": [CDN["bootstrap"]["js"]]},
    "tailwind": {"js": [CDN["tailwind"]["js"]]},
}


class HTML:
    """
    HTML class that prepares the HTML document to be displayed,
    by inserting provided HTML content, and loading any CSS or JS files.
    """

    def __init__(
        self,
        css: Union[str, List[str], None] = None,
        js: Union[str, List[str], None] = None,
    ):
        """
        Parameters
        ----------
        css : str, list or None, default 'None'
            A URL or a list of URLs to CSS files.
        js : str, list or None, default 'None'
            A URL or a list of URLs to JavaScript files.
        """
        self.css = css
        self.js = js

    @property
    def _styles(self):
        """Creates HTML link tags for stylesheets."""

        def template(href):
            return f'<link href="{href}" rel="stylesheet">'

        result = ""

        if isinstance(self.css, list):
            result = [template(href) for href in self.css]
            result = "".join(result)
        elif isinstance(self.css, str):
            result = template(self.css)

        return result

    @property
    def _scripts(self):
        """Creates HTML script tags."""

        def template(src):
            return f'<script src="{src}" defer crossorigin></script>'

        result = ""

        if isinstance(self.js, list):
            result = [template(src) for src in self.js]
            result = "".join(result)
        elif isinstance(self.js, str):
            result = template(self.js)

        return result

    def _template(self, content):
        """
        Creates the HTML document string to display.

        Parameters
        ----------
        content : str
            A string containing HTML markup.

        Returns
        -------
        str :
            HTML document string.
        """
        viewport = (
            '<meta name="viewport" content="width=device-width,initial-scale=1.0">'
        )
        head = f'<head><meta charset="UTF-8">{viewport}{self._styles}{self._scripts}</head>'
        body = f"<body>{content if content else ''}</body>"

        return f'<!DOCTYPE html><html lang="en">{head}{body}</html>'

    def display(self, content: Union[str, None] = None, raw: bool = False):
        """
        Displays provided HTML string.

        Parameters
        ----------
        content : str or None, default 'None'
            A string containing HTML markup.
        raw: bool, default 'False'
            A boolean that determines if the template should displayed or returned.

        Examples
        --------
        >>> html = HTML()
        >>> content = "<h1>Hello World!</h1>"
        >>> html.display(content)
        <IPython.core.display.HTML object>
        """
        template = self._template(content)

        if raw:
            return template

        IPythondisplay(IPythonHTML(template))


def html(
    content: Union[str, None] = None,
    load: Union[
        Literal[
            "alpine",
            "alpine-tailwind",
            "bootstrap",
            "tailwind",
        ],
        None,
    ] = None,
    raw: bool = False,
):
    """
    Displays provided HTML string. Can be used with multiple CSS and JS libraries,
    by defining a preset for the `load` parameter or loading them e.g. as ESModules.

    Parameters
    ----------
    content : str or None, default 'None'
        A string containing HTML markup.
    load : str or None, default 'None'
        A preset name that defines which libraries should be loaded.
    raw: bool, default 'False'
        A boolean that determines if the template should displayed or returned.

    Examples
    --------
    >>> content = "<h1>Hello World!</h1>"
    >>> html(content)
    <IPython.core.display.HTML object>
    """
    preset = load

    if preset and preset not in PRESETS:
        preset_names = ", ".join(sorted(list(PRESETS.keys())))
        raise ValueError(
            f"Preset with the name '{preset}' does not exist.\nAvailable presets: {preset_names}"
        )

    css = PRESETS[preset]["css"] if preset and "css" in PRESETS[preset] else None
    js = PRESETS[preset]["js"] if preset and "js" in PRESETS[preset] else None

    doc = HTML(css=css, js=js)

    if raw:
        return doc.display(content, raw=raw)

    doc.display(content, raw=raw)
