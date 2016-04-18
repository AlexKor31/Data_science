__author__ = 'Alexander'
import urllib.request
import datetime
import pandas as pd
import os

def download(index):

    if index < 10:
        index = "0"+str(index)
    else:
        index = str(index)
    url = "http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R"+index+".txt"
    vhi_url = urllib.request.urlopen(url)
    curDate = datetime.datetime.now().isoformat('_')
    curDate = curDate.replace(":", "_")
    curDate = curDate.replace("-", "_")
    filename = "vhi_id_"+index+"_"+curDate+".csv"
    out = open(filename,'wb')
    out.write(vhi_url.read())
    out.close()
    print ("VHI is successfully downloaded...")

def showFrame(path):
    df = pd.read_csv(path, index_col=False, header = 1)
    df = df.rename(columns={"%Area_VHI_LESS_15":"AED", "%Area_VHI_LESS_35":"AMD"})
    print(df.shape)
    print(dir(df.shape))
    df = df[(df['VHI']>=0)&(df['TCI']>=0)&(df['VCI']>=0)&(df['SMN']>=0)&(df['SMT']>=0)]
    print (len(df))

def monitorVHI(path):
    df = pd.read_csv(path, index_col=False, header = 1)
    df = df[(df['VHI']>=0)&(df['TCI']>=0)&(df['VCI']>=0)&(df['SMN']>=0)&(df['SMT']>=0)]
    print ("Enter a year to monitor the VHI.")
    year = int(input())
    max_vhi = df[(df['year']==year)]['VHI'].max()
    print ("MaxVHI for this year:",max_vhi)
    min_vhi = df[(df['year']==year)]['VHI'].min()
    print ("MinVHI for this year:",min_vhi)

def RegionSelect():
    print("You can download data for some region:")
    regions = {1: "Cherkasy", 2: "Chernihiv", 3:"Chernivtsi", 4:"Crimea", 5:"Dnipropetrovs'k", 6:"Donets'k", 7:"Ivano-Frankivs'k",
           8:"Kharkiv", 9:"Kherson", 10:"Khmel'nits'kyy", 11:"Kiev", 12:"Kiev City", 13:"Kirovohrad", 14:"Luhans'k", 15:"L'viv",
           16:"Mykolayiv", 17:"Odessa", 18:"Poltava", 19:"Rivne", 20:"Sevastopol'", 21:"Sumy", 22:"Ternopil'", 23:"Transcarpathia",
           24:"Vinnytsya", 25:"Volyn", 26:"Zaporizhzhya", 27:"Zhytomyr"}
    i = 1
    while i < 28:
        print(i, regions[i])
        i+=1
    print("\nPlease enter the index of the region.")
    index = 0
    flag = True
    while flag:
        try:
            index = int(input())
        except ValueError:
            print("Please enter the number in range from 1 to 27.")
        else:
            if index < 1 or index > 27:
                print("Please enter the number in range from 1 to 27.")
            else:
                flag = False
    return index

def FileSelect():
    path_f = []
    for d, dirs, files in os.walk(r"D:\PycharmProjects\srp_lab1"):
        for f in files:
            path = os.path.join(d,f) # формирование адреса
            path_f.append(path) # добавление адреса в список
    path_f = filter(lambda x: x.endswith('.csv'), path_f)
    files = []
    ix = 1
    for f in path_f:
        print (ix, "\t", f)
        ix+=1
        files.append(f)
    print("Please choose a file to load to a frame.")
    flag = True
    number = 1
    while flag:
        try:
            number = int(input())
        except ValueError:
            print("Please enter the number in range from 1 to", ix-1, ".")
        else:
            if number < 1 or number >= ix:
                print("Please enter the number in range from 1 to", ix-1, ".")
            else:
                flag = False
    return files[number-1]

def ExtremeDrought(path):
    df = pd.read_csv(path, index_col=False, header = 1)
    df = df[(df['VHI']>=0)&(df['TCI']>=0)&(df['VCI']>=0)&(df['SMN']>=0)&(df['SMT']>=0)]
    print ("Enter the critical value for part of the area with an extreme drought.")
    number = 0
    flag = True
    while flag:
        try:
            number = float(input())
        except ValueError:
            print ("Please enter the value in range from 0 to 100.")
        else:
            if number < 1 or number > 100:
                print("Please enter the value in range from 1 to 100.")
            else:
                flag = False
    years = []
    frame = df[(df['%Area_VHI_LESS_15'] > number)]['year']
    for f in frame:
        if f not in years:
            years.append(f)
    print ("Years you looked for:")
    for year in years:
        print (year)

def ModerateDrought(path):
    df = pd.read_csv(path, index_col=False, header = 1)
    df = df[(df['VHI']>=0)&(df['TCI']>=0)&(df['VCI']>=0)&(df['SMN']>=0)&(df['SMT']>=0)]
    print ("Enter the critical value for part of the area with a moderate drought.")
    number = 0
    flag = True
    while flag:
        try:
            number = float(input())
        except ValueError:
            print ("Please enter the value in range from 0 to 100.")
        else:
            if number < 1 or number > 100:
                print("Please enter the value in range from 1 to 100.")
            else:
                flag = False
    years = []
    frame = df[(df['%Area_VHI_LESS_35'] > number)]['year']
    for f in frame:
        if f not in years:
            years.append(f)
    print ("Years you looked for:")
    for year in years:
        print (year)

def Reindex(ix):
    arr = [0, 22, 24, 23, 25, 3, 4, 8, 19, 20, 21, 9, 26, 10, 11, 12, 13, 14, 15, 16, 27, 17, 18, 6, 1, 2, 7, 5]
    return arr[ix]

def Regions():
    regions = {1: "Cherkasy", 2: "Chernihiv", 3:"Chernivtsi", 4:"Crimea", 5:"Dnipropetrovs'k", 6:"Donets'k", 7:"Ivano-Frankivs'k",
           8:"Kharkiv", 9:"Kherson", 10:"Khmel'nits'kyy", 11:"Kiev", 12:"Kiev City", 13:"Kirovohrad", 14:"Luhans'k", 15:"L'viv",
           16:"Mykolayiv", 17:"Odessa", 18:"Poltava", 19:"Rivne", 20:"Sevastopol'", 21:"Sumy", 22:"Ternopil'", 23:"Transcarpathia",
           24:"Vinnytsya", 25:"Volyn", 26:"Zaporizhzhya", 27:"Zhytomyr"}
    i = 1
    new_reg = ["a",]
    while i < 28:
        print(i, regions[i])
        new_reg.append(regions[i])
        i+=1
    print("\n\n")
    i = 1
    while i < 28:
        new_reg[Reindex(i)] = regions[i]
        i+=1
    i = 1
    while i < 28:
        print(i, new_reg[i])
        i+=1

def spring(path):
    df = pd.read_csv(path, index_col=False, header = 1)
    df = df.rename(columns={"%Area_VHI_LESS_15":"AED", "%Area_VHI_LESS_35":"AMD"})
    df = df[(df['year']>=2000)&(df['week']>=13)&(df['week']<=21)&(df['VHI']>=0)&(df['TCI']>=0)&(df['VCI']>=0)&(df['SMN']>=0)&(df['SMT']>=0)]
    print(df)

#download(RegionSelect())
#curFile = FileSelect()
#showFrame(curFile)
#monitorVHI(curFile)
#ExtremeDrought(curFile)
#ModerateDrought(curFile)
Regions()
#spring(curFile)
#i = 1
#while i < 28:
#    download(i)
#    i+=1