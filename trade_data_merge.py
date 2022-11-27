import pandas as pd
import time
import os
import datetime
from tqdm import tqdm

path = './trade_data'

file_list = os.listdir(path)

head = file_list[0]
tail = file_list[-1]

head_i = int(head[6:-4])
tail_i = int(tail[6:-4])

error_report = []

#bid = 0, ask = 1

for i in tqdm(range(head_i, tail_i+1, 1)):
    if (i == head_i):
        merge_df = pd.read_csv('./trade_data/'+'trade_'+str(i)+'.csv')
        continue
    try:
        temp_df = pd.read_csv('./trade_data/'+'trade_'+str(i)+'.csv')
        merge_df = pd.concat([merge_df, temp_df], axis=0)

    except:
        error_report.append(str(datetime.datetime.fromtimestamp(i))+'.csv')
        
for i in tqdm(range(head_i, tail_i+1, 1)):
    if (i == head_i):
        merge_df = pd.read_csv('./trade_data/'+'trade_'+str(i)+'.csv')
        continue

    temp_df = pd.read_csv('./trade_data/'+'trade_'+str(i)+'.csv')
    merge_df = pd.concat([merge_df, temp_df], axis=0)

merge_df = merge_df.drop_duplicates(['sequential_id'])
merge_df = merge_df.replace('BID',0)
merge_df = merge_df.replace('ASK',1)
merge_df = merge_df.drop(['market'], axis=1)
merge_df = merge_df.sort_values(by='timestamp').reset_index(drop=True)


merge_df.to_csv(
    './trade_merge_data/'+'trade_merged.csv',  sep=',', index=False)

print(error_report)
