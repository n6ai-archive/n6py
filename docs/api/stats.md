# stats

A module to display information and statistics about underlying data.

```py
from n6py import stats
```

## n_changed <Badge type="tip" text="0.1.12" />

Returns a stats string about the difference between the previous and current values.

- **path:** `n6py.stats.n_changed`
- **args:** `prev`, `curr`

::: details type

```py
(function) n_changed(
  prev: int | Sequence[Unknown] | Collection[Unknown] | NDArray[Unknown] | Series[Unknown] | DataFrame,
  curr: int | Sequence[Unknown] | Collection[Unknown] | NDArray[Unknown] | Series[Unknown] | DataFrame
) -> str
```

:::

::: code-group

```py [Code]
from n6py.stats import n_changed

change_1 = n_changed(100, 50)
change_2 = n_changed([1, 2, 3, 4], [1, 2])

print(change_1)
print(change_2)
```

```py [Result]
Current: 50 - Previous: 100 | Change: 50 - 50.00%
Current: 2 - Previous: 4 | Change: 2 - 50.00%
```

:::
