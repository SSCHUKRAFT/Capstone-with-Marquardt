import os
import shutil as sh
import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# arrays arrays for days

def dbstore(folder, legacyfolder):
    legacydata = os.listdir(legacyfolder)
    currentfile = "databaseCsv_" + str(datetime.date.today())
    if currentfile in legacydata:
        sh.copy2(folder + "/pmdci_passed_data.csv", legacyfolder + "/" + currentfile)
        sh.copy2(folder + "/pmdci_failed_data.csv", legacyfolder + "/" + currentfile)
        sh.copy2(folder + "/pmdci_downtime_data.csv", legacyfolder + "/" + currentfile)
        sh.copy2(folder + "/pmdci_retested_data.csv", legacyfolder + "/" + currentfile)
        sh.copy2(folder + "/pmdci_settings_data.csv", legacyfolder + "/" + currentfile)
        sh.copy2(folder + "/pmdci_employee_data.csv", legacyfolder + "/" + currentfile)
    else:
        os.mkdir(os.path.join(legacyfolder, currentfile))
        sh.copy2(folder + "/pmdci_passed_data.csv", legacyfolder + "/" + currentfile)
        sh.copy2(folder + "/pmdci_failed_data.csv", legacyfolder + "/" + currentfile)
        sh.copy2(folder + "/pmdci_downtime_data.csv", legacyfolder + "/" + currentfile)
        sh.copy2(folder + "/pmdci_retested_data.csv", legacyfolder + "/" + currentfile)
        sh.copy2(folder + "/pmdci_settings_data.csv", legacyfolder + "/" + currentfile)
        sh.copy2(folder + "/pmdci_employee_data.csv", legacyfolder + "/" + currentfile)
    print("Today's data has been backed up")

def grabdays(legacyfolder, timespan):
    days=[]
    x = 0
    if timespan <= os.listdir(legacyfolder).__len__():
        while x < timespan:
            days.append((legacyfolder + "/" "databaseCsv_" + str(datetime.date.today() - datetime.timedelta(days=x))))
            x = x + 1
    else:
        while x < os.listdir(legacyfolder).__len__():
            days.append((legacyfolder + "/" "databaseCsv_" + str(datetime.date.today() - datetime.timedelta(days=x))))
            x = x + 1
    return days

# Combines relevant data and creates a list Matrices
def mat(folder):
    TheL = []
    x = 0
    D = os.listdir(folder)
    while x < D.__len__():
        TheL.append(ar(open(folder+"/" + str(D[x])).readlines()))
        x = x + 1
    return TheL

# Creates Matrices
def ar(file):
    PPMArray = []
    x = 0
    i = 0
    pm = []
    while x < file.__len__():
        pm.append(file[x])
        x = x + 1
    while i < file.__len__():
        PPMArray.append(pm[i].split(','))
        i = i + 1
    return PPMArray

# Removes specific section
def column(matrix, col):
    ob = []
    x = 0
    while x < matrix.__len__():
        ob.append(matrix[x][col])
        x = x + 1
    return ob

def average(array):
    x = 0
    i = 0
    while x < array.__len__():
        i = i + array[x]
        x = x + 1
    i = i/array.__len__()
    return i

def combine(array1, array2):
    final = []
    x = 0
    if array1.__len__() < array2.__len__():
        while x < array1.__len__():
            final.append((array1[x] + array2[x]))
            x = x + 1
        while x < array2.__len__():
            final.append((array2[x]))
            x = x + 1
    elif array1.__len__() > array2.__len__():
        while x < array2.__len__():
            final.append((array1[x] + array2[x]))
            x = x + 1
        while x < array1.__len__():
            final.append((array1[x]))
            x = x + 1
    else:
        while x < array1.__len__():
            final.append((array1[x] + array2[x]))
            x = x + 1
    return final

def add(array):
    x = 0
    y = 0
    while x < array.__len__():
        y = y + array[x]
        x = x + 1
    return y

# Compares values
def compare(string, matrix):
    x = 0
    while x < matrix.__len__():
        if string == matrix[x]:
            return True
        else:
            x = x + 1

# Places an array matrices into categories, that are then organized by a positional condition
def sift(folder, position):
    data = mat(folder)[position]
    mach = [*set(column(data, (data[0].__len__()-3)))]
    mach.sort()
    final =[]
    x = 0
    while x < mach.__len__():
        final.append([])
        x = x + 1
    y = 0
    while data.__len__() != 0:
        while y < mach.__len__():
            z = 0
            while z < data.__len__():
                if data[z][data[0].__len__()-3] == mach[y]:
                    final[y].append(data[z])
                    data.remove(data[z])
                else:
                    z = z + 1
            y = y + 1
    i = 0
    while i < final.__len__():
        x = 0
        if final[i][x][0] == "":
            final.remove(final[i])
        i = i + 1
    return final

