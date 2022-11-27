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
  print(tar)
  if (tar == "2019-05-17" and not(bool(i_start))):
    i_start = i
  elif (tar == "2019-05-18" and i_start) : 
    i_stop = i
    break
  print(i_start,i_stop)
    
print(i_start,i_stop)