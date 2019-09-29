# -*- coding: utf-8 -*-
"""
Editor de Spyder

"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file_path = 'orders.xlsx'
df = pd.read_excel(file_path, encoding='utf-16')



nt_orders = df[df.taken == 0]

#chage date format
nt_orders['created_at']= pd.to_datetime(nt_orders.created_at)
#create a copy to contrast data
nto_dayweek = nt_orders

#get day of week from created_at
nto_dayweek['created_at']= nto_dayweek.created_at.dt.dayofweek

#group by day of week
by_day_of_week = nto_dayweek.groupby(['created_at']).size()
 
 
#calculate de percentage
not_dayweek_percentage = []
indexx = []
result={'day':[],'percentage':[]}
total_nto = 9689
for i, v in by_day_of_week.iteritems():
    percentage = (v/total_nto)*100 
    not_dayweek_percentage.append(percentage)
    indexx.append(i)
    result['day'].append(i)
    result['percentage'].append(percentage)
    
    
percentage_result = pd.DataFrame.from_dict(result)

days = {0:'Mon',1:'Tues',2:'Weds',3:'Thurs',4:'Fri',5:'Sat',6:'Sun'}

percentage_result['day'] = percentage_result['day'].apply(lambda x: days[x])
 
