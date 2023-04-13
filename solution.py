import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 388568881 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    if proportions_ztest([x_success,y_success],[x_cnt,y_cnt], alternative = 'larger')[1] > 0.1:
      return False
    else:
      return True
