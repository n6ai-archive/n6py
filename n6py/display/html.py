"""html module"""

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
    HTML class that prepares an HTML document, by inserting
    provided HTML markup and including any CSS or JS file URLs.
    """

    def __init__(
        self,
        content: Union[str, None] = None,
        css: Union[str, List[str], None] = None,
        js: Union[str, List[str], None] = None,
    ):
        """
        Parameters
        ----------
        content : str or None, default 'None'
            A string containing HTML markup.
        css : str, list or None, default 'None'
            A URL or a list of URLs to CSS files.
        js : str, list or None, default 'None'
            A URL or a list of URLs to JavaScript files.

        Examples
        --------
        >>> doc = HTML("<h1>Hello World!</h1>")
        >>> doc.display()
        <IPython.core.display.HTML object>

        >>> doc = HTML("<h1>Hello World!</h1>", js="https://cdn.tailwindcss.com")
        >>> doc.display()
        <IPython.core.display.HTML object>
        """
        if not isinstance(content, (str, type(None))):
            raise TypeError(
                "Provided 'content' parameter is neither a string nor None."
            )

        if not isinstance(css, (str, list, type(None))):
            raise TypeError(
                "Provided 'css' parameter is neither a string, list or None."
            )

        if not isinstance(js, (str, list, type(None))):
            raise TypeError(
                "Provided 'js' parameter is neither a string, list or None."
            )

        self.content = content
        self.css = list(css) if isinstance(css, str) else css
        self.js = list(js) if isinstance(js, str) else js

    @property
    def styles(self):
        """HTML stylesheets link tags."""

        def template(href):
            return f'<link href="{href}" rel="stylesheet">'

        return "".join([template(href) for href in self.css]) if self.css else None

    @property
    def scripts(self):
        """HTML script tags."""

        def template(src):
            return f'<script src="{src}" defer></script>'

        return "".join([template(src) for src in self.js]) if self.js else None

    @property
    def template(self):
        """HTML document template."""
        template = f"""
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width,initial-scale=1.0">
                {self.styles or ''}
                {self.scripts or ''}
            </head>
            <body>
                {self.content or ''}
            </body>
        </html>
        """

        return re.sub(r"\n\s*", "", "".join(template))

    def display(self):
        """
        Displays HTML document.

        Examples
        --------
        >>> doc = HTML("<h1>Hello World!</h1>")
        >>> doc.display()
        <IPython.core.display.HTML object>

        >>> doc = HTML("<h1>Hello World!</h1>", js="https://cdn.tailwindcss.com")
        >>> doc.display()
        <IPython.core.display.HTML object>
        """
        IPythondisplay(IPythonHTML(self.template))


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

    Returns
    -------
    str, DisplayHandle or None :
        HTML document string, IPython display or None.

    Examples
    --------
    >>> content = "<h1>Hello World!</h1>"
    >>> html(content)
    <IPython.core.display.HTML object>

    >>> content = "<h1>Hello World!</h1>"
    >>> html(content, ['tailwind', 'alpine'])
    <IPython.core.display.HTML object>
    """
    if not isinstance(load, (str, list, type(None))):
        raise TypeError("Provided 'load' parameter is neither a string, list or None.")

    load = list(load) if isinstance(load, str) else load
    missing = [x for x in load if x not in CDN] if load else None

    if missing:
        names = sorted(list(CDN.keys()))
        raise ValueError(f"Can't load {missing}. Possible values: {names}")

    css = [CDN[x]["css"] for x in load if "css" in CDN[x]] if load else None
    js = [CDN[x]["js"] for x in load if "js" in CDN[x]] if load else None

    doc = HTML(content, css, js)
    return doc.template if raw else doc.display()
