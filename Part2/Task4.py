import numpy as np
from scipy.integrate import quad, dblquad

f1 = lambda x: x**2 + 1
f2 = lambda x, y: x + y

res1, err1  = quad(f1, 0, 10)
res2, err2 = dblquad(f2, 0, 10, lambda y: 0, lambda y: 10)

print(f"Definite integral = {res1}")
print(f"Double integral = {res2}")