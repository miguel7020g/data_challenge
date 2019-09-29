# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 20:07:53 2019

@author: miguel
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


file_path = 'orders.xlsx'
df = pd.read_excel(file_path, encoding='utf-16')


###
nt_orders = df[df.taken == 0]
nt_orders['indexx'] =  nt_orders.total_earning/ nt_orders.to_user_distance


nt_orders = nt_orders[nt_orders.indexx < 60000]
nt_orders['indexx'].mean()

t1 =np.arange(len(nt_orders['indexx']))
plt.plot(t1,nt_orders['indexx'])
plt.ylabel('eraning/km(non-taken)')
plt.show()

###
t_orders = df[df.taken == 1]
t_orders['indexx'] = t_orders.total_earning/  t_orders.to_user_distance 

t_orders = t_orders[t_orders.indexx < 1000000]
t_orders['indexx'].mean()

t2 =np.arange(len(t_orders['indexx']))
plt.plot(t2,t_orders['indexx'])
plt.ylabel('eraning/km(taken)')
plt.show()


########################3

nt_orders = df[df.taken == 0]
nt_orders['pdist'] =(nt_orders.to_user_distance)**2 + (nt_orders.to_user_elevation/1000)**2 
nt_orders['pdist'] =np.sqrt(nt_orders['pdist'])

nt_orders['rate'] = nt_orders.total_earning/nt_orders['pdist']
nt_orders = nt_orders[nt_orders.rate < 400000]

t1 =np.arange(len(nt_orders['rate']))
plt.plot(t1,nt_orders['rate'])
plt.ylabel('eraning/km(non-taken with elevation)')
plt.show()

nt_orders['rate'].mean()

###

t_orders = df[df.taken == 1]
t_orders['pdist'] =(t_orders.to_user_distance)**2 + (t_orders.to_user_elevation/1000)**2 
t_orders['pdist'] =np.sqrt(t_orders['pdist'])

t_orders['rate'] = t_orders.total_earning/t_orders['pdist']

t_orders = t_orders[t_orders.rate < 1000000]
t2 =np.arange(len(t_orders['rate']))
plt.plot(t2,t_orders['rate'])
plt.ylabel('eraning/km(taken with elevation)')
plt.show()

t_orders['rate'].mean()



