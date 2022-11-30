import pandas as pd

df = pd.read_json("capital.json")
print(df.loc[[0]])
