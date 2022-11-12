import os
import shutil as sh
import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# arrays arrays for days

def dbstore():
    legacydata = os.listdir("legacyDatabases")
    currentfile = "databaseCsv_" + str(datetime.date.today())
    if currentfile in legacydata:
        return None
    else:
        os.mkdir(os.path.join("legacyDatabases", currentfile))
    sh.copy2("databaseCsv/pmdci_passed_data.csv", "legacyDatabases/" + currentfile)
    sh.copy2("databaseCsv/pmdci_failed_data.csv", "legacyDatabases/" + currentfile)
    sh.copy2("databaseCsv/pmdci_downtime_data.csv", "legacyDatabases/" + currentfile)
    sh.copy2("databaseCsv/pmdci_retested_data.csv", "legacyDatabases/" + currentfile)
    print("Today's data has been backed up")

def grabdays(legacyfolder, timespan):
    days=[]
    x = 0
    while x < timespan:
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
    while x < array1.__len__():
        final.append((array1[x]+array2[x]))
        x = x + 1
    return final

def ochange(array):
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
# respect weight of values.
def ppcalc(folder):
    p = consolidate(folder, 2, 1)
    r = consolidate(folder, 3, 1)
    good = combine(p, r)
    results = []
    x = 0
    while x < good.__len__():
        results.append(p[x]+r[x])
        x = x + 1
    return results

def ftfcalc(folder):
    f = consolidate(folder, 1, 1)
    results = []
    x = 0
    while x < f.__len__():
        results.append(f[x])
        x = x + 1
    return results

def ftfcalcoverall(legacyfolder, timespan):
    fol = grabdays(legacyfolder, timespan)
    x = 0
    final = []
    while x < fol.__len__():
        final.append(ochange(ftfcalc(fol[x])))
        x = x + 1
    return final

def ppcalcoverall(legacyfolder, timespan):
    fol = grabdays(legacyfolder, timespan)
    x = 0
    final = []
    while x < fol.__len__():
        final.append(ochange(ppcalc(fol[x])))
        x = x + 1
    return final

# This measure is a percentage based on “Operator Hours” vs “Productive Hours”
# Operator Hours are the total number of hours booked to a line times the number of operators
# Productive Hours are a relationship of total parts made vs the takt time
def prodcalc(folder, te):
    x = 0
    workhours = 10
    pdata = consolidate(folder, 2, 1)
    op = (workhours-.25) * pdata.__len__()
    values = []
    while x < pdata.__len__():
        tes = te[x]/1000*60
        st = (tes*pdata[x])/(3600)
        p = st/op
        values.append(p * 100)
        x = x + 1
    return values

def ttcalc(folder):
    f = consolidate(folder, 1, 1)
    p = consolidate(folder, 2, 1)
    r = consolidate(folder, 3, 1)
    return [ochange(p), ochange(r), ochange(f)]

def dtcalc(folder):
    dt = consolidate(folder, 0, 1)
    et = consolidate(folder, 0, 2)
    results = combine(dt, et)
    return results

# Graph
def ftfgraph(folder):
    data = mat(folder)[2]
    labels = [*set(column(data, (data[0].__len__() - 3)))]
    labels.remove("machine")
    temp = ftfcalc(folder)
    results = []
    x = 0
    while x < temp.__len__():
        results.append(str(round(temp[x], 2)))
        x = x + 1
    fig = go.Figure(data=[go.Bar(x=labels, y=temp, text=results, textposition='auto')])
    fig.update_layout( paper_bgcolor= 'rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', autosize= False, width=840, height=600)
    fig.update_layout(title="PPM", title_font_color="white")
    fig.update_xaxes(color='white')
    fig.update_yaxes(color='white')
    fig.write_image("static/img/ppm.png")
    print("ppm updated")

def prodgraph(folder, te):
    data = mat(folder)[2]
    labels = [*set(column(data, (data[0].__len__() - 3)))]
    labels.remove("machine")
    x = 0
    y = prodcalc(folder, te)
    temp = []
    while x < y.__len__():
        temp.append(str(round(y[x], 2))+"%")
        x = x + 1
    fig = go.Figure(data=[go.Table(header=dict(values=["Machine", 'Productivity']),
                                   cells=dict(
                                       values=[labels, temp],
                                       font_color= ['rgb(0, 0, 0)',
                                        ['rgba(0,172,32, 0.8)' if val >= 85 else 'rgba(175,5,0, 0.8)' for val in y] ]
                                   ))])
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    fig.update_layout(title="Productivity", title_font_color="white")
    fig.write_image("static/img/pro.png")
    print("productivity updated")

