import os
import matplotlib.pyplot as pl
import pandas as pd
import plotly.express as px
import numpy as np
import mysql.connector
import sys
import csv

db = mysql.connector.connect(
    user = 'root',
    password = 'password',
    host = 'localhost',
    database = 'pmdci_db',
    auth_plugin='mysql_native_password'
)
cursor = db.cursor()

query = "SELECT id, passedCount, failedCount from data_entry"
cursor.execute(query)

allData = cursor.fetchall() #Get all data

#Store all data in arrays
all_id = []
all_passed = []
all_failed = []
for id, passedCount, failedCount in allData:
    all_id.append(id)
    all_passed.append(passedCount)
    all_failed.append(failedCount)

dic = {'id: ': all_id, 'passedCount: ': all_passed, 'failedCount': all_failed}
data_frame = pd.DataFrame(dic)
df_csv = data_frame.to_csv('databaseCsv/pmdci_data.csv')
