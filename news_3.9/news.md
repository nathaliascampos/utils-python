# News in Python 3.9

To install:
``` bash
sudo apt install python 3.9
```

To run:
``` bash
python3.9
```

---

### New Union Operators to Merge Dictionaries

``` py
a = {'a': 1, 'b': 3}
b = {'b': 2, 'd': 4}
```

**Old format:**

dict.update() update the dictionary with the key-value pairs from another
dictionary, but it will modify the original dictionary.

``` py
A = a.copy()
A.update(b)
print(A)
```

**New format:**

Using the union operator.
``` py
# Without updating 'a' dict
a | b
# Updating 'a' dict
a |= b
```

### Remove suffix and prefix from a string

``` py 
string = "https://site.com.br/"

string.removesuffix('/')
string.removeprefix('https://')
```