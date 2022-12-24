# Quick Start

Follow the instructions below to get started.

## Try n6py online

Click on the badge to open a demo notebook in Google Colab.

[![Open In Colab](https://img.shields.io/badge/Open%20In%20Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)](https://colab.research.google.com/github/n6ai/n6py/blob/main/notebooks/n6py-demo-colab.ipynb)

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
Cloud Notebook environments like Google Colab don't run the latest Python version required for some libraries like NumPy and Pandas that are bundled with n6py. You have to pass the `--no-deps` flag to prevent n6py from updating those libraries.
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

```sh [Google Colab]
!pip install n6py --no-deps
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
