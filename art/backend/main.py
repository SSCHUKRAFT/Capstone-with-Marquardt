import os
import plotly.graph_objects as go

# arrays arrays for days

expectedouptput = [800, 150, 750, 4000]

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

def average(array1, array2):
    final = []
    x = 0
    while x < array1.__len__():
        final.append((array1[x]+array2[x]/2))
        x = x + 1
    return final

def combine(array1, array2):
    final = []
    x = 0
    while x < array1.__len__():
        final.append((array1[x]+array2[x]/2))
        x = x + 1
    return final

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
def ppmcalc(folder):
    values = []
    f = consolidate(folder, 1, 1)
    p = consolidate(folder, 2, 1)
    r = consolidate(folder, 3, 1)
    if p.__len__() < r.__len__():
        i = 0
        while  i < r.__len__():
            p.append(0)
            i = i + 1
    else:
        i = 0
        while  i < p.__len__():
            r.append(0)
            i = i + 1
    good = combine(p, r)
    values = good
    return values

# This measure is a percentage based on “Operator Hours” vs “Productive Hours”
# Operator Hours are the total number of hours booked to a line times the number of operators
# Productive Hours are a relationship of total parts made vs the takt time
def prodcalc(folder):
    x = 0
    workhours = 10
    pdata = consolidate(folder,2,1)
    op = (workhours-.25) * pdata.__len__()
    values = []
    te = [1800,1000,2090]
    while x < pdata.__len__():
        tes = te[x]/1000*60
        st = (tes*pdata[x])/(3600)
        p = st/op
        values.append(p * 100)
        x = x + 1
    return values

# Throughput = total good units produced / time.

def ochange(array):
    x = 0
    y = 0
    while x < array.__len__():
        y = y + array[x]
        x = x + 1
    return y

def ppmnorm(array):
    norm = []
    x = 0
    y = 0
    while x < array.__len__():
        y = round(array[x]/(expectedouptput[x])*100, 2)
        norm.append(y)
        x = x + 1
    return norm

# Graph
def ppmgraph(folder):
    data = mat(folder)[2]
    labels = [*set(column(data, (data[0].__len__() - 3)))]
    labels.remove("machine")
    x = 0
    y = ppmnorm(ppmcalc(folder))
    while x < y.__len__():
        labels.append("Line " + str(x + 1))
        x = x + 1
    fig = go.Figure(data=[go.Bar(x=labels, y=y, text=y, textposition='auto')])
    fig.update_layout( paper_bgcolor= 'rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    fig.update_layout(title="PPM")
    fig.write_image("static/img/ppm.png")
    print("ppm updated")


def prodgraph(folder):
    data = mat(folder)[2]
    labels = [*set(column(data, (data[0].__len__() - 3)))]
    labels.remove("machine")
    x = 0
    y = prodcalc(folder)
    temp = []
    while x < y.__len__():
        temp.append(str(round(y[x], 2))+"%")
        x = x + 1
    fig = go.Figure(data=[go.Table(header=dict(values=["Machine", 'Productivity']),
                                   cells=dict(values=[labels, temp]))
                          ])
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    fig.update_layout(title="Productivity")
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
                          go.Bar(name="Failed", marker_color='rgb(175,5,0)', x=labels, y=f, text=f, textposition='auto'),
                          go.Bar(name="ReTested", marker_color='rgb(0,32,172)', x=labels, y=r, text=r, textposition='auto')])
    fig.update_layout(title="Total Throughput", barmode='stack')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    fig.update_traces(marker_line_color='rgb(8,48,107)')
    fig.write_image("static/img/tt.png")
    print("Total Throughput updated")
    print(f)


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
    fig = go.Figure(data=[go.Bar(name="Downtime", marker_color='rgb(175,5,0)', x=labels, y=y, text=y, textposition='auto'),
                          go.Bar(name="Escalation time", marker_color='rgb(200,80,0)', x=labels, y=w, text=w, textposition='auto'),
                          go.Bar(name="Remaining time", marker_color='rgb(0,172,23)', x=labels, y=z, text=z, textposition='auto')])
    fig.update_layout(title="Downtime", barmode='stack')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    fig.update_traces(marker_line_color='rgb(8,48,107)')
    fig.write_image("static/img/dt.png")
    print("downtime update")

def collective(folder):
    ppmgraph(folder)
    prodgraph(folder)
    ttgraph(folder)
    dtgraph(folder)

def ppmgraphar(array,array2):
    labels = []
    x = 0
    y = ppmnorm(average(array, array2))
    while x < y.__len__():
        labels.append("Line " + str(x + 1))
        x = x + 1
    fig = go.Figure(data=[go.Bar(x=labels, y=y, text=y, textposition='auto')])
    fig.write_image("static/img/ppm.png")
    print("ppm updated")


def prodgraphar(array,array2):
    labels = ["Operator Hours", "Productive hours"]
    x = 0
    y = average(array, array2)
    fig = go.Figure(data=[go.Pie(labels=labels, values=y)])
    fig.write_image("static/img/pro.png")
    print("productivity updated")


def ttgraphar(array,array2):
    labels = []
    x = 0
    y = average(array, array2)
    z = []
    while x < y.__len__():
        labels.append("Line " + str(x + 1))
        z.append(expectedouptput[x] - y[x])
        x = x + 1
    fig = go.Figure(data=[go.Bar(name="Completed parts", marker_color='rgb(175,5,0)', x=labels, y=y, text=y, textposition='auto'), go.Bar(name="quota", marker_color='rgb(0,172,23)', x=labels, y=expectedouptput, text=z, textposition='auto')])
    fig.update_layout(barmode='stack')
    fig.update_traces(marker_line_color='rgb(8,48,107)')
    fig.write_image("static/img/tt.png")
    print("Total Throughput updated")


def dtgraphar(array,array2):
    labels = []
    x = 0
    y = average(array, array2)
    z = []
    while x < y.__len__():
        labels.append("Op "+str(x+1))
        z.append(600-y[x])
        x = x + 1
    fig = go.Figure(data=[go.Bar(name="Downtime", marker_color='rgb(175,5,0)', x=labels, y=y, text=y, textposition='auto'), go.Bar(name="Remaining time", marker_color='rgb(0,172,23)', x=labels, y=z, text=z, textposition='auto')])
    fig.update_layout(barmode='stack')
    fig.update_traces(marker_line_color='rgb(8,48,107)')
    fig.write_image("static/img/dt.png")
    print("downtime update")

def collectivear(array,array2):
    ppmgraph(array,array2)
    prodgraph(array,array2)
    ttgraph(array,array2)
    dtgraph(array,array2)


if __name__ == '__main__':
    print(mat("databaseCsvtest"))
    print(consolidate("databaseCsvtest", 0, 1))
    print(consolidate("databaseCsvtest", 0, 2))
    print(consolidate("databaseCsvtest", 1, 1))
    print(consolidate("databaseCsvtest", 2, 1))
    print(consolidate("databaseCsvtest", 3, 1))
    print(ppmcalc("databaseCsvtest"))
    print(prodcalc("databaseCsvtest"))
    print(ochange(consolidate("databaseCsvtest",2,1)))
    prodgraph("databaseCsvtest")
    dtgraph("databaseCsvtest")
    ttgraph("databaseCsvtest")
    #print(sift("databaseCsv", 'Machine One'))
    #print("PPM data: " + str(ppmcalc("databaseCsv")))
    #print("Prod data: " + str(prodcalc("databaseCsv")))
    #print("tt data: " + str(ttcalc("databaseCsv")))
    #print(ppmnorm(ppmcalc("databaseCsv")))
    #collective("databaseCsv")

