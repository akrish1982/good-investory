import csv, sqlite3

import datetime

date = datetime.datetime.now().strftime("%d-%b-%Y")
print(date)
data = [date.upper()]
data1 = [date.upper(),date.upper(),'OPTSTK']

#eqFileName = 'C:\\Users\\KRISH\\Desktop\\Ananth shares\\goodinvestory\\foDATEbhav.csv'  
#eqFileName = eqFileName.replace("DATE",date.upper())

con = sqlite3.connect("sqlite3\\goodinvestory.db")

#
sql1 = ''' UPDATE options
          SET 
          LOT_SIZE = (SELECT MARKET_LOTS.JUN_17 from MARKET_LOTS where MARKET_LOTS.SYMBOL = options.SYMBOL)
          where exists(
            SELECT * from MARKET_LOTS where MARKET_LOTS.SYMBOL = options.SYMBOL and options.timestamp = ?
          )'''

sql2 = ''' UPDATE options
SET premium = LOT_SIZE * CLOSE
where timestamp = ?'''


sql3 = ''' UPDATE options
SET 
    underlying_price = (SELECT stocks.close from stocks where stocks.SYMBOL = options.SYMBOL and stocks.TIMESTAMP = ?)
where exists(
    SELECT options.SYMBOL from stocks where stocks.SYMBOL = options.SYMBOL
    AND options.timestamp = ?
    AND options.INSTRUMENT= ?
)'''


sql4 = ''' UPDATE options
    set percent_move = 100*(underlying_price - strike_pr - close)/underlying_price
where underlying_price is not NULL
        and timestamp = ? '''

cur=con.cursor()
cur.execute(sql1,data)
cur.execute(sql2,data)
cur.execute(sql3,data1)
cur.execute(sql4,data)


con.commit()
con.close()
