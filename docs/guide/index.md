# Quick Start

Follow the instructions below to get started.

## Try Online

Click one of the icons to start with a fresh copy of `n6py` in an online environment.

<table>
  <tbody>
    <tr>
      <td>
        <a href="https://colab.research.google.com/github/n6ai/n6py/blob/main/notebooks/n6py-demo.ipynb" target="_blank">
          <img width="42" height="42" src="/icons/colab.svg" />
        </a>
      </td>
      <td>
        <a href="https://mybinder.org/v2/git/https%3A%2F%2Fgithub.com%2Fn6ai%2Fn6py/HEAD?labpath=%2Fnotebooks%2Fn6py-demo.ipynb" target="_blank">
          <img width="42" height="42" src="/icons/binder.svg" />
        </a>
      </td>
      <td>
        <a href="https://kaggle.com/kernels/welcome?src=https://github.com/n6ai/n6py/blob/main/notebooks/n6py-demo.ipynb" target="_blank">
          <img width="80" height="42" src="/icons/kaggle.svg" />
        </a>
      </td>
    </tr>
  </tbody>
</table>

## Prerequisites

- Python >= `3.8`

::: tip
You can check the current Python version by running the executable with a `--version` flag.
:::

::: code-group

```sh [Terminal]
python --version
```

```sh [Jupyter Notebook]
!python --version
```

:::

## Installation

To get started you have to install `n6py` with your preferred package manager.

::: warning
Some cloud notebook environments like Kaggle don't run the latest Python version required for some libraries like NumPy and Pandas that are bundled with `n6py`. Those environments have their own versions pre-installed. You have to pass the `--no-deps --ignore-requires-python` flags to ignore the minimum required Python version and to prevent `n6py` from updating those libraries.
:::

::: code-group

```sh [Pip]
pip install n6py
```

```sh [Pipx]
pipx install n6py
```

```sh [Poetry]
poetry add n6py
```

```sh [Jupyter Notebook]
!pip install n6py
```

```sh [Colab]
!pip install n6py --no-deps
```

```sh [Kaggle]
!pip install n6py --no-deps --ignore-requires-python --root-user-action=ignore
```

:::

## Import

You can either import the entire package, specific modules or functions.

::: code-group

```py [Package]
import n6py as n6
```

```py [Modules]
from n6py import encode, stats
```

```py [Functions]
from n6py.stats import n_changed
```

:::

## Usage

::: code-group

```py [Code]
import n6py as n6

change = n6.stats.n_changed(100, 50)
print(change)
```

```py [Result]
Current: 50 - Previous: 100 | Change: 50 - 50.00%
```

:::
