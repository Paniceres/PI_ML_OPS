import pandas as pd

df_user_items = pd.read_parquet('/home/p/Code/Henry/PI_ML_OPS/data/user_items.parquet', engine='pyarrow')

rows = df_user_items.shape[0]

print(rows)