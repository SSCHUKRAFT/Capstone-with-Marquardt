import os
import matplotlib.pyplot as pl
import pandas as pd
import plotly.express as px
import numpy as np
import mysql.connector

db = mysql.connector.connect(
    user = 'root',
    password = 'password',
    host = 'localhost',
    database = 'pmdci_db',
    auth_plugin='mysql_native_password'
)
cursor = db.cursor()

query = "SELECT id, passedCount, failedCount, retestedCount, downtime, cycletime, errorCode, downtimeDesc FROM data_entry"
cursor.execute(query)

allData = cursor.fetchall() #Get all data

#Store all data in arrays
all_id = []
all_passed = []
all_failed = []
all_retested = []
all_downtime = []
all_cycletime = []
all_errorCodes = []
all_downtimeDesc = []
for id, passedCount, failedCount, retestedCount, downtime, cycletime, errorCode, downtimeDesc in allData:
    all_id.append(id)
    all_passed.append(passedCount)
    all_failed.append(failedCount)
    all_retested.append(retestedCount)
    all_downtime.append(downtime)
    all_cycletime.append(cycletime)
    all_errorCodes.append(errorCode)
    all_downtimeDesc.append(downtimeDesc)

dic = {'id: ': all_id, 'passedCount': all_passed, 'failedCount': all_failed, 'retestedCount': all_retested, 'downtime': all_downtime, 'cycletime': all_cycletime, 'errorCode': all_errorCodes, 'downtimeDesc': all_downtimeDesc}
data_frame = pd.DataFrame(dic)
df_csv = data_frame.to_csv('databaseCsv/pmdci_data.csv')
