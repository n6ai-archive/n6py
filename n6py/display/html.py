"""html module"""

from typing import Sequence, Union
from pathlib import Path

import re
from html import escape
from IPython.display import display as IPythondisplay
from IPython.core.display import HTML as IPythonHTML

# Latest CDN version links
PROVIDER = "https://unpkg.com/"

CDN = {
    "alpine": {"js": f"{PROVIDER}alpinejs@latest/cdn.min.js"},
    "animate": {"css": f"{PROVIDER}animate.css@latest/animate.min.css"},
    "animejs": {"js": f"{PROVIDER}animejs.css@latest/anime.min.js"},
    "bootstrap": {
        "css": f"{PROVIDER}bootstrap@latest/dist/css/bootstrap.min.css",
        "js": f"{PROVIDER}bootstrap@latest/dist/js/bootstrap.bundle.min.js",
    },
    "bulma": {"css": f"{PROVIDER}bulma@latest/css/bulma.min.css"},
    "halfmoon": {
        "css": f"{PROVIDER}halfmoon@latest/css/halfmoon-variables.min.css",
        "js": f"{PROVIDER}halfmoon@latest/js/halfmoon.min.js",
    },
    "minze": {"js": f"{PROVIDER}minze@latest"},
    "normalize": {"css": f"{PROVIDER}normalize.css@latest"},
    "tailwind": {"js": "https://cdn.tailwindcss.com"},
    "unocss": {
        "css": f"{PROVIDER}@unocss/reset@latest/tailwind.css",
        "js": f"{PROVIDER}@unocss/runtime@latest/mini.global.js",
    },
    "vue": {"js": f"{PROVIDER}vue@latest/dist/vue.global.js"},
}


class HTML:
    """
    HTML class that prepares an HTML document, by inserting
    provided HTML markup and including any CSS or JS file URLs.
    """

    def __init__(
        self,
        content: str,
        css: Union[str, Sequence[str], None] = None,
        js: Union[str, Sequence[str], None] = None,
    ):
        """
        Parameters
        ----------
        content : str
            A string containing HTML markup.
        css : str, Sequence or None, default 'None'
            A URL or a sequence of URLs to CSS files.
        js : str, Sequence or None, default 'None'
            A URL or a sequence of URLs to JavaScript files.

        Examples
        --------
        >>> doc = HTML("<h1>Hello World!</h1>")
        >>> doc.display()
        <IPython.core.display.HTML object>

        >>> doc = HTML("<h1>Hello World!</h1>", js="https://cdn.tailwindcss.com")
        >>> doc.display()
        <IPython.core.display.HTML object>
        """
        if not isinstance(content, str):
            raise TypeError("Provided 'content' parameter is not a string.")

        if not isinstance(css, (str, Sequence, type(None))):
            raise TypeError(
                "Provided 'css' parameter is neither a string, Sequence or None."
            )

        if not isinstance(js, (str, Sequence, type(None))):
            raise TypeError(
                "Provided 'js' parameter is neither a string, Sequence or None."
            )

        self.content = content
        self.css = [css] if isinstance(css, str) else css
        self.js = [js] if isinstance(js, str) else js

    @property
    def __styles(self):
        """HTML stylesheets link tags."""

        def template(href):
            return f'<link href="{href}" rel="stylesheet">'

        return "".join([template(href) for href in self.css]) if self.css else None

    @property
    def __scripts(self):
        """HTML script tags."""

        def template(src):
            return f'<script src="{src}"></script>'

        return "".join([template(src) for src in self.js]) if self.js else None

    @property
    def template(self):
        """HTML document template."""
        template = f"""
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width,initial-scale=1.0,shrink-to-fit=no">
                {self.__styles or ''}
                {self.__scripts or ''}
                <style>html, body {{background: transparent !important; overflow: hidden; padding: 0; margin: 0;}}</style>
            </head>
            <body>
                {self.content or ''}
            </body>
        </html>
        """

        return self.__minify(template)

    @property
    def __iframe(self):
        """HTML iframe template."""
        template = f"""
            <style>[data-mime-type="text/html"] {{padding-right: 0;}}</style>
            <iframe
                srcdoc="{escape(self.template)}"
                width="100%"
                height="0"
                fetchpriority="high"
                loading="eager"
                style="border: none;"
                onload="new ResizeObserver(() => {{
                    this.style.height = `${{this.contentDocument.body.scrollHeight}}px`
                }}).observe(this.contentDocument.body)"
            ></iframe>
        """

        return self.__minify(template)

    def __minify(self, template: str):
        """
        Minifies a given HTML template string.

        Parameters
        ----------
        template : str
            A string containing HTML markup.

        Returns
        -------
        str :
            A string containing minified HTML markup.
        """
        return re.sub(
            r"<!--(.*?)-->|(?=>)\s+|(?<!\w)\s+(?=<)|\s+$", "", "".join(template)
        )

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
        IPythondisplay(IPythonHTML(self.__iframe))

    def save(self, name: Union[str, Path]):
        """
        Saves the HTML template to an `.html` file with the provided name or path.

        Parameters
        ----------
        name : str
            Name or path of the file that will be written to disk.

        Examples
        --------
        >>> doc = HTML("<h1>Hello World!</h1>")
        >>> doc.save("file.html")
        """
        if not isinstance(name, (str, Path)):
            raise TypeError("Provided 'name' parameter is neither string or Path.")

        if isinstance(name, str):
            name = name if re.search(r"\.html$", name) else f"{name}.html"

        with open(name, "w", encoding="utf-8") as f:
            f.write(self.template)


def html(
    content: str,
    load: Union[str, Sequence[str], None] = None,
    raw: bool = False,
):
    """
    Displays provided HTML string. Can be used with multiple CSS and JS frameworks/libraries,
    by passing preset(s) for the `load` parameter, manually loading
    via `<link>` and `<script>` tags, or loading them as ESModules.

    Parameters
    ----------
    content : str
        A string containing HTML markup.
    load : str, Sequence or None, default 'None'
        A string or Sequence of strings that define which libraries should be loaded.
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
    if not isinstance(load, (str, Sequence, type(None))):
        raise TypeError(
            "Provided 'load' parameter is neither a string, Sequence or None."
        )

    load = [load] if isinstance(load, str) else load
    missing = [x for x in load if x not in CDN] if load else None

    if missing:
        names = sorted(list(CDN.keys()))
        raise ValueError(f"Can't load {missing}. Possible values: {names}")

    css = [CDN[x]["css"] for x in load if "css" in CDN[x]] if load else None
    js = [CDN[x]["js"] for x in load if "js" in CDN[x]] if load else None

    doc = HTML(content, css, js)
    return doc.template if raw else doc.display()
