# display

A module to display content in Jupyter Notebooks.

```py
from n6py import display
```

## html <Badge type="tip" text="0.1.16" />

Displays provided HTML string. Can be used with multiple CSS and JS frameworks/libraries, by passing preset(s) for the `load` parameter, manually loading via `<link>` and `<script>` tags, or loading them as ESModules.

- **path:** `n6py.display.html`
- **args:** `content`, `load`, `raw`

::: details load presets

The load parameter support the following frameworks/libraries out of the box:

- [alpine](https://alpinejs.dev/)
- [bootstrap](https://getbootstrap.com/)
- [tailwind](https://tailwindcss.com/)

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

::: warning
If you intend to display html multiple times with the same `load` parameter, then it's best to load the frameworks/libraries upfront only once.
:::

::: code-group

```py [HTML]
from n6py.display import html

content = """
<h1>Hello World!</h1>
"""

html(content)
```

```py [Custom]
from n6py.display import html

content = """
<h1>Hello World!</h1>
<script src="https://cdn.tailwindcss.com"></script>
"""

html(content)
```

```py [Multiple]
from n6py.display import html

html(laod=["tailwind", "alpine"])

content_1 = """
<h1 class="text-3xl text-indigo-500 font-bold">
  Hello World!
</h1>
"""

html(content_1)

content_2 = """
<h1 class="text-3xl text-indigo-500 font-bold">
  Hello World!
</h1>
"""

html(content_2)
```

```py [Alpine.js]
from n6py.display import html

# https://alpinejs.dev/
content = """
<div x-data="{ open: false }">
  <button @click="open = !open">Expand</button>

  <div x-show="open">
    Content...
  </div>
</div>
"""

html(content, "alpine")
```

```py [Bootstrap]
from n6py.display import html

# https://getbootstrap.com/
content = """
<div class="alert alert-primary" role="alert">
  A simple primary alert—check it out!
</div>
"""

html(content, "bootstrap")
```

```py [Tailwind CSS]
from n6py.display import html

# https://tailwindcss.com/
content = """
<h1 class="text-3xl text-indigo-500 font-bold">
  Hello World!
</h1>
"""

html(content, "tailwind")
```

```py [Vue.js]
from n6py.display import html

# https://vuejs.org/
content = """
<div id="app">{{ message }}</div>

<script type="module">
  import { createApp } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'

  createApp({
    data() {
      return {
        message: 'Hello Vue!'
      }
    }
  }).mount('#app')
</script>
"""

html(content)
```

```py [Result]
<IPython.core.display.HTML object>
```

:::
