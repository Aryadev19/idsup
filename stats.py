from collections import Counter
import math
from vectors import sum_of_squares,dot

def mean(x):
    return sum(x) / len(x)

def median(arr):
    n = len(arr)
    res = sorted(arr)
    if n % 2 == 1: return res[n // 2]
    else: return (res[n // 2] + res[n // 2 - 1]) / 2
    
def quantile(x, p):
    idx = int(p * len(x))
    return sorted(x)[idx]

def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [i for i, count in counts.iteritems() if count == max_count]

def data_range(x):
    return max(x) - min(x)

def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

def standard_deviation(x):
    return math.sqrt(variance(x))

def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0 # if no variation, correlation is zero


