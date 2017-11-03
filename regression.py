import pandas as pd
import quandl
import math

quandl.ApiConfig.api_key = 'DXX9S7_12yxqeNXJuUcy'
df = quandl.get_table('WIKI/PRICES', ticker='A', date='2017-10-24,2017-10-25,2017-10-26,2017-10-27,2017-10-28,2017-10-29,2017-10-30,2017-10-31,2017-11-01,2017-10-02')
df = df[['adj_open','adj_high','adj_low','adj_close','adj_volume']]
df['hl_pct'] = (df['adj_high'] - df['adj_close']) / df['adj_close'] * 100.0
df['pct_change'] = (df['adj_close'] - df['adj_open']) / df['adj_open'] * 100.0

df = df[['adj_close','hl_pct','pct_change','adj_volume']]

forecast_col = 'adj_close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)

df.dropna(inplace=True)
print(df.tail())