import csv, sqlite3

import datetime

date = datetime.datetime.now().strftime("%d%b%Y")

eqFileName = 'C:\\Users\\KRISH\\Desktop\\Ananth shares\\goodinvestory\\foDATEbhav.csv'  
eqFileName = eqFileName.replace("DATE",date.upper())

con = sqlite3.connect("sqlite3\\goodinvestory.db")

# TO CHECK IF THERE ARE ANY TABLES IN THE DATABASE
#for row in con.execute("pragma table_info('sqlite_master')").fetchall():
#    print(row)

con.execute("DELETE FROM options")

#cur.execute("CREATE TABLE t (col1, col2);") # use your column names here
with open (eqFileName, 'r') as f:
    reader = csv.reader(f)
    columns = next(reader) 
    query = 'insert into options({0}) values ({1})'
    query = query.format(','.join(columns), ','.join('?' * (len(columns))))
    query = query.replace(',)',',EMPTY)')
    #print(query)
    cur = con.cursor()
    for data in reader:
        #print(data)
        cur.execute(query, data)

con.commit()
#delete query for removing futures and any index options
c=con.cursor()
#data = str()
exec = c.execute("DELETE FROM options WHERE INSTRUMENT <> ?",("OPTSTK",))
con.commit()

con.close()




