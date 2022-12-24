# API

[![PyPI Latest Release](https://img.shields.io/pypi/v/n6py?color=%23141414&style=for-the-badge)](https://pypi.org/project/n6py)

API reference for the `n6py` package. All modules within `n6py` are listed in the left sidebar.

## Structure

The `n6py` package contains multiple modules. Those modules expose functions, classes and variables.

```
n6py                         ➤ package
├── encode                   ➤ module
│   ├── split_most_common    ➤ function
│   ├── split                ➤ function
│   └── ...
├── stats                    ➤ module
│   ├── n_changed            ➤ function
│   └── ...
└── ...
```

## Modules

| API                   | Description                                                           |
| --------------------- | --------------------------------------------------------------------- |
| [encode](/api/encode) | A module for encoding data.                                           |
| [stats](/api/stats)   | A module to display information and statistics about underlying data. |
