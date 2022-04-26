def dot_product(A: list[int], B: list[int]):
    """
    calculate dot product
    """
    zipo_vec = zip(A, B)
    dot_result = 0
    for x1, x2 in zipo_vec:
        dot_result = dot_result + x1 * x2
    return dot_result
dot_product([4,1,1],[5,0,11])