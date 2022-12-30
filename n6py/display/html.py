"""html module"""

# pylint: disable=too-few-public-methods
# pylint: disable=inconsistent-return-statements

from typing import List, Union

import re
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
            return f'<script src="{src}" defer></script>'

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
        template = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width,initial-scale=1.0">
                {self._styles}
                {self._scripts}
            </head>
            <body>
                {content if content else ''}
            </body>
            </html>
        """

        return re.sub(r"\n\s*", "", "".join(template))

    def display(self, content: Union[str, None] = None, raw: bool = False):
        """
        Displays provided HTML string.

        Parameters
        ----------
        content : str or None, default 'None'
            A string containing HTML markup.
        raw : bool, default 'False'
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
    load: Union[str, List[str], None] = None,
    raw: bool = False,
):
    """
    Displays provided HTML string. Can be used with multiple CSS and JS frameworks/libraries,
    by passing preset(s) for the `load` parameter, manually loading
    via `<link>` and `<script>` tags, or loading them as ESModules.

    Parameters
    ----------
    content : str or None, default 'None'
        A string containing HTML markup.
    load : str, list or None, default 'None'
        A string or list of string that define which libraries should be loaded.
    raw : bool, default 'False'
        A boolean that determines if the template should displayed or returned.

    Examples
    --------
    >>> content = "<h1>Hello World!</h1>"
    >>> html(content)
    <IPython.core.display.HTML object>

    >>> content = "<h1>Hello World!</h1>"
    >>> html(content, ['tailwind', 'alpine'])
    <IPython.core.display.HTML object>
    """
    if load:
        if not isinstance(load, str) and not isinstance(load, list):
            raise ValueError(
                "Provided 'load' parameter is neither a string nor a list of strings."
            )

        if isinstance(load, str):
            load = [load]

        missing = [x for x in load if x not in CDN]

        if missing:
            names = sorted(list(CDN.keys()))
            raise ValueError(f"Can't load {missing}. Possible values: {names}")

    css = [CDN[x]["css"] for x in load if "css" in CDN[x]] if load else None
    js = [CDN[x]["js"] for x in load if "js" in CDN[x]] if load else None

    doc = HTML(css, js)

    if raw:
        return doc.display(content, raw)

    doc.display(content, raw)
