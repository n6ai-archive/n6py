# display

A module to display content in Jupyter Notebooks.

```py
from n6py import display
```

## display_html <Badge type="tip" text="0.1.16" />

Displays provided HTML string. Can be used with multiple CSS and JS libraries, by defining a preset or loading them as ESModules.

- **path:** `n6py.display.display_html`
- **args:** `content`, `preset`, `raw`

::: details presets

**Standalone**

- [alpine](https://alpinejs.dev/)
- [bootstrap](https://getbootstrap.com/)
- [tailwind](https://tailwindcss.com/)

**Combined**

- alpine-tailwind

:::

::: details type

```py
(function) display_html(
  content: str,
  preset: Literal['alpine', 'alpine-tailwind', 'bootstrap', 'tailwind'] | None = None,
  raw: bool = False
) -> (str | None)
```

:::

::: code-group

```py [HTML]
from n6py.display import display_html

content = """
<h1>Hello World!</h1>
"""

display_html(content)
```

```py [Custom]
from n6py.display import display_html

content = """
<h1>Hello World!</h1>
<script src="https://cdn.tailwindcss.com"></script>
"""

display_html(content)
```

```py [Alpine.js]
from n6py.display import display_html

# https://alpinejs.dev/
content = """
<div x-data="{ open: false }">
  <button @click="open = !open">Expand</button>

  <div x-show="open">
    Content...
  </div>
</div>
"""

display_html(content, "alpine")
```

```py [Bootstrap]
from n6py.display import display_html

# https://getbootstrap.com/
content = """
<div class="alert alert-primary" role="alert">
  A simple primary alert—check it out!
</div>
"""

display_html(content, "bootstrap")
```

```py [Tailwind CSS]
from n6py.display import display_html

# https://tailwindcss.com/
content = """
<h1 class="text-3xl text-indigo-500 font-bold">
  Hello World!
</h1>
"""

display_html(content, "tailwind")
```

```py [Vue.js]
from n6py.display import display_html

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

display_html(content)
```

```py [Result]
<IPython.core.display.HTML object>
```

:::
