a = (1,2,3,4)
a[0]

a = (1,1,1,1,1,2,3,4)
print(a.count(2))
print(a.count(1))
print(a.index(3))

a = set([1,2,3,4,5])
b = {3,4,5}

a.add(3)
a.add(10)
print(a.intersection(b))