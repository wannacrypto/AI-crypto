import pandas as pd
import csv
import sys
from tqdm import tqdm

pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)

#Level 15 bid
#price,quantity,type,timestamp

#trade.csv
#timestamp,quantity,price,fee,amount,side
#2019-05-16 13:32,0.02243481,9568000,107.32,-214764,0

# read csvfile
orderbook_df = pd.read_csv("orderbook.csv")

mod_orderbook = pd.concat([orderbook_df['timestamp'],orderbook_df[["price","quantity","type"]]],axis=1)

temp_hr=0
temp_min=0
temp_sec=0
    
for i in tqdm(range(int(len(mod_orderbook)/30))) :
    df_order = mod_orderbook.loc[30*i:(30*i)+29].reset_index(drop=True)
    if (i == 0) : 
        new_order = df_order
        for i in range(int(len(df_order))) :
            part = new_order.iloc[i]
            stamp_split = part['timestamp'].split(".")
            stamp_str = stamp_split[0]
            stamp_slice = stamp_str[:-3]
            new_order.loc[i,'timestamp'] = stamp_slice
        continue
    
    if (df_order.iloc[0]['timestamp'][-9:-7]=='00'):
        for i in range(int(len(df_order))) :
            part = df_order.iloc[i]
            stamp_split = part['timestamp'].split(".")
            stamp_str = stamp_split[0]
            stamp_slice = stamp_str[:-3]
            df_order.loc[i,'timestamp'] = stamp_slice
        new_order = pd.concat([new_order,df_order]).reset_index(drop=True)

new_order.to_csv('./mod_orderbook.csv',sep=',',index=False)

