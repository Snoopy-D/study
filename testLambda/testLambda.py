f = lambda x,y,z: z + y + z
print f(4, 2, 6)

L = {
    'f1':(lambda x,y: x**2 + y**2),
    'f2':(lambda x,y: x**3 + y**3),
    'f3':(lambda x,y: x**4 + y**3)
}
print L['f2'](3,2)