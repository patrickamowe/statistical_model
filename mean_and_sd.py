import math, itertools


def population_mean(arr_x_vals):
    """
    :param arr_x_vals: is an array contain x variables
    :return: the population mean
    """
    summation_x = 0
    N = len(arr_x_vals)

    for x in arr_x_vals:
        summation_x += x

    mean = round(summation_x / N, 2)
    return mean


def population_standard_deviation(arr_x_vals, mean):
    summation_x_mean = 0
    N = len(arr_x_vals)

    for x in arr_x_vals:
        summation_x_mean += (x - mean) ** 2

    standard_deviation = round(math.sqrt(summation_x_mean / N), 2)
    return standard_deviation


def with_replacement(arr_x_vals, sample_size):
    arr_vals = []
    val = 0
    arr_possible_samples = list(itertools.product(arr_x_vals, repeat=sample_size))
    for i in arr_possible_samples:
        for v in i:
            val += v
        arr_vals.append(round(val/sample_size, 2))
        val = 0
    return arr_vals


def without_replacement(arr_x_vals, sample_size):
    arr_vals = []
    val = 0
    arr_possible_samples = list(itertools.combinations(arr_x_vals, sample_size))
    for i in arr_possible_samples:
        for v in i:
            val += v
        arr_vals.append(round(val/sample_size, 2))
        val = 0
    return arr_vals


def sample_mean(arr_x, sample_size, method):
    summation_arr_vals = 0
    if method.lower() == "without":
        arr_vals = without_replacement(arr_x, sample_size)
        for i in arr_vals:
            summation_arr_vals += i
        mean = round(summation_arr_vals/len(arr_vals), 2)
        return mean
    else:
        arr_vals = with_replacement(arr_x, sample_size)
        for i in arr_vals:
            summation_arr_vals += i
        mean = round(summation_arr_vals / len(arr_vals), 2)
        return mean


def sample_standard_deviation(arr_x, sample_size, method, mean):
    summation_x_mean = 0
    if method.lower() == "without":
        arr_vals = without_replacement(arr_x, sample_size)
        n = len(arr_vals)
        for x in arr_vals:
            summation_x_mean += (x - mean) ** 2

        standard_deviation = round(math.sqrt(summation_x_mean / n), 2)
        return standard_deviation
    else:
        arr_vals = with_replacement(arr_x, sample_size)
        n = len(arr_vals)
        for x in arr_vals:
            summation_x_mean += (x - mean) ** 2

        standard_deviation = round(math.sqrt(summation_x_mean / n), 2)
        return standard_deviation


def cal_sample_deviation_with(sd, n):
    """
        n : sample size
        sd : standard deviation of the population
        we can use those values to  calculate the sample standard deviation with replacement
    """
    standard_deviation = round(sd/math.sqrt(n), 2)
    return standard_deviation


def cal_sample_deviation_without(sd, n, N):
    """
        N : population size
        n : sample size
        sd : standard deviation of the population
        we can use those values to  calculate the sample standard deviation without replacement
    """
    standard_deviation = round((sd/math.sqrt(n)) * math.sqrt((N-n)/(N-1)), 2)
    return standard_deviation
