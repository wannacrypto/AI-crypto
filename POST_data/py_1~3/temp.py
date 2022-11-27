import pandas as pd
import csv
import sys
from tqdm import tqdm

#mod_orderbook.csv
#Level 15 bid
#timestamp,price,quantity,type
#2019-05-17 00:00:00,9449000.0,40.39262446,0

#trade.csv
#timestamp,quantity,price,fee,amount,side
#2019-05-16 13:32,0.02243481,9568000,107.32,-214764,0

#read csvfile
trade_df = pd.read_csv("trade.csv")
orderbook_df = pd.read_csv("mod_orderbook.csv")

for i in range (5):
    print(orderbook_df.loc[30*i:(30*i)+29,'timestamp'])
    