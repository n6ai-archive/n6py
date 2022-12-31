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
- **methods:** `display()`

::: details type

```py
(class) HTML(
  content: str | None = None,
  css: str | List[str] | None = None,
  js: str | List[str] | None = None
)
```

:::

::: code-group

```py [Code]
from n6py.display import HTML

content = """
<h1>Hello World!</h1>
"""

doc = HTML(content, js="https://cdn.tailwindcss.com")
doc.display()
```

```py [Result]
<IPython.core.display.HTML object>
```

:::

## html <Badge type="tip" text="0.1.16" />

Displays provided HTML string. Can be used with multiple CSS and JS frameworks/libraries, by passing preset(s) for the `load` parameter, manually loading via `<link>` and `<script>` tags, or loading them as ESModules.

- **path:** `n6py.display.html`
- **args:** `content`, `load`, `raw`

::: details load presets

The load parameter supports the following frameworks/libraries out of the box:

**CSS**

- [bootstrap](https://getbootstrap.com/)
- [bulma](https://bulma.io/)
- [normalize](https://necolas.github.io/normalize.css/)
- [tailwind](https://tailwindcss.com/)

**JavaScript**

- [alpine](https://alpinejs.dev/)
- [minze](https://minze.dev/)
- [vue](https://vuejs.org/)

:::

::: details type

```py
(function) html(
  content: str | None = None,
  load: str | List[str] | None = None,
  raw: bool = False
) -> (str | None)
```

:::

::: code-group

```py [HTML]
from n6py.display import html

html("<h1>Hello World!</h1>")
```

```py [Custom]
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
