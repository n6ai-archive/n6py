# encode

A module for encoding data.

```py
from n6py import encode
```

## split_most_common <Badge type="tip" text="0.1.12" />

Keeps the x most common values and encodes everything else as the provided remainder.

- **path:** `n6py.encode.split_most_common`
- **args:** `values`, `num_to_keep`, `remainder`

::: details Type

```py
(function) split_most_common(
  values: list[Unknown] | tuple[Unknown, ...] | NDArray[Unknown] | Series[Unknown],
  num_to_keep: int = 10,
  remainder: str | int | float | None = "other"
) -> (list[Unknown] | tuple[Unknown, ...] | NDArray[Unknown] | Series[Unknown])
```

:::

::: code-group

```py [Code]
from n6py.encode import split_most_common

x = [1, 1, 1, 2, 2, 3, 4]
x_split = split_most_common(x, 2)

print(x_split)
```

```py [Result]
[1, 1, 1, 2, 2, 'other', 'other']
```

:::

## split <Badge type="tip" text="0.1.12" />

Keeps the provided values and encodes everything else as the provided remainder.

- **path:** `n6py.encode.split`
- **args:** `values`, `values_to_keep`, `remainder`

::: details Type

```py
(function) split(
  values: list[Unknown] | tuple[Unknown, ...] | NDArray[Unknown] | Series[Unknown],
  values_to_keep: list[Unknown] | tuple[Unknown, ...] | NDArray[Unknown] | Series[Unknown],
  remainder: str | int | float | None = "other"
) -> (list[Unknown] | tuple[Unknown, ...] | NDArray[Unknown] | Series[Unknown])
```

:::

::: code-group

```py [Code]
from n6py.encode import split

x = [1, 2, 3, 4]
x_split = split(x, [1, 2])

print(x_split)
```

```py [Result]
[1, 2, 'other', 'other']
```

:::
