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
# ['timestamp','quantity','price','fee','amount','side']

#read csvfile
trade_df = pd.read_csv("trade.csv")
result_df = pd.read_csv("3_2_result.csv")

pre_trade_df = trade_df[['timestamp','quantity','price']]

pre_trade_df = pre_trade_df.assign(mid_price=0.0,Bfeature=0.0,Alpha=0.0)

trade_side = trade_df[['side']]

mod_trade_df = pd.concat([pre_trade_df,trade_side], axis=1)

i_start = 0
i_stop = 0

for i in range(int(len(mod_trade_df))) :
  tar = str(mod_trade_df.loc[i]['timestamp'][0:10])
  if (tar == "2019-05-17" and not(bool(i_start))):
    i_start = i
  elif (tar == "2019-05-18" and i_start) : 
    i_stop = i
    break

trade_df_body=mod_trade_df[i_start:i_stop].reset_index(drop=True)

save_index = 0

for k in range(int(len(result_df))):
    current_ts = result_df.loc[k,'timestamp']
    current_mid_price = result_df.loc[k,'mid_price']
    current_Bfeature = result_df.loc[k,'Bfeature']
    current_Alpha = result_df.loc[k,'Alpha']
    for i in range(save_index,int(len(trade_df_body)),1):
        tar_ts = trade_df_body.loc[i,'timestamp']
        if(current_ts == tar_ts):
            trade_df_body.loc[i,'mid_price'] = current_mid_price
            trade_df_body.loc[i,'Bfeature'] = current_Bfeature
            trade_df_body.loc[i,'Alpha'] = current_Alpha
        
        else:
            save_index = i
            break
        
    
result_df = trade_df_body.reset_index(drop=True)         

result_df.to_csv('./New_2019-05-trade.csv',sep=',',index=False)

pd.concat([result_df.head(20),result_df.tail(20)],axis=0).to_csv('./New_2019-05-trade_partial.csv',sep=',')
