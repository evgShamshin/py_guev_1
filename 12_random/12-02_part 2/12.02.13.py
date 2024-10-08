from random import choice
from string import ascii_letters, digits

letters = "".join(list(i for i in ascii_letters if i not in "lIOo"))

n, m = int(input()), int(input())
res = list("".join(choice(letters + digits[2:]) for i in range(m)) for j in range(n))
print(*res, sep="\n")