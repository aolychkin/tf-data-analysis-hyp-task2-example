import pandas as pd
import numpy as np


chat_id = 1068310526 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    statistic, critical_values, pvalue = anderson_ksamp([x, y])
    alpha = 0.05
    if statistic > critical_values[2]:
        return True
    else:
        return False
