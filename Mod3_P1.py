a=1

def add(b):
    return a+b

c=add(10)
print(c)

def f(*x):
    return sum(x)

print(f(4,43,6,-8,15,-10))
