# n6py Contributing Guide

## Development

### Cloud

Get started on a remote machine.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=568493639)

### Local

Get started on a local machine.

<details>
<summary>Steps</summary>

#### Prerequisites

- [Python v3+](https://www.python.org/downloads/)
- [Node.js v16+](https://nodejs.dev/)
- [Poetry](https://python-poetry.org/)

Set the following environment variables for Poetry:

```sh
poetry config virtualenvs.in-project true
```

#### Installing

Install all dependencies and create a `venv` with Poetry. Additionaly add pre-commit hooks.

```sh
poetry install
poetry run pre-commit install
```

```sh
npm install
```

</details>

### Use venv

> The `venv` is automatically activated in `VS Code` when opening a new terminal window. You don't need to run the poetry shell command manually, simply open a new terminal after the dependencies are installed.

```sh
poetry shell
```
