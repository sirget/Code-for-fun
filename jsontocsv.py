import pandas as pd

df = pd.read_json(r'./data_train.json')

export_csv = df.to_csv(r'./new.csv', index=None, header=True)
