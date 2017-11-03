import pandas as pd
import quandl

quandl.ApiConfig.api_key = 'DXX9S7_12yxqeNXJuUcy'
df = quandl.get_table('WIKI/PRICES', ticker='A', date='1999-11-18,1999-11-19,1999-11-22,1999-11-23,1999-11-24,1999-11-25,1999-11-26')
df = df[['adj_open','adj_high','adj_low','adj_close','adj_volume']]
df['hl_pct'] = (df['adj_high'] - df['adj_close']) / df['adj_close'] * 100.0
df['pct_change'] = (df['adj_close'] - df['adj_open']) / df['adj_open'] * 100.0

df = df[['adj_close','hl_pct','pct_change','adj_volume']]

print(df.head())


