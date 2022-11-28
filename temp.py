import pandas as pd
import time
import os
import datetime
from tqdm import tqdm

pd.set_option('display.max_columns', 100)

def midprice():
    orderbook_df = pd.read_csv("./orderbook_merge_data/mod_orderbook.csv").head(2000)

    time_stamp_list = []
    mid_price_list = []

    for i in tqdm(range(int(len(orderbook_df)/10))):
        df_order = orderbook_df.loc[10*i:(10*i)+9].reset_index(drop=True)
        time_stamp_list.append(df_order.loc[0,'timestamp'])
        
        df_bid = df_order.loc[0:4]
        df_ask = df_order.loc[5:9]
        
        df_bid = df_bid.sort_values(by=['price'], axis=0, ascending=False).reset_index(drop=True)
        df_ask = df_ask.sort_values(by=['price'], axis=0, ascending=True).reset_index(drop=True)

        top_bid = df_bid.iloc[0]['price']
        top_ask = df_ask.iloc[0]['price']
        
        mid_price = (top_bid+top_ask)/2
        mid_price_list.append(mid_price)

    timestamp_series = pd.Series(time_stamp_list)
    timestamp_series = timestamp_series.apply(lambda x:x[:-7])
    mid_price_list = pd.Series(mid_price_list) 

    result_df = pd.concat([timestamp_series,mid_price_list],axis=1)

    result_df.columns = ['timestamp','mid_price']

    print(result_df)
    
midprice()