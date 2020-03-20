import math
import numpy as np
import pandas as pd

def calculate_sumgeo(df,sumgeo):
    variables = list(df.columns[1:])
    var = list(set([i.replace('E', '')\
                .replace('M', '')\
                .replace('C', '') for i in variables]))
    results = []
    for i in df[sumgeo].unique():
        dff = df[df[sumgeo] == i]
        record = {}
        record[sumgeo] = i
        for v in var:
            e = dff[f'{v}E'].sum()
            if f'{v}M' not in dff.columns:
                m = np.nan
            else:
                m = math.sqrt(dff[f'{v}M'].apply(lambda x: x**2).sum())
            if m == 0 or e == 0:
                c = np.nan
            else:
                c = np.absolute(m/1.645/e*100) #double check CV math
            record[f'{v}E'] = e
            record[f'{v}M'] = m
            record[f'{v}C'] = c            
        results.append(record)   
    r = pd.DataFrame(results)
    return r

def calc_muni_agg(df,sumgeo):
    variables = list(df.columns[1:])
    var = list(set([i.replace('E', '')\
                .replace('M', '') for i in variables]))
    results = []
    for i in df[sumgeo].unique():
        dff = df[df[sumgeo] == i]
        record = {}
        record[sumgeo] = i
        for v in var:
            e = dff[f'{v}E'].sum()
            if f'{v}M' not in dff.columns:
                m = np.nan
            else:
                m = math.sqrt(dff[f'{v}M'].apply(lambda x: x**2).sum())
            record[f'{v}E'] = e
            record[f'{v}M'] = m            
        results.append(record)   
    r = pd.DataFrame(results)
    return r