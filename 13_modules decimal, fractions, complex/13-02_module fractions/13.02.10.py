from fractions import Fraction as F

print(sum([F(f"1/{i ** 2}") for i in range(1, int(input()) + 1)]))