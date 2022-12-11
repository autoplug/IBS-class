import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_json("capital.json")
df.info()

data = pd.DataFrame(list(df["data"]),columns=["name","capital","iso2"])
print(df)
