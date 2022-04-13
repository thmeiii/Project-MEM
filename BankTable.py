import sqlite3
import backEnd
import pandas as pd
import numpy as np
import datetime

conn = sqlite3.connect(backEnd.DATABASE_PATH)
BankFilePath = r"/Users/hienle/Desktop/CPS406/MEM/Bank.xlsx"

#drop existing table
command = '''
DROP TABLE IF EXISTS bank
'''
backEnd.runCommand(command)

#add table
command = '''
CREATE TABLE IF NOT EXISTS bank(
  id int,
  date just_date,
  amount double,
  paymentReason varchar(255),
  memberID int,
  PRIMARY KEY (id)
  );
'''
backEnd.runCommand(command)

#insert data into table
Bank = pd.read_excel(BankFilePath, index_col = 0)
Bank.to_sql('bank', conn, if_exists = 'append', index_label = 'id')

#read data from table
command = '''
SELECT *
FROM bank;
'''
# print(backEnd.showTables()) #to see list of tables
readBank = backEnd.runQuery(command)
print(readBank.head(20)) #print the first 5 row of dataframe
