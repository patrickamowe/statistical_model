from mean_and_sd import population_mean, population_standard_deviation, sample_mean, sample_standard_deviation, cal_sample_deviation_with, cal_sample_deviation_without
from correlation import pearson_correlation

x = [12,16,16,15,13,19,10,12,17,14]
y = [35,46,48,50,40,65,28,37,49,55]

arr = [2,3,6,8,11]
method = "with"
n = 2
N = len(arr)

mean = population_mean(arr)
standard_deviation = population_standard_deviation(arr, mean)
sample_mean = sample_mean(arr, n, method)
sample_standard_deviation = sample_standard_deviation(arr, n, method, sample_mean)
cal_sample_deviation_without = cal_sample_deviation_without(standard_deviation, n,N)
cal_sample_deviation_with = cal_sample_deviation_with(standard_deviation, n)

r = pearson_correlation(x, y, len(x))
print(r)