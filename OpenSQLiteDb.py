from IPython.core.display import display, HTML
display(HTML("<style>.container { width:80% !important; }</style>"))

import pandas as pd
#pd.set_option('display.max_columns',15)
desired_width = 320
pd.set_option('display.width', desired_width)
table = pd.DataFrame()

import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        conn = sqlite3.connect('D:\\ProgramFiles\\Programming\\Db_files\\ttcs.db')
        return conn
    except Error:
        #print(Error)
        print("There was an error!")


#conn = sql_connection()
conn = sqlite3.connect('D:\\ProgramFiles\\Programming\\Db_files\\ttcs.db')
#cursorObj = conn.cursor()

pd.set_option('display.max_columns',15)
table = pd.DataFrame()

tname = 'teammembers'
sstring = 'chris'

#query = "Select * from " + tname + " where FLGACS = %" + sstring + "%"
        #Select * from  TeamMembers where FLGACS like 'George%'
#query = "Select * from " + tname + " where FLGACS like " + "'%" + sstring + "%'"
#query = "Select * from combinedresults"
#dbquery = pd.read_sql_query(query, conn)
#print(dbquery.head())


query = ('select Race, Dis, First_Name, Last_Name, Gender, Age, Team, FinalPoints from CombinedResults ' \
        'where SearchString in (Select SearchString from Combinedresults group by SearchString having count(*) > 1)' \
        'and Team is not null ' \
        'order by Last_Name, First_Name')
dbquery = pd.read_sql_query(query, conn)
#print(dbquery.head())
print(dbquery)
