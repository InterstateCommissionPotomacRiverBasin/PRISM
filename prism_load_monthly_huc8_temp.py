# -*- coding: utf-8 -*-
"""
Created on Tue Mar 05 11:35:24 2019

@author: aseck
PRISM data analysis
"""


#import os
#import glob
import numpy as np
import pandas as pd
import time

start = time. time()

#savedir = "D:/2019_demandstudy/PRISM_data/monthly/"
textdir = "D:/2019_demandstudy/PRISM_raster/temp/monthly/"
maindir = "D:/2019_demandstudy/"
#os.chdir(savedir)

counties_file1 = maindir + "pot_huc8.txt"
counties_file2 = maindir + "huc8.csv"
outfile = maindir + "huc_monthly_temp1.csv"

df_counties =  pd.read_csv(counties_file2, sep=',', header=0, skiprows=0)
counties = np.loadtxt(counties_file1, skiprows=6)  

startyear = 2018 #year to start downloading precipitation data
endyear = 2018 #last year to download data
#year = startyear
df= pd.DataFrame()
#counties_list = [2795, 2785]
counties_list = df_counties['FID']
for county in counties_list:
    print county
    list=[]
    yearlist=[]
    monthlist=[]
    for year in range(startyear, endyear+1): #loop through years
        #textfile = textdir + str(year) + "/prism_ppt_stable_4kmm2_189501_bil.txt"
        #print textfile
        
        result_array = np.empty((0, 12))
        for i in range(1,9):
            textfile = textdir + str(year) + "/prism_tmean_stable_4kmm2_"+ str(year) + str(i).zfill(2)  + "_bil.txt"
            print textfile
            precip = np.loadtxt(textfile, skiprows=6)   
            precip[precip==-9999] = 'nan'
            precip[counties!=county] = 'nan'
            avg = np.nanmean(precip)
            list.append(avg)
            monthlist.append(i)
            yearlist.append(year)
            #result_array = np.append(result_array, [avg1], axis=0)
     
        result=np.array(list)
        result1=np.array(yearlist)
        result2=np.array(monthlist)
    df[str(county)] = result
df['year'] = result1
df['month'] = result2

df.to_csv(outfile)
end = time. time()
print(end - start)

#df = pd.read_csv(textfile, sep=r"\s+", header=None, skiprows=6)
#df= df.astype(float)  
#df1= df.replace(-9999, np.nan)



#df_avg = df[df_counties.values == 2795].values.mean()



"""
for year in range(startyear, endyear+1): #loop through years
    #os.chdir(str(year))
    if not os.path.exists(textdir + str(year)):
        os.mkdir(textdir + str(year))
    #os.chdir(textdir + str(year))
    
    print year
    #yearfile = savedir + "/" + str(year) + "/" + "PRISM_ppt_stable_4kmM2_" + str(year) +  "_bil.bil"
    #print yearfile
    #os.remove(yearfile)
    allFiles = glob.glob(savedir + "/" + str(year) + "/" + "*.bil")
    #print allFiles


    print str(year) + " done"
    for file_ in allFiles:
        title = file_[-37:-4]
        textfile = title + ".txt"
        #print textfile
        out_textfile = textdir + "/" + str(year) + "/" + textfile
        print file_
        print out_textfile
        arcpy.RasterToASCII_conversion(in_raster=file_,out_ascii_file=out_textfile)

"""