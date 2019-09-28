import json
import pandas as pd

file_path = 'orders2.xlsx'
df = pd.read_excel(file_path, encoding='utf-16')
dict = df.to_dict()
json = json.dumps(dict)
f = open("data.json", "w")
f.write(json)
f.close()
