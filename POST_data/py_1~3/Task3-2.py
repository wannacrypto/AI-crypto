import pandas as pd
import csv
import sys
from tqdm import tqdm

pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)

#mod_orderbook.csv
#Level 15 bid
#timestamp,price,quantity,type
#2019-05-17 00:00:00,9449000.0,40.39262446,0

#trade.csv
#timestamp,quantity,price,fee,amount,side
#2019-05-16 13:32,0.02243481,9568000,107.32,-214764,0

#read csvfile
# trade_df = pd.read_csv("trade.csv")
orderbook_df = pd.read_csv("mod_orderbook.csv")

time_stamp_list = []
mid_price_list = []
Bfeature_list = []
Alpha_list = []

result_df = pd.DataFrame()

for i in range(int(len(orderbook_df)/30)):
    df_order = orderbook_df.loc[30*i:(30*i)+29].reset_index(drop=True)
    time_stamp_list.append(df_order.loc[0,'timestamp'])
    
    df_bid = df_order.loc[0:14]
    df_ask = df_order.loc[15:29]
    
    df_bid = df_bid.sort_values(by=['price'], axis=0, ascending=False).reset_index(drop=True)
    df_ask = df_ask.sort_values(by=['price'], axis=0, ascending=True).reset_index(drop=True)

    top_bid = df_bid.iloc[0]['price']
    top_ask = df_ask.iloc[0]['price']
    
    mid_price = (top_bid+top_ask)/2
    
    # ask_qty = df_ask['quantity'].mean()
    # bid_qty = df_bid['quantity'].mean()
    # bidPx = df_bid['price'].mean()
    
    # book_price = (ask_qty*bidPx)/bid_qty
    # Bfeature = (book_price - mid_price)
    
    # Alpha = Bfeature * mid_price
    
    # mid_price_list.append(mid_price)
    # Bfeature_list.append(Bfeature)
    # Alpha_list.append(Alpha)

timestamp_series = pd.Series(time_stamp_list)
mid_price_list = pd.Series(mid_price_list) 
# Bfeature_list = pd.Series(Bfeature_list)
# Alpha_list = pd.Series(Alpha_list)

result_df = pd.concat([timestamp_series,mid_price_list],axis=1)

result_df.columns = ['timestamp','mid_price']

print(result_df)

result_df.to_csv('./result/3_2_result.csv',sep=',',index=False)

