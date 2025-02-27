import pandas as pd
import numpy as np
from scipy.stats import laplace, norm, ks_2samp, anderson_ksamp, cramervonmises_2samp

chat_id = 781119239 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    
    p_value = anderson_ksamp([x, y]).pvalue
    return p_value < 0.04
    
