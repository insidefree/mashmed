a = [1, 2, 3, 4, 5, 6, 7]
ia = iter(a)


for n in a[::2]:
    index = a.index(n)
    a[index] *= 2

for n in a:
    print(n)
