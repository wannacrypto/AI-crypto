import pandas as pd
import time
import os
import datetime
import natsort
from tqdm import tqdm

path = './orderbook_data'

df_26 = pd.read_csv('./orderbook_merge_data/'+'2022-11-26-upbit-btc-krw-orderbook'+'.csv')

merge_df = df_26
merge_df = merge_df.reset_index(drop=True)
merge_df = merge_df[['timestamp','price','quantity','side']]
merge_df = merge_df.rename(columns={'side':'type'})
merge_df.to_csv(
    './orderbook_merge_data/' +'mod_partial_orderbook.csv',  sep=',', index=False)
