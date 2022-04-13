import sqlite3
import pandas as pd
import numpy as np

DATABASE_PATH = "database.db"

#use for reading tables
def runQuery (q):
    with sqlite3.connect (DATABASE_PATH) as conn:
        return pd.read_sql (q,conn)

#use for   
def runCommand (c):
    with sqlite3.connect (DATABASE_PATH) as conn:
        conn.isolation_level = None
        conn.execute (c)

def showTables ():
    q = '''
    SELECT
        name,
        type
    FROM sqlite_master
    WHERE type IN ("table","view")
    '''
    return runQuery (q)