# Orders values
def org(ar, row, check):
    base = []
    x = 0
    while x < ar.__len__():
        if(ar[x][row] == check):
            base.append(ar[x])
        x = x + 1
    return base

# Combines line values
def consolidate(folder, position, extractval):
    temp = []
    final = []
    data = sift(folder, position)
    x = 0
    while x < data.__len__():
        temp.append(column(data[x], extractval))
        x = x + 1
    y = 0
    while y < temp.__len__():
        temp2 = []
        z = 0
        a = 0
        while z < temp[y].__len__():
            a = a + int(temp[y][z])
            temp2.append(a)
            z = z + 1
        final.append(temp2[temp2.__len__()-1])
        y = y + 1
    return final

# Calculate
def passthresholds(folder):
    x = 2
    final = []
    while x < 12:
        final.append(add(consolidate(folder, 5, x)))
        x = x + 1
    return final

def failthresholds(folder):
    x = 13
    final = []
    while x < 23:
        final.append(add(consolidate(folder, 5, x)))
        x = x + 1
    return final

def pt(legacyfolder, timespan):
    fol = grabdays(legacyfolder, timespan)
    x = 0
    final = []
    while x < fol.__len__():
        final.append(add(passthresholds(fol[x])))
        x = x + 1
    return final

def ft(legacyfolder, timespan):
    fol = grabdays(legacyfolder, timespan)
    x = 0
    final = []
    while x < fol.__len__():
        final.append(add(failthresholds(fol[x])))
        x = x + 1
    return final

def ppcalc(folder):
    p = consolidate(folder, 3, 1)
    r = consolidate(folder, 4, 1)
    results = combine(p, r)
    x = 0
    return results

def ftfcalc(folder):
    f = consolidate(folder, 2, 1)
    results = []
    x = 0
    while x < f.__len__():
        results.append(f[x])
        x = x + 1
    return results

def prodcalc(folder):
    x = 0
    te = passthresholds(folder)
    workhours = 10
    pdata = consolidate(folder, 3, 1)
    op = (workhours-.25) * pdata.__len__()
    values = []
    while x < pdata.__len__():
        tes = te[x]/1000*60
        st = (tes*pdata[x])/(3600)
        p = st/op
        values.append(p * 100)
        x = x + 1
    return values

def dtcalc(folder):
    dt = consolidate(folder, 0, 1)
    et = consolidate(folder, 0, 2)
    results = combine(dt, et)
    return results

def ftfcalcoverall(legacyfolder, timespan):
    fol = grabdays(legacyfolder, timespan)
    x = 0
    final = []
    while x < fol.__len__():
        final.append(add(ftfcalc(fol[x])))
        x = x + 1
    return final

def ppcalcoverall(legacyfolder, timespan):
    fol = grabdays(legacyfolder, timespan)
    x = 0
    final = []
    while x < fol.__len__():
        final.append(add(ppcalc(fol[x])))
        x = x + 1
    return final

def prodcalcoverall(legacyfolder, timespan):
    fol = grabdays(legacyfolder, timespan)
    x = 0
    final = []
    while x < fol.__len__():
        final.append(average(prodcalc(fol[x])))
        x = x + 1
    return final

def dtcalcoverall(legacyfolder, timespan):
    fol = grabdays(legacyfolder, timespan)
    x = 0
    final = []
    while x < fol.__len__():
        final.append(average(consolidate(fol[x], 0, 1)))
        x = x + 1
    return final

def escalcoverall(legacyfolder, timespan):
    fol = grabdays(legacyfolder, timespan)
    x = 0
    final = []
    while x < fol.__len__():
        final.append(average(consolidate(fol[x], 0, 2)))
        x = x + 1
    return final

# This measure is a percentage based on “Operator Hours” vs “Productive Hours”
# Operator Hours are the total number of hours booked to a line times the number of operators
# Productive Hours are a relationship of total parts made vs the takt time
# Graph

def ppmcalcall(folderar):
    x = 0
    collection = []
    final = []
    while x < folderar.__len__():
        collection.append(ftfcalc(folderar[x]))
        x = x + 1
    y = 0
    while y < folderar.__len__():
        final.append(add(collection[y]))
        y = y + 1
    return final

