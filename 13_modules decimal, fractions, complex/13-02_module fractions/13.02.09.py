from fractions import Fraction as F

_1, _2 = input(), input()
_math = [lambda x, y: f"{x} + {y} = {F(x) + F(y)}",
         lambda x, y: f"{x} - {y} = {F(x) - F(y)}",
         lambda x, y: f"{x} * {y} = {F(x) * F(y)}",
         lambda x, y: f"{x} / {y} = {F(x) / F(y)}"]

[print(func(_1,_2)) for func in _math]