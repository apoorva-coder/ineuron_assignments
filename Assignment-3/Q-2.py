"""
Implement List comprehensions to produce the following lists.
Write List comprehensions to produce the following Lists

['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
[[2, 3, 4, 5], [3, 4, 5, 6],[4, 5, 6, 7], [5, 6, 7, 8]]
[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
"""

l=['x','y','z']
m=[i*k for i in l for k in range(1,5)]
print(m)

n = [i*k for k in range(1,5) for i in l]
print(n)

y = [2,3,4]
o = [[i+k]for i in y for k in range(3) ]
print(o)

z = [2,3,4,5]
q = [[i+k for k in range(4)]for i in z ]
print(q)


u = [(j,i) for i in range(1,4) for j in range(1,4)]
print(u)