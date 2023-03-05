# n6py Contributing Guide

Welcome to the Contributing Guide! Glad you decided to contribute to n6py. Before submitting your contribution, please read the following guide:

## Structure

When first starting out, you will likely be focused on the following directories:

```
repo/                      📁 root directory
├── docs/                  📁 documentation
├── n6py/                  📁 main n6py package
├── playground/            📁 playground environment
├── notebooks/             📁 jupyter notebooks
├── tests/                 📁 n6py tests
└── ...
```

## Quick Start

### Cloud

Get started on a remote machine.

> You have to use the `--host` flag when working with vite inside a remote continer `npm run docs -- --host`

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

#### Install Python dependencies

Install all dependencies and create a `venv` with Poetry.

```sh
poetry install
```

#### Install Node.js dependencies

> git hooks are automatically added after npm installs all dependencies.

```sh
npm install
```

</details>

### Use venv

> The `venv` is automatically activated in `VS Code` when opening a new terminal window. You don't need to run the poetry shell command manually, simply open a new terminal after the dependencies are installed.

```sh
poetry shell
```

## Commands

> Commands are executed via npm scripts.

| Command                | Action                                     |
| :--------------------- | :----------------------------------------- |
| `npm run dev`          | Starts a dev server for playground/main.py |
| `npm run docs`         | Starts a dev server for docs               |
| `npm run docs-build`   | Builds the docs                            |
| `npm run docs-preview` | Serves the built docs                      |
| `npm run format`       | Runs black and prettier                    |
| `npm run lint`         | Runs pylint                                |
| `npm run test`         | Runs pytest                                |
| `npm run test-debug`   | Runs pytest with print statements enabled  |
| `npm run doctest`      | Runs doc tests on all n6py files           |

## Pull Request Guidelines

- Checkout a topic branch from a base branch, e.g. `main`, and merge back against that branch.

- If adding a new feature:

  - Add accompanying test case in [tests](https://github.com/n6ai/n6py/tree/main/tests).
  - Provide a convincing reason to add this feature. Ideally, you should open a suggestion issue first and have it approved before working on it.

- If fixing bug:

  - If you are resolving a special issue, add `(fix #xxxx[,#xxxx])` (#xxxx is the issue id) in your PR title for a better release log, e.g. `fix: update entities encoding/decoding (fix #3899)`.
  - Provide a detailed description of the bug in the PR.
  - Add appropriate tests if applicable.

- It's OK to have multiple small commits as you work on the PR - GitHub can automatically squash them before merging.

- Make sure tests pass!

- Commit messages must follow the [commit message convention](./COMMIT_CONVENTION.md) so that changelogs can be automatically generated. Commit messages are automatically validated before committing (by invoking [Git Hooks](https://git-scm.com/docs/githooks) via [simple-git-hooks](https://github.com/toplenboren/simple-git-hooks).

- No need to worry about code style as long as you installed the dev dependencies - modified files are automatically formatted with Prettier on commit (by invoking [Git Hooks](https://git-scm.com/docs/githooks) via [simple-git-hooks](https://github.com/toplenboren/simple-git-hooks).
