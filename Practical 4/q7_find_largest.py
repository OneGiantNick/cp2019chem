def find_largest(x):
    x.sort(reverse=True)
    print(x[0])


alist = [5, 1, 8, 7, 2]
print(find_largest(alist))
