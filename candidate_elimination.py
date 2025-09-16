#candidate elimination algorithm
import numpy as np
import pandas as pd
dataset = pd.read_csv('lab1.csv')

concept = np.array(dataset)[:,:-1]
target = np.array(dataset)[:,-1]

def train_sg(con,tar):
    s = con[0].copy()
    g = [['?' for _ in range(len(s))] for _ in range(len(s))]

    for i,val in enumerate(con): 
        if tar[i]=='yes':
            for x in range(len(s)): 
                if val[x] != s[x]:
                    s[x]='?'
                    g[x][x]='?'
        else:
            for x in range(len(s)): 
                if val[x]!=s[x]: 
                    g[x][x]=s[x]
                else: 
                    g[x][x] = '?'
        print(f'{i}')
        print(str(s))
        print(str(g))
    g = [g[i] for i, val in enumerate(g) if val !=['?' for _ in range(len(g))]]
    print('\n\n')
    print(str(s))
    print(str(g))

print(train_sg(concept,target))
