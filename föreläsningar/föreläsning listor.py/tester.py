
konton = [1,2,3]
print(konton[0])
n = 2
konton[n] = 5
print(konton)

a = 33.6
print(round(33.6))


def add_interest(b, r):
    """Returnerar beloppet b med r% ränta. """
    return b * (1 + r/100)

a = 2000
b = 1.6
a = add_interest(a,b)
print(round(a))