def matrix(n=None, m=None, v=None):
    match n, m, v:
        case int() as n, int() as m, int() as v:
            return [[v for _ in range(m)] for _ in range(n)]

    match n, m:
        case int() as n, int() as m:
            return [[0 for _ in range(m)] for _ in range(n)]

    match n:
        case int() as n:
            return [[0 for _ in range(n)] for _ in range(n)]

    return [[0]]

print(matrix(6, 8, 7))