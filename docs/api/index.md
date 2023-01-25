# API

<p>
  <a href="https://pypi.org/project/n6py" target="_blank">
    <img src="https://img.shields.io/pypi/v/n6py?color=%23141414&style=for-the-badge" alt="PyPI Latest Release" width="127" height="28">
  </a>
</p>

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

| API                     | Description                                                           |
| ----------------------- | --------------------------------------------------------------------- |
| [app](/api/app)         | A module to create app wrappers around code bases and git repos.      |
| [display](/api/display) | A module to display content in Jupyter Notebooks.                     |
| [encode](/api/encode)   | A module for encoding data.                                           |
| [stats](/api/stats)     | A module to display information and statistics about underlying data. |
