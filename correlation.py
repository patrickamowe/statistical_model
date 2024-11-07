import math


def pearson_correlation(x, y, n):
    """
    :param x: is an array of the independent variables
    :param y: is an array of the dependent variables
    :param n: is the number of variable
    :return r: the correlation of the x and y
    """
    summation_x = 0
    summation_y = 0
    summation_xy = 0
    summation_y_square = 0
    summation_x_square = 0

    for i, e in zip(x, y):
        summation_x += i
        summation_x_square += i ** 2
        summation_y += e
        summation_y_square += e ** 2
        summation_xy += i*e

    numerator = (n * summation_xy)-(summation_x * summation_y)
    denominator = ((n * summation_x_square) - summation_x ** 2) * ((n * summation_y_square) - summation_y ** 2)
    r = numerator / math.sqrt(denominator)
    return r


def rank_elements(arr):
    """
    :param arr: An array of int
    :return: An array of ranking for each element in arr
    """

    sorted_arr = sorted(arr)
    ranks = {}

    rank = 1
    for value in sorted_arr:
        if value not in ranks:
            count = sorted_arr.count(value)
            ranks[value] = sum(range(rank, rank + count)) / count
            rank += count
    # Map ranks back to original array
    return [ranks[element] for element in arr]


def spearman_correlation(x, y, n):
    """
    :param x: is an array of the independent variables
    :param y: is an array of the dependent variables
    :param n: is the number of variable
    :return r: the correlation of the x and y
    """
    ranks_y = rank_elements(y)
    ranks_x = rank_elements(x)

    summation_d_square = 0
    for i, e in zip(ranks_y, ranks_x):
        summation_d_square += (i - e) ** 2

    numerator = 6 * summation_d_square
    denominator = n * ((n**2)-1)
    r = 1-(numerator/denominator)
    return r