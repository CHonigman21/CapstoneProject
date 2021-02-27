import pandas as pd

df = pd.read_csv("NFL Play by Play 2009-2018 (v5).csv")

df_2018 = df[df['game_date'].str.startswith('2018')]

