__author__ = 'Alex'
import pandas as pd
import random
import numpy as np
import timeit
import time

def PdsDf():
    df = pd.read_csv("household_power_consumption.txt", sep = ';', index_col = False, low_memory = False)
    #print(df.shape)
    df=df[(df['Global_active_power']!='?')]
    df['Global_active_power']=df['Global_active_power'].astype(float)
    df['Global_reactive_power']=df['Global_reactive_power'].astype(float)
    df['Voltage']=df['Voltage'].astype(float)
    df['Global_intensity']=df['Global_intensity'].astype(float)
    df['Sub_metering_1']=df['Sub_metering_1'].astype(float)
    df['Sub_metering_2']=df['Sub_metering_2'].astype(float)
    df['Sub_metering_3']=df['Sub_metering_3'].astype(float)
    #print(df.shape)
    return df

def ActPowHghrFive(df):
    ndf = df[df['Global_active_power']>5]
    #print(ndf.shape)
    print(ndf[:20])

def HighVoltage(df):
    ndf = df[df['Voltage']>235]
    print(ndf[:20])

def IntensAndSubMetTwoMoreThnThree(df):
    ndf = df[(df['Global_intensity']>19)&(df['Global_intensity']<20)&(df['Sub_metering_2']>df['Sub_metering_3'])]
    print (ndf[:20])

def RandFveHndrdThsnd(df):
    df.index = range(df.shape[0])
    arr = random.sample(range(df.shape[0]), 500000)
    ndf = df.ix[arr]
    print(ndf)
    print ("The avarage value of sub_metering_1 is", ndf['Sub_metering_1'].mean())
    print ("The avarage value of sub_metering_2 is", ndf['Sub_metering_2'].mean())
    print ("The avarage value of sub_metering_3 is", ndf['Sub_metering_3'].mean())

def AfterEghtn(df):
    ndf = df[(df['Time']>'18:00:00')&(df['Global_active_power']>6)&(df['Sub_metering_2']>df['Sub_metering_3'])&(df['Sub_metering_2']>df['Sub_metering_1'])]
    ndf.index = range(ndf.shape[0])
    arr = list(range(2, int(ndf.shape[0]/2), 3))
    arr.extend(list(range(int(ndf.shape[0]/2)+4, ndf.shape[0], 4)))
    ndf = ndf.ix[arr]
    print (ndf)



def NmpArr():
    ar = np.genfromtxt("household_power_consumption.txt", dtype=("S10","S10", float, float, float, float, float, float, float),
                       unpack=True, delimiter=";", missing_values='?', filling_values=-1, names=True)
    #print(ar.shape)
    return ar

def NmpActPowHghrFive(arr):
    narr = arr[arr['Global_active_power']>5]
    print(narr[:20])

def NmpHighVoltage(arr):
    narr = arr[arr['Voltage']>235]
    print(narr[:20])

def NmpIntensAndSubMetTwoMoreThnThree(arr):
    narr = arr[(arr['Global_intensity']>19)&(arr['Global_intensity']<20)&(arr['Sub_metering_2']>arr['Sub_metering_3'])]
    print (narr[:20])

def NmpRandFveHndrdThsnd(arr):
    nums = random.sample(range(arr.shape[0]), 500000)
    narr = arr.take(nums)
    print(narr)
    print ("The avarage value of sub_metering_1 is", narr['Sub_metering_1'].mean())
    print ("The avarage value of sub_metering_2 is", narr['Sub_metering_2'].mean())
    print ("The avarage value of sub_metering_3 is", narr['Sub_metering_3'].mean())

def NmpAfterEghtn(arr):
    narr = arr[(arr['Time'].astype(str)>'18:00:00')&(arr['Global_active_power']>6)&(arr['Sub_metering_2']>arr['Sub_metering_3'])&(arr['Sub_metering_2']>arr['Sub_metering_1'])]
    nums = list(range(2, int(narr.shape[0]/2), 3))
    nums.extend(list(range(int(narr.shape[0]/2)+4, narr.shape[0], 4)))
    narr = narr.take(nums)
    print (narr)

f = open("res.txt", 'w')
i = 0
t = [0,0,0,0,0,0,0,0,0,0,0,0]
while i < 20:
    temp = time.time()
    df = PdsDf()
    temp = time.time() - temp
    t[0] += temp
    t[1] += timeit.Timer(lambda: ActPowHghrFive(df)).timeit(number=1)
    t[2] += timeit.Timer(lambda: HighVoltage(df)).timeit(number=1)
    t[3] += timeit.Timer(lambda: IntensAndSubMetTwoMoreThnThree(df)).timeit(number=1)
    t[4] += timeit.Timer(lambda: RandFveHndrdThsnd(df)).timeit(number=1)
    t[5] += timeit.Timer(lambda: AfterEghtn(df)).timeit(number=1)
    temp = time.time()
    arr = NmpArr()
    temp = time.time() - temp
    t[6] += temp
    t[7] +=timeit.Timer(lambda: NmpActPowHghrFive(arr)).timeit(number=1)
    t[8] +=timeit.Timer(lambda: NmpHighVoltage(arr)).timeit(number=1)
    t[9] +=timeit.Timer(lambda: NmpIntensAndSubMetTwoMoreThnThree(arr)).timeit(number=1)
    t[10] +=timeit.Timer(lambda: NmpRandFveHndrdThsnd(arr)).timeit(number=1)
    t[11] +=timeit.Timer(lambda: NmpAfterEghtn(arr)).timeit(number=1)
    i+=1


for j in t:
    j = j / 20
    f.write(str(j) + '\n')
#NmpActPowHghrFive(arr)
#NmpHighVoltage(arr)
#NmpIntensAndSubMetTwoMoreThnThree(arr)
#NmpRandFveHndrdThsnd(arr)
#NmpAfterEghtn(arr)
f.close()