def prodcalcall(folderar, tear):
    x = 0
    collection = []
    final = []
    while x < folderar.__len__():
        collection.append(prodcalc(folderar[x], tear[x]))
        x = x + 1
    y = 0
    while y < folderar.__len__():
        final.append(average(collection[y]))
        y = y + 1
    return final

def dtcalcall(folderar):
    x = 0
    collection = []
    final = []
    while x < folderar.__len__():
        collection.append(dtcalc(folderar[x]))
        x = x + 1
    y = 0
    while y < folderar.__len__():
        final.append(average(collection[y]))
        y = y + 1
    return final

def ftfgraphar(folderar):
    labels = []
    i = 0
    results = ppmcalcall(folderar)
    while i < results.__len__():
        labels.append("Floor " + str(i+1))
        i = i + 1
    fig = go.Figure(data=[go.Bar(x=labels, y=results, text=results, textposition='auto')])
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', autosize= False, width=840, height=600)
    fig.update_layout(title="Collective PPM", title_font_color="white")
    fig.update_xaxes(color='white')
    fig.update_yaxes(color='white')
    fig.write_image("static/img/ppm.png")
    print("ppm updated")

def prodgraphar(folderar, tear):
    labels = []
    i = 0
    temp = folderar
    while i < temp.__len__():
        labels.append("Floor " + str(i+1))
        i = i + 1
    x = 0
    y = prodcalcall(folderar, tear)
    temp = []
    while x < y.__len__():
        temp.append(str(round(y[x], 2)) + "%")
        x = x + 1
    fig = go.Figure(data=[go.Table(header=dict(values=["Machine", 'Productivity']),
                                   cells=dict(
                                       values=[labels, temp],
                                       font_color=['rgb(0, 0, 0)',
                                                   ['rgba(0,172,32, 0.8)' if val >= 85 else 'rgba(175,5,0, 0.8)' for val
                                                    in y]]
                                   ))])
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    fig.update_layout(title="Collective Productivity", title_font_color="white")
    fig.update_xaxes(color='white')
    fig.update_yaxes(color='white')
    fig.write_image("static/img/pro.png")
    print("productivity updated")

def dtgraphar(folderar):
    labels = []
    i = 0
    temp = folderar
    while i < temp.__len__():
        labels.append("Floor " + str(i+1))
        i = i + 1
    x = 0
    r = 0
    l = 0
    ty = []
    tw = []
    y = []
    w = []
    z = []
    while r < temp.__len__():
        ty.append(consolidate(folderar[r], 0, 1))
        tw.append(consolidate(folderar[r], 0, 2))
        r = r + 1
    while l < tw.__len__():
        y.append(round(average(ty[l])))
        w.append(round(average(tw[l])))
        l = l + 1
    while x < y.__len__():
        labels.append("Op " + str(x + 1))
        z.append(600 - y[x] - w[x])
        x = x + 1
    fig = go.Figure(
        data=[go.Bar(name="Remaining time", marker_color='rgb(0,172,23)', x=labels, y=z, text=z, textposition='auto'),
              go.Bar(name="Escalation time", marker_color='rgb(227,234,0)', x=labels, y=w, text=w, textposition='auto'),
              go.Bar(name="Downtime", marker_color='rgb(175,5,0)', x=labels, y=y, text=y, textposition='auto'),
              ])
    fig.update_xaxes(color='white')
    fig.update_yaxes(color='white')
    fig.update_layout(title="Collective Downtime", title_font_color="white", barmode='stack')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', autosize= False, width=840, height=600)
    fig.update_traces(marker_line_color='rgb(8,48,107)')
    fig.write_image("static/img/dt.png")
    print("downtime update")

def collectivear(folderar, tear):
    ftfgraphar(folderar)
    prodgraphar(folderar, tear)
    dtgraphar(folderar)

