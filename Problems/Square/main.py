""" :var: size of square """
n: int = 4
""" :var: symbol for square """
symbol = "*"

for i in range(n):
    for j in range(n):
        if j == 0:
            print(symbol, end='')
            continue

        if j == (n - 1):
            print(' {}'.format(symbol), end='')
            continue

        if i in (0, n - 1):
            print(' {}'.format(symbol), end='')
            continue

        print('  ', end='')

    print()
