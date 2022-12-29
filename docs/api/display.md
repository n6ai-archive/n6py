# display

A module to display content in Jupyter Notebooks.

```py
from n6py import display
```

## html <Badge type="tip" text="0.1.16" />

Displays provided HTML string. Can be used with multiple CSS and JS libraries, by defining a preset for the `load` parameter or loading them as e.g. ESModules.

- **path:** `n6py.display.html`
- **args:** `content`, `load`, `raw`

::: details load presets

**Standalone**

- [alpine](https://alpinejs.dev/)
- [bootstrap](https://getbootstrap.com/)
- [tailwind](https://tailwindcss.com/)

**Combined**

- alpine-tailwind

:::

::: details type

```py
(function) html(
  content: str | None,
  load: Literal['alpine', 'alpine-tailwind', 'bootstrap', 'tailwind'] | None = None,
  raw: bool = False
) -> (str | None)
```

:::

::: warning
If you intend to display html multiple times with one preset, then it's best to load the preset upfront only once.
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

html(laod="tailwind")

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