def ftfgraph(legacyfolder, timespan):
    p = ppcalcoverall(legacyfolder, timespan)
    f = ftfcalcoverall(legacyfolder, timespan)
    ptt = pt(legacyfolder, timespan)
    ftt = ft(legacyfolder, timespan)
    temp = grabdays(legacyfolder, timespan)
    exp = []
    exp2 = []
    x = 0
    labels = []
    while x < temp.__len__():
        labels.append(temp[x][temp[x].__len__()-8:temp[x].__len__()])
        exp.append(p[x]-average(p))
        exp2.append(f[x] + average(f))
        x = x + 1
    i = 0
    while i < exp.__len__():
        if exp[i] < 0:
            exp[i] = 0
        i = i + 1
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=labels, y=ptt, text=ptt, line_color='rgb(0,200,0)', name="Expected Throughput"))
    fig.add_trace(go.Scatter(x=labels, y=ftt, text=ftt, line_color='rgb(200,0,0)', name="Expected Failed"), secondary_y=True)
    fig.add_trace(go.Scatter(x=labels, y=p, text=p, line_color='rgb(0,100,0)', name="Actual Throughput"))
    fig.add_trace(go.Scatter(x=labels, y=exp, text=p, line_color='rgba(0,0,0,0)', showlegend=False))
    fig.add_trace(go.Scatter(x=labels, y=exp2, text=p, line_color='rgba(0,0,0,0)', showlegend=False), secondary_y=True)
    fig.add_trace(go.Scatter(x=labels, y=f, text=f, line_color='rgb(100,0,0)', name="Actual Failed"), secondary_y=True)
    fig.update_layout(title="First Time Failures & Total Throughput", title_font_color="white", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', autosize=False, width=840,
                      height=600)
    fig.update_layout(legend=dict(font=dict(color="white")))
    fig.update_xaxes(color='white')
    fig.update_yaxes(color='white', title="Throughput")
    fig.update_yaxes(gridcolor='rgb(50,50,50)', title="Failed", secondary_y=True)
    fig.update_yaxes(rangemode='tozero', constraintoward='bottom')
    fig.update_yaxes(rangemode='tozero', constraintoward='bottom', secondary_y=True)
    fig.write_image("static/img/ppm.png")
    print("parts updated")

def prodgraph(legacyfolder, timespan):
    p = prodcalcoverall(legacyfolder, timespan)
    temp = grabdays(legacyfolder, timespan)
    x = 0
    labels = []
    hun = []
    eighty = []
    while x < temp.__len__():
        labels.append(temp[x][temp[x].__len__()-8:temp[x].__len__()])
        hun.append(100)
        eighty.append(85)
        x = x + 1
    fig = make_subplots()
    fig.add_trace(go.Scatter(x=labels, y=p, text=p, line_color='rgb(0,0,150)', name="Productivity", showlegend=False))
    fig.add_trace(go.Scatter(x=labels, y=hun, line_color='rgb(0,150,0)', name="100% Productivity"))
    fig.add_trace(go.Scatter(x=labels, y=eighty, line_color='rgb(150,0,0)', name="85% Productivity"))
    fig.update_layout(title="Productivity", title_font_color="white", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', autosize=False, width=840,
                      height=600)
    fig.update_layout(legend=dict(font=dict(color="white")))
    fig.update_xaxes(color='white')
    fig.update_yaxes(color='white')
    fig.write_image("static/img/pro.png")
    print("Productivity updated")

def dtgraph(legacyfolder, timespan):
    p = dtcalcoverall(legacyfolder, timespan)
    e = escalcoverall(legacyfolder, timespan)
    temp = grabdays(legacyfolder, timespan)
    x = 0
    labels = []
    while x < temp.__len__():
        labels.append(temp[x][temp[x].__len__()-8:temp[x].__len__()])
        x = x + 1
    fig = make_subplots()
    fig.add_trace(go.Scatter(x=labels, y=p, text=p, line_color='rgb(0,0,150)', name="Downtime"))
    fig.add_trace(go.Scatter(x=labels, y=e, text=e, line_color='rgb(150,75,50)', name="Escalation time"))
    fig.update_layout(title="Downtime", title_font_color="white", paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)', autosize=False, width=840,
                      height=600)
    fig.update_layout(legend=dict(font=dict(color="white")))
    fig.update_xaxes(color='white')
    fig.update_yaxes(color='white')
    fig.write_image("static/img/dt.png")
    print("Downtime updated")

def collective(folder, time):
    ftfgraph(folder, time)
    prodgraph(folder, time)
    dtgraph(folder, time)

if __name__ == '__main__':
    a = ["databaseCsv", "databaseCsvtest"]
    c = ["legacyDatabases", "legacyDatabasestest"]
    dbstore(a[0], "legacyDatabases")
    dbstore(a[1], "legacyDatabasestest")
    ftfgraph(c[0], 10)
    print(prodcalc("legacyDatabases/databaseCsv_2022-11-10"))
    #collective(c[0], b[1], 10)