a = {'a': 1, 'b': 3}
b = {'b': 2, 'd': 4}

# Old format:
A = a.copy()
A.update(b)
print(A)

# New format
# Without updating 'a' dict
print(a | b)
print(a)

# Updating 'a' dict
a |= b
print(a)
