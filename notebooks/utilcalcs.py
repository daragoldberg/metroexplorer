import math
import numpy as np

def get_moe(m):
    result = math.sqrt(sum(map(lambda x: x**2, m)))
    return result

def get_cv(e, m): 
    if e == 0:
        return np.nan
    else:
        return np.absolute(m/1.645/e*100)
    
def get_pct(e,agg_e):
    if agg_e == 0:
        return np.nan
    else:
        return e/agg_e

def get_pctmoe(e,m,agg_e,agg_m): #check to make sure this doesn't break 
    if agg_e == 0:
        return np.nan
    else: 
        return (1/agg_e)*math.sqrt((m**2)-(((e/agg_e)**2)*(agg_m**2)))