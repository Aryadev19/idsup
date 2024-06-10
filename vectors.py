from functools import reduce
import math

v = [1,2,3]
w = [4,5,6]

def vector_add(v, w):
    return [i + j for i, j in zip(v, w)]

def vector_subtract(v, w):
    return [i - j for i, j in zip(v, w)]

def vector_sum(vectors):
    return reduce(vector_add, vectors)

def scalar_multiply(c, v):
    return [c * i for i in v]

def vector_mean(vectors):
    n = len(vectors)
    mean = vector_sum(vectors)
    return [ v / n for v in mean]

def dot(v, w):
    return sum(i * j for i, j in zip(v, w))

def sum_of_squares(v):
    return dot(v, v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
    return math.sqrt(squared_distance(v, w))

print(vector_add(v,w))
print(vector_subtract(v,w))
print(scalar_multiply(4,v))
print(vector_sum([v,w]))
print(vector_mean([v,w]))
print(dot(v,w))