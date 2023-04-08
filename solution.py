import pandas as pd
import numpy as np


chat_id = 388568881 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    if 1.1 * x_success / x_cnt >= y_success / y_cnt:
      return False
    else:
      return True
