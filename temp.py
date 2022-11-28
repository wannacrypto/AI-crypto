import pandas as pd
import time
import os
import datetime
from tqdm import tqdm

pd.set_option('display.max_columns', 100)

def ts_mod(sr):
    ts = sr['trade_date_utc'] +' '+sr['trade_time_utc']
    ts = pd.to_datetime(ts)
    return ts


orderbook_df = pd.read_csv("./trade_merge_data/trade_merged.csv").head(2000)
orderbook_df = orderbook_df[['trade_date_utc,trade_time_utc','trade_price','trade_volume','ask_bid','sequential_id']]

orderbook_df['timestamp']= orderbook_df.apply(ts_mod,axis=1)