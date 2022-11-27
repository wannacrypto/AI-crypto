import pandas as pd
import csv
import sys
import numpy as np

# for prompt use
# promtin = sys.argv[1:]

pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)

#read csvfile
for i in range(15):
    if (i == 0):
        temp_df = pd.DataFrame(data=[["a",0.0,0.0,0]], columns=['A','B','C','D'])
    else :
        add_df = pd.DataFrame(data=[["a",0.0,0.0,0]], columns=['A','B','C','D'])
        temp_df = pd.concat([temp_df,add_df])
    print(temp_df)
