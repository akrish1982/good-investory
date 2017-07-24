import csv, sqlite3

import datetime

#date = datetime.datetime.now().strftime("%d%m%Y")

eqFileName = 'C:\\Users\\KRISH\\Desktop\\Ananth shares\\goodinvestory\\volatility.csv'  
#eqFileName = eqFileName.replace("DATE",date)

con = sqlite3.connect("sqlite3\\goodinvestory.db")

# TO CHECK IF THERE ARE ANY TABLES IN THE DATABASE
#for row in con.execute("pragma table_info('sqlite_master')").fetchall():
#    print(row)

con.execute("DELETE FROM volatility")

#cur.execute("CREATE TABLE t (col1, col2);") # use your column names here

with open (eqFileName, 'r') as f:
    reader = csv.reader(f)
    columns = next(reader) 
    query = 'INSERT INTO volatility (Date,Symbol,close,prev_close,log_returns,' \
            'Previous_Day_Volatility,Current_Day_Underlying_Daily_Volatility,Annualised_Volatility)' \
            'values (?,?,?,?,?,?,?,?)'
    #query = query.format(','.join(columns), ','.join('?' * (len(columns))))
    #query = query.replace(',)',',EMPTY)')
    print(query)
    cur = con.cursor()
    for data in reader:
        print(data)
        cur.execute(query, data)


con.commit()

con.close()





