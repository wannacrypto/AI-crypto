import pandas as pd
import time
import os
import datetime
import natsort
from tqdm import tqdm

path = './trade_data'

file_list = os.listdir(path)
file_list = natsort.natsorted(file_list)

head = file_list[0]
tail = file_list[-1]

head_i = int(head[6:-4])
tail_i = int(tail[6:-4])

error_report = []

#bid = 0, ask = 1

def ts_mod(sr):
    ts = sr['trade_date_utc'] +' '+sr['trade_time_utc']
    ts = pd.to_datetime(ts)
    return ts

for i in tqdm(range(head_i, tail_i+1, 1)):
    if (i == head_i):
        merge_df = pd.read_csv('./trade_data/'+'trade_'+str(i)+'.csv')
        date = merge_df.iloc[0]['trade_date_utc']
        continue
    try:
        temp_df = pd.read_csv('./trade_data/'+'trade_'+str(i)+'.csv')
        cur_date = temp_df.iloc[0]['trade_date_utc']
        merge_df = merge_df.drop_duplicates(['sequential_id'])
        
        if(cur_date != date):
            merge_df = merge_df[['trade_date_utc','trade_time_utc','trade_price','trade_volume','ask_bid','sequential_id']]
            merge_df = merge_df.drop_duplicates(['sequential_id'])
            merge_df = merge_df.replace('BID',0)
            merge_df = merge_df.replace('ASK',1)
            merge_df['timestamp'] = merge_df.apply(ts_mod,axis=1)
            merge_df = merge_df.sort_values(by='timestamp').reset_index(drop=True)
            merge_df = merge_df.drop(columns = ['trade_date_utc','trade_time_utc'])
            merge_df.to_csv(
                './trade_merge_data/'+date+'_trade_merged.csv',  sep=',', index=False)
            
            merge_df = pd.read_csv('./trade_data/'+'trade_'+str(i)+'.csv')
            date = cur_date
            continue
            
        merge_df = pd.concat([merge_df, temp_df], axis=0)

    except:
        error_report.append(str(datetime.datetime.fromtimestamp(i))+'.csv')
        
merge_df = merge_df[['trade_date_utc','trade_time_utc','trade_price','trade_volume','ask_bid','sequential_id']]
merge_df = merge_df.drop_duplicates(['sequential_id'])
merge_df = merge_df.replace('BID',0)
merge_df = merge_df.replace('ASK',1)
merge_df['timestamp'] = merge_df.apply(ts_mod,axis=1)
merge_df = merge_df.sort_values(by='timestamp').reset_index(drop=True)
merge_df = merge_df.drop(columns = ['trade_date_utc','trade_time_utc'])


merge_df.to_csv(
    './trade_merge_data/'+cur_date+'_trade_merged.csv',  sep=',', index=False)

print(error_report)
