import sqlite3 as lite
import pandas as pd

def createtable():
    con = lite.connect('test.db')

    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
        cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
        cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
        cur.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
        cur.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
        cur.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
        cur.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
        cur.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
        cur.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")

def retrievedata():
    con = lite.connect('test.db')
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Cars")
        rows = cur.fetchall()

        for row in rows:
            print row

def pd_to_db():
    df = pd.read_csv(r'C:\Users\Phillip\Dropbox (Ring)\QA\Data Processing\Data\explorer\V2\0810\V2_1_6_76_stats.csv')
    df.to_sql(r'C:\Users\Phillip\Dropbox (Ring)\Source\SQL\statustest.db')

if __name__=='__main__':
    pd_to_db()