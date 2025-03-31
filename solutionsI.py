import math
import numpy as np

data = [
    5.13, 11.95, 13.60, 12.27, 16.62, 15.37, 17.00, 17.06, 14.20, 17.76, 16.31, 14.51, 12.81, 13.21, 12.58,
    11.54, 15.92, 14.11, 11.00, 15.96, 14.91, 15.75, 15.31, 13.46, 15.46, 14.68, 15.70, 16.86, 13.96, 14.28,
    13.83, 13.56, 13.01, 15.64, 16.43, 14.28, 13.91, 16.41, 14.18, 16.59, 13.00, 13.57, 12.10, 15.82, 16.37,
    16.29, 14.13, 13.66, 12.95, 17.08, 15.73, 14.02, 15.63, 16.58, 14.85, 12.50, 15.16, 14.94, 14.36, 12.46,
    14.52, 15.31, 15.97, 16.00, 13.44, 16.80, 13.83, 14.67, 17.37, 15.40, 14.85, 17.24, 17.27, 15.06, 13.15,
    15.03, 14.74, 15.64, 16.09, 13.28, 17.81, 17.28, 18.20, 14.61, 13.75, 14.03, 14.25, 14.67, 14.09, 14.29,
    12.00, 9.97, 14.48, 13.23, 17.88, 19.89, 16.38, 14.70, 13.97, 15.25
]

data.sort()
n = len(data)


# 1
R = data[-1] - data[0]


# 2
m = int(1 + math.log2(n))
h = R / m
print(f" Число интервалов по Стёрженсу = {m}, длина интервала = {h}")
print(f"Размах выборки = {data[-1]} - {data[0]} = {R}\n")

intervals = np.linspace(data[0], data[-1], m + 1)
freq, _ = np.histogram(data, bins=intervals)


# 3
header = (
    f"| {'№':^3} | {'Границы':^15} | {'Середина':^10} | {'Частота':^8} | "
    f"{'Отн. частота':^15} | {'Накопл. частота':^17} | {'Накопл. отн. частота':^22} | {'Плотность':^12} |"
)
print("-" * len(header))
print(header)
print("-" * len(header))

accum_freq = 0
accum_rel_freq = 0
total_count = sum(freq)

for i in range(len(freq)):
    left = intervals[i]
    right = intervals[i + 1]
    midpoint = (left + right) / 2
    relative_freq = freq[i] / total_count
    accum_freq += freq[i]
    accum_rel_freq += relative_freq
    density = relative_freq / (right - left)

    print(
        f"| {i + 1:^3} | [{left:.2f}; {right:.2f}) | {midpoint:^10.2f} | {freq[i]:^8} | "
        f"{relative_freq:^15.4f} | {accum_freq:^17} | {accum_rel_freq:^22.4f} | {density:^12.4f} |"
    )

print("-" * len(header))
print("\nПроверка: сумма частот =", sum(freq))


# 4