from fractions import Fraction as F

res = []
n = int(input())
for _1 in range(1, n + 1):
    for _2 in range(1, n + 1):
        if _1 > 1:
            if (0 < _1 / _2 < 1
                    and (_1 % _2 != 0 and _2 % _1 != 0)): res.append(F(f"{_1}/{_2}"))
        else:
            if (0 < _1 / _2 < 1
                    and (_1 % _2 != 0 or _2 % _1 != 0)): res.append(F(f"{_1}/{_2}"))

print(*sorted(set(res)), sep="\n")