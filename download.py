import requests
import zipfile
import datetime
import os

date = datetime.datetime.now().strftime("%d%b%Y")
dateddmmyyyy = datetime.datetime.now().strftime("%d%m%Y")

url = 'https://www.nseindia.com/content/historical/EQUITIES/2017/JUL/cmDATEbhav.csv.zip'
futURL = 'https://www.nseindia.com/content/historical/DERIVATIVES/2017/JUL/foDATEbhav.csv.zip'
volatilityURL = 'https://www1.nseindia.com/archives/nsccl/volt/CMVOLT_DATE1.CSV'

url = url.replace("DATE",date.upper())
futURL = futURL.replace("DATE",date.upper())
volatilityURL = volatilityURL.replace("DATE1",dateddmmyyyy)

eqZipFileName = os.path.join(os.path.expanduser('~'),'Desktop','Ananth shares','goodinvestory','EQBhav.zip')
futZipFileName = os.path.join(os.path.expanduser('~'),'Desktop','Ananth shares','goodinvestory','FUTBhav.zip')
volatilityFileName = os.path.join(os.path.expanduser('~'),'Desktop','Ananth shares','goodinvestory','Volatility.csv')
outpath = os.path.join(os.path.expanduser('~'),'Desktop','Ananth shares','goodinvestory')

req = requests.get(url)
file = open(eqZipFileName, 'wb')
for chunk in req.iter_content(100000):
    file.write(chunk)
file.close()
z=zipfile.ZipFile(eqZipFileName)
z.extractall(outpath)
z.close()

req = requests.get(futURL)
file = open(futZipFileName, 'wb')
for chunk in req.iter_content(100000):
    file.write(chunk)
file.close()
z=zipfile.ZipFile(futZipFileName)
z.extractall(outpath)
z.close()

req = requests.get(volatilityURL)
file = open(volatilityFileName, 'wb')
for chunk in req.iter_content(100000):
    file.write(chunk)
file.close()


#futFileName = 'C:\\Users\\KRISH\\Desktop\\Ananth shares\\goodinvestory\\foDATEbhav.csv'


