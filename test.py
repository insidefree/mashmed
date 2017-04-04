a = [10, 2, 3, 4, 5, 6, 3]

# a = a[2:1:-1]
# for i in a[::-1]:
#     if i == 3:
#         # del a[a.index(i)]
#         a = a[a[a.index(i + 1)]:a[a.index(i)]:-1]


# def foo(lst):
#     index = [ind for ind, x in enumerate(lst) if x == 3]
#     for ind in index[::-1]:
#         del lst[ind]
#         del lst[ind-1]
#         del lst[ind-2]
#     return lst
#
#
# for i in foo(a):
#     print(i)
#
# for i in a:
#     print(i)
# tmp = [enumerate(a)]
#
# for ind, val in tmp:
#     print(tmp[ind])

# for i, val in enumerate(a[::-1]):
#     tmp = a
#     print(a[i])
    # if a[i] == 3:
    #     del a[i]

# for i in a:
#     print(i)

for ind, val in enumerate(a):
    print(f'{ind}:{val}')

# tmp = [ind, val for ind, val in enumerate(a)]