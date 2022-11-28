import pandas as pd
import time
import os
import datetime
import natsort
from tqdm import tqdm

path = './orderbook_data'

df_25 = pd.read_csv('./orderbook_merge_data/'+'2022-11-25-upbit-btc-krw-orderbook'+'.csv')
df_26 = pd.read_csv('./orderbook_merge_data/'+'2022-11-26-upbit-btc-krw-orderbook'+'.csv')
df_27 = pd.read_csv('./orderbook_merge_data/'+'2022-11-27-upbit-btc-krw-orderbook'+'.csv')

merge_df = pd.concat([df_25,df_26,df_27], axis=0)
merge_df = merge_df.reset_index(drop=True)
merge_df = merge_df[['timestamp','price','quantity','side']]
merge_df = merge_df.rename(columns={'side':'type'})
merge_df['timestamp'] = merge_df['timestamp'].apply(lambda x:x[:-7])
merge_df.to_csv(
    './orderbook_merge_data/' +'mod_orderbook.csv',  sep=',', index=False)
