import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 324151080 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    #beta = 
    loc = x.mean()
    var = sum([(i - loc) ** 2 for i in x])
    scale = np.sqrt(var / (len(x)))
    #return 2 * loc - 2 * (scale * norm.ppf(1 - alpha / 2) / np.sqrt(len(x))), \
    #       2 * loc + 2 * (scale * norm.ppf(1 - alpha / 2) / np.sqrt(len(x)))
    return loc - (scale * norm.ppf(1 - alpha / 2) / np.sqrt(len(x))), \
           loc + (scale * norm.ppf(1 - alpha / 2) / np.sqrt(len(x)))
    #return scale
    #return norm.ppf(alpha/2), norm.ppf(1 - alpha/2)
    #return norm.ppf(1 - alpha/2)
    #return loc

#if __name__ == '__main__':
##    m = np.array([0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 0.96, 0.97, 0.98, 0.99])
#    print(solution(0.95, m))