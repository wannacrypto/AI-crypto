import pandas as pd
import time
import os
import datetime
from tqdm import tqdm

merge_df = pd.read_csv('./trade_merge_data/'+'trade_merged'+'.csv')
merge_df.groupby('timestamp')