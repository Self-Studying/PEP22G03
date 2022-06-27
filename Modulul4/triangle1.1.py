
def este_triunghi(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True


def este_triunghi_isoscel(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True


print(este_triunghi(1, 1, 1))
print(este_triunghi_isoscel(4, 1, 3))
