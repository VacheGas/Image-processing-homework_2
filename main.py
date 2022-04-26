from cmath import sqrt
import math
import numpy as np


def dot_product(A: list[int], B: list[int])->int:
	"""
	calculate doc product
	"""
	zipo_vec = zip(A, B)
	dot_result = 0
	for x1, x2 in zipo_vec:
	    dot_result = dot_result + x1 * x2
	return dot_result


def cross_prod(A: list[int], B: list[int]):
    C = []
    C.append(A[1] * B[2] - B[1] - A[2])
    C.append(A[2] * B[0] - B[2] - A[0])
    C.append(A[0] * B[1] - B[0] - A[1])
    return C

A = [1,4,5]
B = [3,2,7]
C = [9,3,6]

AB = cross_prod(A, B)
BC = cross_prod(B,C)
print(AB)
print(BC)

dot = dot_product(AB, BC)
print(dot)
mod_AB = sqrt(AB[0]**2 + AB[1]**2 + AB[2]**2)
mod_BC = sqrt(BC[0]**2 + BC[1]**2 + BC[2]**2)
end_mod = mod_AB * mod_BC
angle_cos = dot / end_mod
print(angle_cos)
angle = np.arccos(angle_cos)
print("ba",math.degrees(angle))