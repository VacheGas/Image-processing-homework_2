from cmath import cos, sin


def rotate(A:list[int], angle):
    new_cord = []
    new_cord.append(A[0] * cos(angle) - A[1] * sin(angle))
    new_cord.append(A[1] * cos(angle) + A[0] * sin(angle))
    print(new_cord[0], new_cord[1])


rotate([3,6],90)