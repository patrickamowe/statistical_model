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