import pandas as pd
import time
import os
import datetime
from tqdm import tqdm

pd.set_option('display.max_columns', 100)

def midprice():
    orderbook_df = pd.read_csv("./orderbook_merge_data/mod_orderbook.csv")

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
    mid_price_list = pd.Series(mid_price_list) 

    result_df = pd.concat([timestamp_series,mid_price_list],axis=1)

    result_df.columns = ['timestamp','mid_price']

    print(result_df)

    result_df.to_csv('./result/midprice.csv',sep=',',index=False)
    
    
def Book_I():
    orderbook_df = pd.read_csv("./orderbook_merge_data/mod_orderbook.csv")

    ratio = 0.2
    level = 5
    interval = 1
    
    time_stamp_list = []
    book_i_list = []

    for i in tqdm(range(int(len(orderbook_df)/10))):
        askqty = bidqty = askpx = bidpx = book_p = 0
        
        df_order = orderbook_df.loc[10*i:(10*i)+9].reset_index(drop=True)
        time_stamp_list.append(df_order.loc[0,'timestamp'])
        
        df_bid = df_order.loc[0:4]
        df_ask = df_order.loc[5:9]
        
        df_bid = df_bid.sort_values(by=['price'], axis=0, ascending=False).reset_index(drop=True)
        df_ask = df_ask.sort_values(by=['price'], axis=0, ascending=True).reset_index(drop=True)

        top_bid = df_bid.iloc[0]['price']
        top_ask = df_ask.iloc[0]['price']
        
        mid_price = (top_bid+top_ask)/2

        
        if(mid_price != 0):
        
            
            for j in range(int(len(df_bid))):
                bidqty += df_bid.iloc[j]['quantity']**ratio
                bidpx += df_bid.iloc[j]['price']*(df_bid.iloc[j]['quantity']**ratio)

            for k in range(int(len(df_ask))):
                askqty += df_ask.iloc[j]['quantity']**ratio
                askpx += df_ask.iloc[j]['price']*(df_ask.iloc[j]['quantity']**ratio)
            
            book_p = ( ((askqty*bidpx)/bidqty) + ((bidqty*askpx)/askqty) )/ (bidqty+askqty)
            book_i = (book_p - mid_price)/interval
            book_i_list.append(book_i)
            
        else:
            book_i_list.append(0)
            
    timestamp_series = pd.Series(time_stamp_list)
    book_i_series = pd.Series(book_i_list) 

    result_df = pd.concat([timestamp_series,book_i_series],axis=1)

    result_df.columns = ['timestamp','book-imbalance-0.2-5-1']

    print(result_df)

    result_df.to_csv('./result/book_i.csv',sep=',',index=False)

def merge():
    m_df = pd.read_csv("./result/midprice.csv")
    i_df = pd.read_csv("./result/book_i.csv")
    print(i_df['book-imbalance-0.2-5-1'],m_df['mid_price'],m_df['timestamp'])
    result_df = pd.concat([i_df['book-imbalance-0.2-5-1'],m_df['mid_price'],m_df['timestamp']],axis=1)
    result_df = result_df.reset_index(drop=True)
    result_df.to_csv('./result/2022-11-25_26_27-upbit-btc-krw-feature.csv',sep=',',index=False)
    
midprice()
Book_I()
time.sleep(2)
merge()
