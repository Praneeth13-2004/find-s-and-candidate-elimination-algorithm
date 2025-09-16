#find s algorithm
import numpy as np
import pandas as pd
df = pd.read_csv('lab1.csv')
rows = np.array(df)[:,:-1]
target = np.array(df)[:,-1]

def find_s(data, tar):
    for i, val in enumerate(tar):
        if val == 'yes':
            hyp = data[i].copy() 
    for i, val in enumerate(data): 
        if tar[i]=='yes':
            for x in range(len(hyp)):
                if val[x]!=hyp[x]:
                    hyp[x]='?'
                else:
                    pass 
    return hyp

x = find_s(rows, target)
print(x)
