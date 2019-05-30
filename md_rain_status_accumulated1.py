# -*- coding: utf-8 -*-
"""
Created on Thu May 23 12:05:18 2019

@author: Alimatou Seck @yaayu_sulay
"""



"""
For EACH COUNTY
    fOR EACH MONTH 
        Calculate  3, 6, 12-MONTH, and WY TO DATE, accumulated ACTUAL rain,
        Calculate  3, 6, 12-MONTH, and WY TO DATE, accumulated NORMAL rain,
For EACH REGION (by averaging counties)
    FOR EACH MONTH
        Calculate  3, 6, 12-MONTH, and WY TO DATE, accumulated ACTUAL rain,
        Calculate  3, 6, 12-MONTH, and WY TO DATE, accumulated NORMAL rain,
        Calculate  3, 6, 12-MONTH, and WY TO DATE, percentage,
        (Calculate  3, 6, 12-MONTH, and WY TO DATE, status)--> done in Excel

"""
import numpy as np
import pandas as pd
import time

#start = time. time()

"Output files"
maindir = "D:/2019_demandstudy/TIME_SERIES/"
outfile1 = maindir + "md_precip_perc1.csv" #3-month actual/normal percentage
outfile2 = maindir + "md_precip_perc2.csv"  #6-month actual/normal percentage
outfile3 = maindir + "md_precip_perc3.csv"  #12-month actual/normal percentage

"Import data"
infile = maindir + "md_time_series2.csv" #
df_indata =  pd.read_csv(infile, sep=',', header=0, skiprows=0)

#"""
#normal rain ##################################################################
df= pd.DataFrame()
for i in range(1,13):
    df1= df_indata.loc[df_indata['month'] == i]
    df2 = df1.iloc[:,3:13]
    df3 = df2.rolling(window=30).mean()
    df4 = pd.merge(df1.iloc[:,1:3], df3, left_index=True, right_index=True)
    df=df4.append(df)

df= df.sort_index()

#3-month accumulated normal
df5 = df.iloc[:,2:13]
df6 = df5.rolling(window=3).sum()
df7 = pd.merge(df.iloc[:,0:2], df6, left_index=True, right_index=True)
a =  df7[['2785','2795','2803']].mean(axis=1, skipna=True)
b =  df7[['2787','2790', '2791','2794','2795','2796','2797','2799']].mean(axis=1, skipna=True)
df7['western']= a
df7['central']= b

#6-month accumulated normal
df8 = df.iloc[:,2:13]
df9 = df8.rolling(window=6).sum()
df10 = pd.merge(df.iloc[:,0:2], df9, left_index=True, right_index=True)
a =  df10[['2785','2795','2803']].mean(axis=1, skipna=True)
b =  df10[['2787','2790', '2791','2794','2795','2796','2797','2799']].mean(axis=1, skipna=True)
df10['western']= a
df10['central']= b

#12-month accumulated normal
df11 = df.iloc[:,2:13]
df12 = df11.rolling(window=12).sum()
df13 = pd.merge(df.iloc[:,0:2], df12, left_index=True, right_index=True)
a =  df13[['2785','2795','2803']].mean(axis=1, skipna=True)
b =  df13[['2787','2790', '2791','2794','2795','2796','2797','2799']].mean(axis=1, skipna=True)
df13['western']= a
df13['central']= b

#==> calculate region average normals
###############################################################################
#"""

#actual rain ##################################################################
#3-month accumulated 
df_actual = df_indata.iloc[:,3:13]
df1_actual = df_actual.rolling(window=3).sum()
df1_actual1 = pd.merge(df_indata.iloc[:,1:3], df1_actual, left_index=True, right_index=True)
a =  df1_actual1[['2785','2795','2803']].mean(axis=1, skipna=True)
b =  df1_actual1[['2787','2790', '2791','2794','2795','2796','2797','2799']].mean(axis=1, skipna=True)
df1_actual1['western']= a
df1_actual1['central']= b

#6-month accumulated 
df2_actual = df_actual.rolling(window=6).sum()
df2_actual1 = pd.merge(df_indata.iloc[:,1:3], df2_actual, left_index=True, right_index=True)
a =  df2_actual1[['2785','2795','2803']].mean(axis=1, skipna=True)
b =  df2_actual1[['2787','2790', '2791','2794','2795','2796','2797','2799']].mean(axis=1, skipna=True)
df2_actual1['western']= a
df2_actual1['central']= b

#12-month accumulated 
df3_actual = df_actual.rolling(window=12).sum()
df3_actual1 = pd.merge(df_indata.iloc[:,1:3], df3_actual, left_index=True, right_index=True)
a =  df3_actual1[['2785','2795','2803']].mean(axis=1, skipna=True)
b =  df3_actual1[['2787','2790', '2791','2794','2795','2796','2797','2799']].mean(axis=1, skipna=True)
df3_actual1['western']= a
df3_actual1['central']= b

#then calculate region accumulated  (3-6-12 month) actual rain
"""a =  df1_actual1[['2785','2795']].mean(axis=1, skipna=True)
b =  df1_actual1[['2787','2790', '2791','2794','2795','2796','2797','2799']].mean(axis=1, skipna=True)
df1_actual1['western']= a
df1_actual1['central']= b
"""

###############################################################################

#then calculate percentage (actual/normal)
df_perc1 = pd.merge(df_indata.iloc[:,1:3], df1_actual1.iloc[:,2:14].div(df7.iloc[:,2:14]), left_index=True, right_index=True)
df_perc2 = pd.merge(df_indata.iloc[:,1:3], df2_actual1.iloc[:,2:14].div(df10.iloc[:,2:14]), left_index=True, right_index=True)
df_perc3 = pd.merge(df_indata.iloc[:,1:3], df3_actual1.iloc[:,2:14].div(df13.iloc[:,2:14]), left_index=True, right_index=True)

df_perc1.to_csv(outfile1)
df_perc2.to_csv(outfile2)
df_perc3.to_csv(outfile3)
