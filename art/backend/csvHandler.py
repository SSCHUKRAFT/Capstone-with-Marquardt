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

passedQuery = "SELECT * FROM passed_data_entry"
failedQuery = "SELECT * FROM failed_data_entry"
retestedQuery = "SELECT * FROM retested_data_entry"
downtimeQuery = "SELECT * FROM downtime_data_entry"
employeesQuery = "SELECT * FROM employees";
settingsQuery = "SELECT * FROM data_collection_settings";

#Store all data in arrays
all_passed = []
all_failed = []
all_retested = []
all_downtime = []
all_esclTime = []
all_errorCode = []
all_description = []
all_passed_machine = []
all_failed_machine = []
all_retested_machine = []
all_downtime_machine = []
all_passed_employeeID = []
all_failed_employeeID = []
all_retested_employeeID = []
all_downtime_employeeID = []
all_passed_timestamp = []
all_failed_timestamp = []
all_retested_timestamp = []
all_downtime_timestamp = []
all_employee_id = []
all_employee_name = []
all_employeePosition = []
all_partFamily = []
all_expectedPassed = []
all_expectedFailed = []
all_ucl = []

passedCursor = db.cursor()
passedCursor.execute(passedQuery)
allPassedData = passedCursor.fetchall() #Get all passed data

# for passedCount, machine, employeeID, timestamp in allPassedData:
#     all_passed.append(passedCount)
#     all_passed_machine.append(machine)
#     all_passed_employeeID.append(employeeID)
#     all_passed_timestamp.append(timestamp)

# passedDic = {'passedCount': all_passed, 'machine': all_passed_machine, 'employeeID': all_passed_employeeID, "timestamp": all_passed_timestamp}
# passed_data_frame = pd.DataFrame(passedDic)
# df_csv = passed_data_frame.to_csv('databaseCsv/pmdci_passed_data.csv')

# passedCursor.close()

# failedCursor = db.cursor()
# failedCursor.execute(failedQuery)
# allFailedData = failedCursor.fetchall() #Get all failed data

# for failedCount, machine, employeeID, timestamp in allFailedData:
#     all_failed.append(failedCount)
#     all_failed_machine.append(machine)
#     all_failed_employeeID.append(employeeID)
#     all_failed_timestamp.append(timestamp)

# failedDic = {'failedCount': all_failed, 'machine': all_failed_machine, 'employeeID': all_failed_employeeID, "timestamp": all_failed_timestamp}
# failed_data_frame = pd.DataFrame(failedDic)
# df_csv = failed_data_frame.to_csv('databaseCsv/pmdci_failed_data.csv')

# failedCursor.close()

# retestedCursor = db.cursor()
# retestedCursor.execute(retestedQuery)
# allRetestedData = retestedCursor.fetchall() #Get all retested data

# for retestedCount, machine, employeeID, timestamp in allRetestedData:
#     all_retested.append(retestedCount)
#     all_retested_machine.append(machine)
#     all_retested_employeeID.append(employeeID)
#     all_retested_timestamp.append(timestamp)

# retestedDic = {'retestedCount': all_retested, 'machine': all_retested_machine, 'employeeID': all_retested_employeeID, "timestamp": all_retested_timestamp}
# retested_data_frame = pd.DataFrame(retestedDic)
# df_csv = retested_data_frame.to_csv('databaseCsv/pmdci_retested_data.csv')

# retestedCursor.close()

# downtimeCursor = db.cursor()
# downtimeCursor.execute(downtimeQuery)
# allDowntimeData = downtimeCursor.fetchall() #Get all downtime data

# for downtime, esclTime, errorCode, description, machine, employeeID, timestamp in allDowntimeData:
#     all_downtime.append(downtime)
#     all_esclTime.append(esclTime)
#     all_errorCode.append(errorCode)
#     all_description.append(description)
#     all_downtime_machine.append(machine)
#     all_downtime_employeeID.append(employeeID)
#     all_downtime_timestamp.append(timestamp)

# downtimeDic = {'downtime': all_downtime, 'escalation time': all_esclTime, 'error code': all_errorCode, 'description': all_description, 'machine': all_passed_machine, 'employeeID': all_passed_employeeID, "timestamp": all_passed_timestamp}
# downtime_data_frame = pd.DataFrame(downtimeDic)
# df_csv = downtime_data_frame.to_csv('databaseCsv/pmdci_downtime_data.csv')

# downtimeCursor.close()

employeesCursor = db.cursor()
employeesCursor.execute(employeesQuery)
allEmployeeData = employeesCursor.fetchall() #Get all employee data

for id, employeeID, employeeName, position in allEmployeeData:
    all_employee_id.append(employeeID)
    all_employee_name.append(employeeName)
    all_employeePosition.append(position)

employeeDic = {'employeeID': all_employee_id, 'employeeName': all_employee_name, 'position': all_employeePosition}
employee_data_frame = pd.DataFrame(employeeDic)
df_csv = employee_data_frame.to_csv('databaseCsv/pmdci_employee_data.csv')

employeesCursor.close()

settingsCursor = db.cursor()
settingsCursor.execute(settingsQuery)
allSettingsData = settingsCursor.fetchall() #Get all machine settings

for partFamily, expectedPassed, expectedFailed, ucl in allSettingsData:
    all_partFamily.append(partFamily)
    all_expectedPassed.append(expectedPassed)
    all_expectedFailed.append(expectedFailed)
    all_ucl.append(ucl)

settingsDic = {'partFamily': all_partFamily, 'expectedPassed': all_expectedPassed, 'expectedFailed': all_expectedFailed, 'ucl': all_ucl}
settings_data_frame = pd.DataFrame(settingsDic)
df_csv = settings_data_frame.to_csv('databaseCsv/pmdci_settings_data.csv')

employeesCursor.close()
