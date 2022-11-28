import pandas as pd
import time
import os
import datetime
from tqdm import tqdm

pd.set_option('display.max_columns', 100)

trade_df = pd.read_csv("./trade_merge_data/mod_trade.csv").head(2000)

head_ts = pd.to_datetime('2022-11-25 21:30:12')

for i in range(10):
    if (i == 0):
        ts = head_ts
    print(ts)
    
    temp_df = trade_df[trade_df['timestamp'] == str(ts)]

    print(temp_df)
    
    if(not(temp_df.empty)):
        try:
            bidcnt = temp_df['type'].value_counts()[0]
            print('bidcnt : ' ,temp_df['type'].value_counts()[0])
        except:
            bidcnt = 0
            print('bidcnt : ' ,bidcnt)
            
        try:
            askcnt = temp_df['type'].value_counts()[1]
            print('askcnt : ' ,temp_df['type'].value_counts()[1])
        except:
            askcnt = 0
            print('askcnt : ' ,askcnt)
        
    else:
        bidcnt = 0
        askcnt = 0
    
    