def ttgraph(folder):
    data = mat(folder)[2]
    labels = [*set(column(data, (data[0].__len__() - 3)))]
    labels.remove("machine")
    f = consolidate(folder, 1, 1)
    p = consolidate(folder, 2, 1)
    r = consolidate(folder, 3, 1)
    fig = go.Figure(data=[go.Bar(name="Passed", marker_color='rgb(0,172,32)', x=labels, y=p, text=p, textposition='auto'),
                          go.Bar(name="ReTested", marker_color='rgb(0,32,172)', x=labels, y=r, text=r, textposition='auto'),
                          go.Bar(name="Failed", marker_color='rgb(175,5,0)', x=labels, y=f, text=f, textposition='auto')])
    fig.update_layout(title="Total Throughput", title_font_color="white", barmode='stack')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', autosize= False, width=840, height=600)
    fig.update_traces(marker_line_color='rgb(8,48,107)')
    fig.update_xaxes(color='white')
    fig.update_yaxes(color='white')
    fig.write_image("static/img/tt.png")
    print("Total Throughput updated")

def dtgraph(folder):
    data = mat(folder)[0]
    labels = [*set(column(data, (data[0].__len__()-3)))]
    labels.remove("machine")
    x = 0
    y = consolidate(folder, 0, 1)
    w = consolidate(folder, 0, 2)
    z = []
    while x < y.__len__():
        labels.append("Op "+str(x+1))
        z.append(600-y[x]-w[x])
        x = x + 1
    fig = go.Figure(data=[go.Bar(name="Remaining time", marker_color='rgb(0,172,23)', x=labels, y=z, text=z, textposition='auto'),
                          go.Bar(name="Escalation time", marker_color='rgb(227,234,0)', x=labels, y=w, text=w, textposition='auto'),
                          go.Bar(name="Downtime", marker_color='rgb(175,5,0)', x=labels, y=y, text=y, textposition='auto'),
                          ])
    fig.update_layout(title="Downtime", title_font_color="white", barmode='stack')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', autosize= False, width=840, height=600)
    fig.update_traces(marker_line_color='rgb(8,48,107)')
    fig.update_xaxes(color='white')
    fig.update_yaxes(color='white')
    fig.write_image("static/img/dt.png")
    print("downtime update")

def collective(folder, te):
    ftfgraph(folder)
    prodgraph(folder, te)
    ttgraph(folder)
    dtgraph(folder)

def ppmcalcall(folderar):
    x = 0
    collection = []
    final = []
    while x < folderar.__len__():
        collection.append(ftfcalc(folderar[x]))
        x = x + 1
    y = 0
    while y < folderar.__len__():
        final.append(ochange(collection[y]))
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

def ttcalcall(folderar):
    x = 0
    collection = []
    final =[]
    while x < folderar.__len__():
        collection.append(ttcalc(folderar[x]))
        x = x + 1
    y = 1
    i = 0
    while y < folderar.__len__():
        final = combine(collection[i], collection[y])
        y = y + 1
        i = i + 1
    return [collection, final]

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

def ttgraphar(folderar):
    labels = []
    i = 0
    temp = folderar
    while i < temp.__len__():
        labels.append("Floor " + str(i+1))
        i = i + 1
    data = ttcalcall(folderar)[0]
    p = column(data, 0)
    r = column(data, 1)
    f = column(data, 2)
    fig = go.Figure(
        data=[go.Bar(name="Passed", marker_color='rgb(0,172,32)', x=labels, y=p, text=p, textposition='auto'),
              go.Bar(name="ReTested", marker_color='rgb(0,32,172)', x=labels, y=r, text=r, textposition='auto'),
              go.Bar(name="Failed", marker_color='rgb(175,5,0)', x=labels, y=f, text=f, textposition='auto')])
    fig.update_layout(title="Collective Total Throughput", title_font_color="white", barmode='stack')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', autosize= False, width=840, height=600)
    fig.update_traces(marker_line_color='rgb(8,48,107)')
    fig.update_xaxes(color='white')
    fig.update_yaxes(color='white')
    fig.write_image("static/img/tt.png")
    print("Total Throughput updated")

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
    ttgraphar(folderar)
    dtgraphar(folderar)

def pfgraph(legacyfolder, timespan):
    p = ppcalcoverall(legacyfolder, timespan)
    f = ftfcalcoverall(legacyfolder, timespan)
    temp = grabdays(legacyfolder, timespan)
    x = 0
    labels = []
    while x < temp.__len__():
        labels.append(temp[x][28:temp[x].__len__()])
        x = x + 1
    print(labels)
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=labels, y=p, text=p, line_color='rgb(0,100,0)', name="Passed"))
    fig.add_trace(go.Scatter(x=labels, y=f, text=f, line_color='rgb(100,0,0)', name="Failed"), secondary_y=True)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', autosize=False, width=840,
                      height=600)
    fig.update_layout(title="Part", title_font_color="white")
    fig.update_xaxes(color='white')
    fig.update_yaxes(color='white')
    fig.write_image("static/img/ppm.png")
    print("parts updated")


if __name__ == '__main__':
    a = ["databaseCsv", "databaseCsv_2022-11-08"]
    b = [[3000,2000], [1800,1000,2090]]
    dbstore()
    print(ppcalcoverall("legacyDatabases", 4))
    print(ftfcalcoverall("legacyDatabases", 4))
    print("databaseCsv_2022-11-08"[12: 22])
    pfgraph("legacyDatabases", 4)