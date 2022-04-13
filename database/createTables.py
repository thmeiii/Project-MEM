#Will Delete All Tables and Insert Brand New Data from Excel

import sqlite3
from tkinter import COMMAND
import backEnd
import pandas as pd
import numpy as np

conn = sqlite3.connect(backEnd.DATABASE_PATH)
membersListFilePath = r"C:\Users\KI PC\OneDrive\Documents\Software Engineering and Computer Science\CS Bachelor in Ryerson\[4] Year 2 Semester 2\CPS406 - Software Engineering I\Assignments\Assignment3\database\membersList.xls"

#drop existing table
command = '''
DROP TABLE IF EXISTS memberList
'''
backEnd.runCommand(command)

#add table
command = '''
CREATE TABLE IF NOT EXISTS memberList(
  id int PRIMARY KEY,
  memberType varchar(255),
  firstName varchar(255),
  lastName varchar(255),
  phoneNumber int,
  email varchar(255)
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
print(readMemberList.head())
