def fatorial(n, show=False):
    fat = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        fat *= c
    return fat


print(fatorial(5))