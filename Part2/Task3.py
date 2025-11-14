import numpy as np
import scipy.linalg as linalg

def solvation(A, b):
    A_ = linalg.inv(A)
    x = np.dot(A_, b)
    return x

m = np.array([[-2, -8.5, -3.4, 3.5],
              [0, 2.4, 0, 8.2],
              [2.5, 1.6, 2.1, 3],
              [0.3, -0.4, -4.8, 4.6]])
v = np.array([-1.88, -3.28, -0.5, -2.83])

solution = solvation(m, v)
print(solution)