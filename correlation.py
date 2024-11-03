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

    return [f"x: {summation_x}", f"x_squaress: {summation_x_square}", f"y: {summation_y}", f"y_square: {summation_y_square}", f"xy: {summation_xy}"]