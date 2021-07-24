a = None
b = None

def swap(a, b):
    a, b = b, a
    return a, b

res = swap(12, 13)
print(res)
print(type(res))

print(f'a:{res[0]}, b:{res[1]}')
