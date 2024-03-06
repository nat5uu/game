import pandas as pd
df = pd.read_csv("./recepies.csv", header = 'infer', sep =";")

print(df)

neue_zeile = {"Input_1": "none","Input_2": "none","Activated":1,"Item":"feuer"}
df.loc[len(df)] = neue_zeile
print(df)