import pandas as pd
import time
import os
import datetime
import natsort
from tqdm import tqdm

path = './orderbook_data'

file_list = os.listdir(path)
file_list = natsort.natsorted(file_list)

head = file_list[0]
tail = file_list[-1]

head_i = int(head[10:-4])
tail_i = int(tail[10:-4])

error_report = []

for i in tqdm(range(head_i, tail_i+1, 1)):
    if (i == head_i):
        merge_df = pd.read_csv('./orderbook_data/'+'orderbook_'+str(i)+'.csv')
        date = str(datetime.datetime.fromtimestamp(i))[:10]
        continue
    try:
        temp_df = pd.read_csv('./orderbook_data/'+'orderbook_'+str(i)+'.csv')
        if (str(datetime.datetime.fromtimestamp(i))[:10] != date):
            merge_df.to_csv(
                './orderbook_merge_data/' + date+'-upbit-btc-krw-orderbook.csv',  sep=',', index=False)
            date = str(datetime.datetime.fromtimestamp(i))[:10]
            merge_df = temp_df
        merge_df = pd.concat([merge_df, temp_df], axis=0)

    except:
        time_now = str(datetime.datetime.fromtimestamp(i))+'.000000'
        for k in range(10):
            if (k==0):
                temp_df = pd.DataFrame(data=[[0,0.0,0,time_now]], columns=['price','quantity','side','timestamp'])
            elif (k<5):
                add_df = pd.DataFrame(data=[[0,0.0,0,time_now]], columns=['price','quantity','side','timestamp'])
                temp_df = pd.concat([temp_df,add_df])
            else :
                add_df = pd.DataFrame(data=[[0,0.0,1,time_now]], columns=['price','quantity','side','timestamp'])
                temp_df = pd.concat([temp_df,add_df])
        merge_df = pd.concat([merge_df, temp_df], axis=0)
        error_report.append(str(datetime.datetime.fromtimestamp(i))+'.csv')

merge_df.to_csv(
    './orderbook_merge_data/' + date+'-upbit-btc-krw-orderbook.csv',  sep=',', index=False)

print(error_report)
