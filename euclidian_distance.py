import pandas as pd
from scipy.spatial import distance
from sklearn import preprocessing

# Reading Sample Table
df = pd.read_csv("./db/cidades_metrics.csv",
                 sep=",",
                 encoding="utf-8-sig",
                 low_memory=False,
                 index_col="key")

df.fillna(0, inplace=True)

# Normalizing Values (0 to 1
df = pd.DataFrame(preprocessing.MinMaxScaler().fit_transform(df.values),
                  columns=df.columns,
                  index=df.index)

# Calculating Euclidian Distance Between Cities
ed = pd.DataFrame(data=distance.cdist(df.values, df.values),
                  columns=list(df.index),
                  index=df.index)

# Nominal 5 Closest Cities
auxl = []
for col in ed.columns:
    auxl.append({'City': col,
                 '1st_close': ed[col].sort_values().index[1],
                 '2st_close': ed[col].sort_values().index[2],
                 '3st_close': ed[col].sort_values().index[3],
                 '4st_close': ed[col].sort_values().index[4],
                 '5st_close': ed[col].sort_values().index[5],
                 })

lf = pd.DataFrame.from_dict(auxl)
lf.set_index('City', inplace=True)

# Saving Calculated Tables to db
ed.to_csv("./db/euclidian_matrix_br_cities.csv",
          sep=",",
          encoding="utf-8-sig")

lf.to_csv("./db/closest_ed_cities.csv",
          sep=",",
          encoding="utf-8-sig")
