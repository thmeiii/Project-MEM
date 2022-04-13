#Will Delete All Tables and Insert Brand New Data from Excel
import sys
import sqlite3
import backEnd
import pandas as pd
import numpy as np

#establish connection
conn = sqlite3.connect(backEnd.DATABASE_PATH) 
membersListFilePath = "membersList.xls"

#drop existing table
command = '''
DROP TABLE IF EXISTS memberList
'''
backEnd.runCommand(command)

#add table
command = '''
CREATE TABLE IF NOT EXISTS memberList(
  id int,
  memberType varchar(255),
  firstName varchar(255),
  lastName varchar(255),
  password varchar(255),
  phoneNumber int,
  email varchar(255),
  PRIMARY KEY (id)
  );
'''
backEnd.runCommand(command)

#insert data into table
memberList = pd.read_excel(membersListFilePath, index_col = 0)
memberList.to_sql('memberList', conn, if_exists = 'append', index_label = 'id')

#read data from table
command = '''
SELECT *
FROM memberList;
'''

# print(backEnd.showTables()) #to see list of tables
readMemberList = backEnd.runQuery(command)
print(readMemberList.head(5)) #print the first 5 row of dataframe