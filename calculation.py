import pandas as pd
import time
import os
import datetime
from tqdm import tqdm

pd.set_option('display.max_columns', 100)

def book_D():
    path = './trade_merge_data/'

    file_list = os.listdir(path)

    target = file_list[0]
    trade_df = pd.read_csv(path+str(target))
    print(trade_df)
    
book_D()
#good