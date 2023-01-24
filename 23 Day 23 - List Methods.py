l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)

l.append(7)
print(l)

l.sort(reverse=True)
print(l)
l.reverse()
print(l)

s = [11, 45, 1, 2, 4, 6, 1, 1]
print(s.index(1))
print(s.count(1))

m = l
m[0] = 0
print(l)
m = l.copy()
m[0] = 0
print(l)

i = [11, 45, 1, 2, 4, 6, 1, 1]
i.insert(1, 899)
print(i)

l = [11, 45, 1, 2, 4, 6, 1, 1]
m = [900, 1000, 1100]
l.extend(m)     #it'll append in l
print(l)
k = l + m       #it'll merge
print(k)