Ex.1

```
|-123| = 123
| 27| = 27
|0} = 0
```

Ex. 2

```
  factor(30030) = 2 x 3 x 5 x 7 x 11 x 13
```

Ex. 3

```
  4x + 21 = 5

  ==> 4x = -16

  1. For N, no solutions.
  2. For Z, x = -4.
```

Ex. 4

```
  2x^3 - x^2 - 2x = -1

  ===> 2x^3 - 2x = x^2 - 1
  ===> 2x (x^2 - 1) = x^2 - 1

  1. For N:

    x = 1 is a solution since it reduces both sides to 0.

  2. For Z:

    x = {1, -1} are the solutions for the same reason.

  3. For Q:

    We have the solutions 1, -1 as above, and we can also eliminate (x^2 - 1) from both sides:

    ===> 2x = 1

    So the set of solutions is: {-1, 1, 1/2}
```

Ex. 5

```
  1. For (27, 5), m = 5, r = 2. Check: 27 = 5 x 5 + 2.
  2. For (27, -5), m = -5, r = 2. Check: 27 = -5 x -5 + 2.
  3. For (127, 0), there is no solution (since b =/= 0, by definition).
  4. For (-1687, 11), m = -154, r = 7. Check: -1687 = -154 x 11 + 7.
  5. For (0, 7), m = 0, r = 0. Check: 0 = 0 x 7 + 0.
```

Ex. 6

```
TBD

```

Ex. 7

See `ex7.py`.

```python
def d2b(n: int) -> List[int]:
    b = []

    while n > 0:
        b.append(str(n % 2))
        n //= 2
    b.reverse()

    return ''.join(b)
```

Ex. 8

```

```
