import requests
import zipfile
import datetime
import tkinter

class simpleapp_tk(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.entry = tkinter.Entry(self)
        self.entry.grid(column=0,row=0,sticky='EW')

        button = tkinter.Button(self,text=u"Calculate !")
        button.grid(column=1,row=0)

        label = tkinter.Label(self,anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')

        self.grid_columnconfigure(0,weight=1)


if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('goodinvestory options')

    app.mainloop()
        

date = datetime.datetime.now().strftime("%d%b%Y")
dateddmmyyyy = datetime.datetime.now().strftime("%d%m%Y")

url = 'https://www.nseindia.com/content/historical/EQUITIES/2017/JUN/cmDATEbhav.csv.zip'
futURL = 'https://www.nseindia.com/content/historical/DERIVATIVES/2017/JUN/foDATEbhav.csv.zip'
volatilityURL = 'https://www1.nseindia.com/archives/nsccl/volt/CMVOLT_DATE1.CSV'

url = url.replace("DATE",date.upper())
futURL = futURL.replace("DATE",date.upper())
volatilityURL = futURL.replace("DATE1",dateddmmyyyy)
eqZipFileName = 'C:\\Users\\KRISH\\Desktop\\Ananth shares\\goodinvestory\\EQBhav.zip'
futZipFileName = 'C:\\Users\\KRISH\\Desktop\\Ananth shares\\goodinvestory\\FUTBhav.zip'
volatilityFileName = 'C:\\Users\\KRISH\\Desktop\\Ananth shares\\goodinvestory\\Volatility.csv'
outpath = 'C:\\Users\\KRISH\\Desktop\\Ananth shares\\goodinvestory'

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


