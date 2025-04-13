import math
import numpy as np
import matplotlib.pyplot as plt

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
interval_freqs, _ = np.histogram(data, bins=intervals)
relative_freqs = []
accum_freqs = []
accum_rel_freqs = []
interval_middles = []



# 3
header = (
    f"| {'№':^3} | {'Границы':^15} | {'Середина':^10} | {'Частота':^8} | "
    f"{'Отн. частота':^15} | {'Накопл. частота':^17} | {'Накопл. отн. частота':^22} | {'Плотность':^12} |"
)
print("-" * len(header))
print(header)
print("-" * len(header))

current_accum = 0
current_rel_accum = 0
total_count = sum(interval_freqs)

for i in range(len(interval_freqs)):
    left = intervals[i]
    right = intervals[i + 1]
    interval_middles.append((left + right) / 2)
    relative_freqs.append(interval_freqs[i] / total_count)

    current_accum += interval_freqs[i]
    accum_freqs.append(current_accum)

    current_rel_accum += relative_freqs[i]
    accum_rel_freqs.append(current_rel_accum)

    density = relative_freqs[i] / (right - left)

    print(
        f"| {i + 1:^3} | [{left:.2f}; {right:.2f}) | {interval_middles[i]:^10.2f} | {interval_freqs[i]:^8} | "
        f"{relative_freqs[i]:^15.4f} | {accum_freqs[i]:^17} | {accum_rel_freqs[i]:^22.4f} | {density:^12.4f} |"
    )

print("-" * len(header))
interval_middles = np.round(interval_middles, 2)



# 4
plt.figure(figsize=(18, 6))

# Полигон абсолютных частот
plt.subplot(1, 3, 1)
X = interval_middles
Y = interval_freqs
plt.plot(X, Y, marker='o', color='b', label='Полигон абс. частот')
plt.fill_between(X, Y, alpha=0.3, color='b') # fill color
plt.title('Полигон абс. частот')
plt.xlabel('Середины интервалов')
plt.ylabel('Абсолютная частота')
plt.grid(True)
for i, val in enumerate(Y):
    plt.text(X[i], val, str(val), ha='center', va='bottom', color='b', fontsize=15)
plt.xticks(X, labels=[str(m) for m in X])

# Гистограмма относительных частот и полигон относительных частот
Y = relative_freqs
plt.subplot(1, 3, 2)
plt.bar(X, Y, width=intervals[1] - intervals[0], edgecolor='black', alpha=0.6, label='Гистограмма отн. частот')
plt.plot(X, Y, marker='o', color='r', label='Полигон отн. частот', linestyle='--')
plt.title('Гистограмма + полигон отн. частот')
plt.xlabel('Середины интервалов')
plt.ylabel('Отн. частота')
plt.grid(True)
for i, val in enumerate(Y):
    plt.text(X[i], val, f'{val:.2f}', ha='center', va='bottom', color='r', fontsize=15)
plt.xticks(X, labels=[str(m) for m in X])

# Гистограмма плотности
width = intervals[1] - intervals[0]
density = relative_freqs / width
Y = density
plt.subplot(1, 3, 3)
plt.step(X, Y, where='mid', color='g', label='Гистограмма плотности')
plt.fill_between(X, Y, step='mid', alpha=0.3, color='g')
plt.title('Гистограмма плотности отн. частот')
plt.xlabel('Середины интервалов')
plt.ylabel('Плотность отн. частоты')
plt.grid(True)
for i, val in enumerate(Y):
    plt.text(X[i], val, f'{val:.2f}', ha='center', va='bottom', color='g', fontsize=15)
plt.xticks(X, labels=[str(m) for m in X])

plt.tight_layout()
plt.savefig('../../plots/1.1.4.png')
plt.close()



# 5
# Построить эмпирическую функцию распределения интервального ряда Fn(x)),
# то есть относительную частоту (частость) того, что признак (случайная величина X)
# примет значение, меньшее заданного x , т.е. Fn(x) = w(X < x) .
# Для данного эмпирическая функция распределения представляет накопленную частость
# w^{acc}_x = n^{acc}_x / n.
# Графиком эмпирической функции распределения является кумулята накопленных относительных
# частот, то есть ломаная, вершины которой имеют абсциссы, совпадающие с правыми границами
# интервалов группировки, и ординаты, совпадающие со значениями накопленных частот
# для соответствующих интервалов.

plt.xlabel('Значение $x$')
X = intervals[1:]
X = np.round(X, 2)
plt.ylabel('$F_n(x)$')
Y = accum_rel_freqs

plt.figure(figsize=(8, 5))
plt.plot(X, Y, color='m', label='Эмпирическая F')
plt.scatter(X, Y, color='m', zorder=3)
for i, val in enumerate(Y):
    plt.text(X[i], val, f'{val:.2f}', ha='right', va='bottom', color='m', fontsize=12)
plt.xticks(X, labels=[str(m) for m in X])
plt.title('Эмпирическая функция распределения $F_n(x)$')
plt.grid(True)
plt.legend()
plt.savefig('../../plots/1.1.5.png')



# 6
# Найти эмпирическую функцию распределения дискретного вариационного ря-
# да (cередины интервалов – накопленные относительные частоты). Здесь эмпирическая
# функция распределения представляет собой разрывную ступенчатую функцию по анало-
# гии с функцией распределения для дискретной случайной величины с той разницей, что
# по оси ординат вместо вероятностей – накопленные частости

plt.xlabel('Середины интервалов')
plt.ylabel('Накопленные отн. частоты')
Y = accum_rel_freqs

plt.figure(figsize=(8, 5))
plt.step(X, Y, where='mid', color='c', label='Эмпирическая F (дискретная)')
plt.scatter(X, Y, color='c', zorder=3)
for i, val in enumerate(Y):
    plt.text(X[i], val, f'{val:.2f}', ha='right', va='bottom', color='c', fontsize=12)
plt.xticks(X, labels=[str(m) for m in X])
plt.title('Эмпирическая F (дискретный вариационный ряд)')
plt.grid(True)
plt.legend()
plt.savefig('../../plots/1.1.6.png')



# 7
sample_mean = 0
biased_dispersion_est = 0
unbiased_dispersion_est = 0
rmsd = 0 # root mean square deviation

for i in range(len(interval_middles)):
    w = interval_freqs[i] / n
    sample_mean += interval_middles[i] * w
print(f"Выборочное среднее = {round(sample_mean, 2)}")

for i in range(len(interval_middles)):
    w = interval_freqs[i] / n
    biased_dispersion_est += (interval_middles[i] - sample_mean) ** 2 * w
print(f"Смещенная оценка дисперсии = {round(biased_dispersion_est, 2)}")

unbiased_dispersion_est = n / (n - 1) * biased_dispersion_est
print(f"Несмещенная оценка дисперсии = {round(unbiased_dispersion_est, 2)}")

rmsd = np.sqrt(unbiased_dispersion_est)
print(f"Среднеквадратичное отклонение = {round(rmsd, 2)}")



# 10
summ = 0
for i in range(len(interval_freqs)):
    summ += ((round((interval_middles[i] - sample_mean)**3, 2)) * interval_freqs[i])

# 11
summ = 0
for i in range(len(interval_freqs)):
    cur = ((round((interval_middles[i] - sample_mean)**4, 2)) * interval_freqs[i])
    print(round((interval_middles[i] - sample_mean)**4), interval_freqs[i])
    summ += cur

print(82.7/15.06)
