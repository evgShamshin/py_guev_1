from decimal import Decimal as D

d = D(input())
res = d.exp() + d.ln() + d.log10() + d.sqrt()
print(res)