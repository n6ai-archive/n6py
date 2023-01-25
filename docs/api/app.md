# app

A module to create app wrappers around code bases and git repos.

```py
from n6py import app
```

## GitApp <Badge type="tip" text="0.1.30" />

A class that provides a unified API for wrapping and enhancing git repositories with commands for easy usage on Linux systems.

- **path:** `n6py.app.GitApp`
- **args:** `url`, `app_script`, `input_dir`, `output_dir`
- **properties**: `.name`, `.dir`, `.app_script_path`
- **methods:** `.install()`, `.uninstall()`, `.run()`

::: details type

```py
(class) GitApp(
  url: str | None,
  app_script: str | Path | None,
  input_dir: str | Path | None = None,
  output_dir: str | Path | None = None
)
```

:::

::: code-group

```py [Code]
from n6py.app import GitApp

app = GitApp(
  url="https://github.com/<USER>/<REPO>",
  app_script="app.py",
  input_dir="/content/input",
  output_dir="/content/output"
)

app.install()
app.run("--example-flag")
```

```py [Result]
Success ✨
```

:::
