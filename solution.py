import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 324151080 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = x.mean()
    var = sum([(i - loc) ** 2 for i in x])
    scale = np.sqrt(var / (len(x) - 1))
    return 2 * loc - 2 * (scale * norm.ppf(alpha / 2) / np.sqrt(len(x))), \
           2 * loc - 2 * (scale * norm.ppf(alpha / 2) / np.sqrt(len(x)))


#if __name__ == '__main__':
##    m = np.array([12, 24, 56, 78])
#    print(solution(0.95, m))