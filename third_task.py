import numpy as np
from scipy.linalg import lu
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import chisquare


A = np.array([
    [4, -3.4, 1, 1.8],
    [-2, 8, 0, -9],
    [2, -2.5, -7, 4],
    [1, -1, 5, 1]
])
P, L, U = lu(A)
print("P:")
print(P)
print("L:")
print(L)
print("U:")
print(U)

det_L = np.prod(np.diag(L))
det_U = np.prod(np.diag(U))
det_P = 1/np.linalg.det(P)
det_A = det_L * det_U * det_P 
print("\n", det_A)

n = 100
low, high = 0, 100
uniform_sample = np.random.randint(low, high + 1, n)
normal_sample = np.clip(np.random.normal(50, 15, 100), 0, 100).astype(int)
print("\n", uniform_sample)
print(normal_sample)
def characteristics(sample):
    print("Среднее:",sample.mean())
    print("Мода:", stats.mode(sample).mode)
    print("Медиана:", np.median(sample))
    print("Минимальное:", np.min(sample))
    print("Максимальное:", np.max(sample))
    print("Стандартное отклонение:", np.std(sample))
print("\nХарактеристики равномерного распределения:")
characteristics(uniform_sample)
print("Характеристики нормального распределения:")
characteristics(normal_sample)

def test_uniformity(sample, alpha=0.05):
    values, observed = np.unique(sample, return_counts=True)
    expected = np.full(len(values), len(sample) / len(values))
    chi2, p_value = chisquare(observed, expected)
    print("Равномерное" if p_value >= alpha else "Не равномерное")
    return p_value
print("\nРавномерная выборка:")
test_uniformity(uniform_sample)
print("Нормальная выборка:")
test_uniformity(normal_sample) # Выдаёт равномерность по причине низкого объема выборки