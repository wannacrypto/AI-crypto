import pandas as pd
import time
import os
import datetime
from tqdm import tqdm

original_df = pd.read_csv('./trade_merge_data/'+'trade_merged.csv')

mod_df = original_df[['timestamp','trade_price','trade_volume','ask_bid','sequential_id']]
mod_df.columns = [['timestamp','price','quantity','type','sequential_id']]

mod_df.to_csv(
    './trade_merge_data/'+'mod_trade.csv',  sep=',', index=False)

#sync with orderbook (duration) was done by hand