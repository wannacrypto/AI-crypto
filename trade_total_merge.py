import pandas as pd
import time
import os
import datetime
import natsort
from tqdm import tqdm

df_25 = pd.read_csv('./trade_merge_data/'+'2022-11-25_trade_merged'+'.csv')
df_26 = pd.read_csv('./trade_merge_data/'+'2022-11-26_trade_merged'+'.csv')
df_27 = pd.read_csv('./trade_merge_data/'+'2022-11-27_trade_merged'+'.csv')

def utc_to_kst(sr):
    ts = pd.to_datetime(sr)
    ts = ts + datetime.timedelta(hours=9)
    return str(ts)

merge_df = pd.concat([df_25,df_26,df_27], axis=0)
merge_df = merge_df.reset_index(drop=True)
mod_df = merge_df[['timestamp','trade_price','trade_volume','ask_bid','sequential_id']]
mod_df.columns = [['timestamp','price','quantity','type','sequential_id']]
mod_df['timestamp'] = merge_df['timestamp'].apply(utc_to_kst)
mod_df.to_csv(
    './trade_merge_data/' +'mod_trade.csv',  sep=',', index=False)
