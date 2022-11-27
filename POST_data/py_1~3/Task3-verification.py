import pandas as pd
import csv
import sys
from tqdm import tqdm

pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)

#Level 15 bid
#price,quantity,type,timestamp

#mod_orderbook.csv
#Level 15 bid
#timestamp,price,quantity,type
#2019-05-17 00:00:00,9449000.0,40.39262446,0

#trade.csv
#timestamp,quantity,price,fee,amount,side
#2019-05-16 13:32,0.02243481,9568000,107.32,-214764,0

#read csvfile

#read csvfile
trade_df = pd.read_csv("trade.csv")
orderbook_df = pd.read_csv("orderbook.csv")

mod_orderbook = pd.concat([orderbook_df['timestamp'],orderbook_df[["price","quantity","type"]]],axis=1)

d = 0
temp_hr=0
temp_min=0
temp_sec=0
        
error_list=[]
    
for i in tqdm(range(int(len(orderbook_df)/30))) :
    if (d==60):
        d = 0
        
    df_order = orderbook_df.loc[30*i:(30*i)+29].reset_index(drop=True)
    
    df_bid = df_order.loc[0:14].reset_index(drop=True)
    df_ask = df_order.loc[15:29].reset_index(drop=True)
    
    if (int(df_order.iloc[0]['timestamp'][-2:])==d):
        for j in range(len(df_bid)):
            if(df_bid.iloc[j]['type']==0):
                pass
            else:
                print("error!! ask side exists in bid side in ",30*i+j,"th data")
            
            if(df_ask.iloc[j]['type']==1):
                pass
            else:
                print("error!! bid side exists in ask side in ",30*i+j,"th data")
        
    else :
        temp_hr=0
        temp_min=0
        temp_sec=0
        for i in range(i):
            temp_sec +=1
            if (temp_sec == 60) :
                temp_min +=1
                temp_sec = 0

            if (temp_min == 60) :
                temp_hr +=1
                temp_min = 0
        msg = str(temp_hr).zfill(2)+":"+str(temp_min).zfill(2)+":"+str(temp_sec).zfill(2)
        error_list.append(i)
        error_list.append(msg)
        d +=1
    d +=1
print(error_list)
        

# date_list.append(d)
# cnt_list.append(temp_cnt)
# acc_buy_cnt_list.append(temp_acc_buy)
# acc_sell_cnt_list.append(temp_acc_sell)

# date_series = pd.Series(date_list)
# cnt_series = pd.Series(cnt_list)
# acc_buy_cnt_series = pd.Series(acc_buy_cnt_list)
# acc_sell_cnt_series = pd.Series(acc_sell_cnt_list)

# result_df = pd.concat([date_series,cnt_series,acc_buy_cnt_series,acc_sell_cnt_series],axis=1)
# result_df.columns = ['date','Daily','Daily_buy','Daily_sell']



