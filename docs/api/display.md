# display

A module to display content in Jupyter Notebooks.

```py
from n6py import display
```

## HTML <Badge type="tip" text="0.1.20" />

HTML class that prepares an HTML document, by inserting provided HTML markup and including any CSS or JavaScript file URLs.

- **path:** `n6py.display.HTML`
- **args:** `content`, `css`, `js`
- **properties:** `.template`
- **methods:** `.display()`, `.save()`

::: details type

```py
(class) HTML(
  content: str,
  css: str | Sequence[str] | None = None,
  js: str | Sequence[str] | None = None
)
```

:::

::: code-group

```py [Code]
from n6py.display import HTML

content = """
<h1>Hello World!</h1>
"""

doc = HTML(content, js="https://cdn.tailwindcss.com/3.2.4")
doc.display()
```

```py [Custom]
from n6py.display import HTML

def html(content):
  url = {
    "css": ["https://unpkg.com/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"],
    "js": ["https://unpkg.com/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"]
  }

  doc = HTML(content, url["css"], url["js"])
  doc.display()

content = """
<div class="alert alert-primary" role="alert">
  A simple primary alert—check it out!
</div>
"""

html(content)
```

```py [Save]
from n6py.display import HTML

content = """
<h1>Hello World!</h1>
"""

doc = HTML(content)
doc.save("file.html")
```

```py [Result]
<IPython.core.display.HTML object>
```

:::

## html <Badge type="tip" text="0.1.16" />

Displays provided HTML string. Can be used with multiple CSS and JavaScript frameworks/libraries, by passing preset(s) for the `load` parameter, manually loading via `<link>` and `<script>` tags, or loading them as ESModules.

- **path:** `n6py.display.html`
- **args:** `content`, `load`, `raw`

::: details load presets

The load parameter supports the following frameworks/libraries out of the box:

| Preset                                                | Language | Function           |
| :---------------------------------------------------- | :------- | :----------------- |
| [alpine](https://alpinejs.dev/)                       | JS       | layout             |
| [animate](https://animate.style/)                     | CSS      | animation          |
| [animejs](https://animejs.com/)                       | JS       | animation          |
| [bootstrap](https://getbootstrap.com/)                | CSS      | layout, components |
| [bulma](https://bulma.io/)                            | CSS      | layout             |
| [halfmoon](https://www.gethalfmoon.com/)              | CSS      | layout, components |
| [minze](https://minze.dev/)                           | JS       | web components     |
| [normalize](https://necolas.github.io/normalize.css/) | CSS      | layout, reset      |
| [tailwind](https://tailwindcss.com/)                  | CSS      | layout, utilies    |
| [vue](https://vuejs.org/)                             | JS       | layout, components |

:::

::: details type

```py
(function) html(
  content: str,
  load: str | Sequence[str] | None = None,
  raw: bool = False
) -> (str | None)
```

:::

::: warning
The `html` function always loads the latest version of the available presets via a CDN. In production, it's better to pin the CSS and JavaScript files to a specific version as demonstrated in the HTML class code examples.
:::

::: code-group

```py [Code]
from n6py.display import html

html("<h1>Hello World!</h1>")
```

```py [Presets]
from n6py.display import html

content = """
<h1 class="text-3xl text-indigo-500 font-bold">
  Hello World!
</h1>
"""

html(content, "tailwind")
```

```py [Result]
<IPython.core.display.HTML object>
```

:::
