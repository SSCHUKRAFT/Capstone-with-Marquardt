import os
import shutil as sh
import datetime
import plotly.graph_objects as go
from fpdf import FPDF
from plotly.subplots import make_subplots
import kaleido 
print(kaleido.__version__)

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

def zipit(folder, loc):
    if folder+".zip" in os.listdir(loc):
        os.remove(loc+"/"+folder+".zip")
        sh.make_archive(loc+"/"+folder, 'zip', folder)
    else:
        sh.make_archive(loc+"/"+folder, 'zip', folder)
    print("file zipped")

def grabdays(legacyfolder, timespan):
    days=[]
    x = 0
    if timespan < os.listdir(legacyfolder).__len__():
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

def combineav(array1, array2):
    final = []
    x = 0
    if array1.__len__() < array2.__len__():
        while x < array1.__len__():
            final.append(((average([array1[x], array2[x]]))))
            x = x + 1
        while x < array2.__len__():
            final.append((array2[x]))
            x = x + 1
    elif array1.__len__() > array2.__len__():
        while x < array2.__len__():
            final.append(((average([array1[x], array2[x]]))))
            x = x + 1
        while x < array1.__len__():
            final.append((array1[x]))
            x = x + 1
    else:
        while x < array1.__len__():
            final.append((round(average([array1[x], array2[x]]))))
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

def lowestarr(folderar):
    x = 0
    fold = folderar[0]
    while x < folderar.__len__():
        if fold.__len__() > folderar[x].__len__():
            fold = folderar[x]
        else:
            fold = fold
        x = x + 1
    return fold

# Calculate
def passthresholds(folder):
    x = 2
    final = []
    if os.path.exists(folder):
        while x < 12:
            final.append(add(consolidate(folder, 5, x)))
            x = x + 1
    else:
        final.append(0)
    return final

def failthresholds(folder):
    x = 13
    final = []
    if os.path.exists(folder):
        while x < 23:
            final.append(add(consolidate(folder, 5, x)))
            x = x + 1
    else:
        final.append(0)
    return final

def ftfcalc(folder):
    results = []
    x = 0
    if os.path.exists(folder):
        f = consolidate(folder, 2, 1)
        while x < f.__len__():
            results.append(f[x])
            x = x + 1
    else:
        results.append(0)
    return results

def ppcalc(folder):
    if os.path.exists(folder):
        p = consolidate(folder, 3, 1)
        r = consolidate(folder, 4, 1)
        results = combine(p, r)
    else:
        results = [0]
    return results

def prodcalc(folder):
    x = 0
    values = []
    if os.path.exists(folder):
        te = passthresholds(folder)
        workhours = 10
        pdata = consolidate(folder, 3, 1)
        op = (workhours-.25) * pdata.__len__()
        while x < pdata.__len__():
            tes = te[x]/1000*60
            st = (tes*pdata[x])/(3600)
            p = st/op
            values.append(p * 100)
            x = x + 1
    else:
        values.append(0)
    return values

def dtcalc(folder):
    if os.path.exists(folder):
        dt = consolidate(folder, 0, 1)
        et = consolidate(folder, 0, 2)
        results = combine(dt, et)
    else: results = [0]
    return results

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

def ptall(folderar, timespan):
    fol = grabdays(folderar[0], timespan)
    x = 0
    final = []
    while x < fol.__len__():
        final.append(add(passthresholds(fol[x])))
        x = x + 1
    return final

def ftall(folderar, timespan):
    fol = grabdays(folderar[0], timespan)
    x = 0
    final = []
    while x < fol.__len__():
        final.append(add(failthresholds(fol[x])))
        x = x + 1
    return final

def ftfcalcoverall(legacyfolder, timespan):
    fol = grabdays(legacyfolder, timespan)
    x = 0
    final = []
    f = os.listdir(legacyfolder)
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
        final.append(add(prodcalc(fol[x])))
        x = x + 1
    return final

def dtcalcoverall(legacyfolder, timespan):
    fol = grabdays(legacyfolder, timespan)
    x = 0
    final = []
    while x < fol.__len__():
        if os.path.exists(fol[x]):
            final.append(average(consolidate(fol[x], 0, 1)))
        else:
            final.append(0)
        x = x + 1
    return final

def escalcoverall(legacyfolder, timespan):
    fol = grabdays(legacyfolder, timespan)
    x = 0
    final = []
    while x < fol.__len__():
        if os.path.exists(fol[x]):
            final.append(average(consolidate(fol[x], 0, 2)))
        else:
            final.append(0)
        x = x + 1
    return final

def ftfcalcall(folderar, time):
    x = 0
    collection = []
    final = []
    while x < folderar.__len__():
        collection.append(ftfcalcoverall(folderar[x], time))
        x = x + 1
    y = 0
    while y < folderar.__len__():
        final = collection[0]
        final = combineav(final, collection[y])
        y = y + 1
    return final

def ppcalcall(folderar, time):
    x = 0
    collection = []
    final = []
    while x < folderar.__len__():
        collection.append(ppcalcoverall(folderar[x], time))
        x = x + 1
    y = 0
    while y < folderar.__len__():
        final = collection[0]
        final = combineav(final, collection[y])
        y = y + 1
    return final

def prodcalcall(folderar, time):
    x = 0
    collection = []
    final = []
    while x < folderar.__len__():
        collection.append(prodcalcoverall(folderar[x], time))
        x = x + 1
    y = 0
    while y < folderar.__len__():
        final = collection[0]
        final = combineav(final, collection[y])
        y = y + 1
    return final

def dtcalcall(folderar, time):
    x = 0
    collection = []
    final = []
    while x < folderar.__len__():
        collection.append(dtcalcoverall(folderar[x], time))
        x = x + 1
    y = 0
    while y < folderar.__len__():
        final = collection[0]
        final = combineav(final, collection[y])
        y = y + 1
    return final

def escalcall(folderar, time):
    x = 0
    collection = []
    final = []
    while x < folderar.__len__():
        collection.append(escalcoverall(folderar[x], time))
        x = x + 1
    y = 0
    while y < folderar.__len__():
        final = collection[0]
        final = combineav(final, collection[y])
        y = y + 1
    return final

# Graph
def ftfgraphar(folderar, timespan, color):
    p = ppcalcall(folderar, timespan)
    f = ftfcalcall(folderar, timespan)
    ptt = ptall(folderar, timespan)
    ftt = ftall(folderar, timespan)
    temp = grabdays(lowestarr(folderar), timespan)
    exp = []
    exp2 = []
    x = 0
    labels = []
    while x < temp.__len__():
        labels.append(temp[x][temp[x].__len__() - 8:temp[x].__len__()])
        exp.append(p[x] - average(p))
        exp2.append(f[x] + average(f))
        x = x + 1
    i = 0
    while i < exp.__len__():
        if exp[i] < 0:
            exp[i] = 0
        i = i + 1
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=labels, y=ptt, text=ptt, line_color='rgb(0,200,0)', name="Expected Throughput"))
    fig.add_trace(go.Scatter(x=labels, y=ftt, text=ftt, line_color='rgb(200,0,0)', name="Expected Failed"),
                  secondary_y=True)
    fig.add_trace(go.Scatter(x=labels, y=p, text=p, line_color='rgb(0,100,0)', name="Actual Throughput"))
    fig.add_trace(go.Scatter(x=labels, y=exp, text=p, line_color='rgba(0,0,0,0)', showlegend=False))
    fig.add_trace(go.Scatter(x=labels, y=exp2, text=p, line_color='rgba(0,0,0,0)', showlegend=False), secondary_y=True)
    fig.add_trace(go.Scatter(x=labels, y=f, text=f, line_color='rgb(100,0,0)', name="Actual Failed"), secondary_y=True)
    fig.update_layout(title="First Time Failures & Total Throughput", title_font_color=color,
                      paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', autosize=False, width=840,
                      height=600)
    fig.update_layout(legend=dict(font=dict(color=color)))
    fig.update_xaxes(color=color)
    fig.update_yaxes(color=color, title="Throughput")
    fig.update_yaxes(gridcolor='rgb(50,50,50)', title="Failed", secondary_y=True)
    fig.update_yaxes(rangemode='tozero', constraintoward='bottom')
    fig.update_yaxes(rangemode='tozero', constraintoward='bottom', secondary_y=True)
    fig.write_image("static/img/ppm.png")
    print("parts updated")

def prodgraphar(folderar, timespan, color):
    p = prodcalcall(folderar, timespan)
    temp = grabdays(lowestarr(folderar), timespan)
    x = 0
    labels = []
    hun = []
    eighty = []
    while x < temp.__len__():
        labels.append(temp[x][temp[x].__len__() - 8:temp[x].__len__()])
        hun.append(100)
        eighty.append(85)
        x = x + 1
    fig = make_subplots()
    fig.add_trace(go.Scatter(x=labels, y=p, text=p, line_color='rgb(0,0,150)', name="Productivity", showlegend=False))
    fig.add_trace(go.Scatter(x=labels, y=hun, line_color='rgb(0,150,0)', name="100% Productivity"))
    fig.add_trace(go.Scatter(x=labels, y=eighty, line_color='rgb(150,0,0)', name="85% Productivity"))
    fig.update_layout(title="Productivity", title_font_color=color, paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)', autosize=False, width=840,
                      height=600)
    fig.update_layout(legend=dict(font=dict(color=color)))
    fig.update_xaxes(color=color)
    fig.update_yaxes(color=color)
    fig.write_image("static/img/pro.png")
    print("Productivity updated")

def dtgraphar(folderar, timespan, color):
    p = dtcalcall(folderar, timespan)
    e = escalcall(folderar, timespan)
    temp = grabdays(lowestarr(folderar), timespan)
    x = 0
    labels = []
    while x < temp.__len__():
        labels.append(temp[x][temp[x].__len__() - 8:temp[x].__len__()])
        x = x + 1
    fig = make_subplots()
    fig.add_trace(go.Scatter(x=labels, y=p, text=p, line_color='rgb(0,0,150)', name="Downtime"))
    fig.add_trace(go.Scatter(x=labels, y=e, text=e, line_color='rgb(150,75,50)', name="Escalation time"))
    fig.update_layout(title="Downtime", title_font_color=color, paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)', autosize=False, width=840,
                      height=600)
    fig.update_layout(legend=dict(font=dict(color=color)))
    fig.update_xaxes(color=color)
    fig.update_yaxes(color=color)
    fig.write_image("static/img/dt.png")
    print("Downtime updated")

def collectivear(folderar, time, color):
    ftfgraphar(folderar, time, color)
    prodgraphar(folderar, time, color)
    dtgraphar(folderar, time, color)

def ftfgraph(legacyfolder, timespan, color):
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
    fig.update_layout(title="First Time Failures & Total Throughput", title_font_color=color, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', autosize=False, width=840,
                      height=600)
    fig.update_layout(legend=dict(font=dict(color=color)))
    fig.update_xaxes(color=color)
    fig.update_yaxes(color=color, title="Throughput")
    fig.update_yaxes(gridcolor='rgb(50,50,50)', title="Failed", secondary_y=True)
    fig.update_yaxes(rangemode='tozero', constraintoward='bottom')
    fig.update_yaxes(rangemode='tozero', constraintoward='bottom', secondary_y=True)
    fig.write_image("static/img/ppm.png")
    print("parts updated")

def prodgraph(legacyfolder, timespan, color):
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
    fig.update_layout(title="Productivity", title_font_color=color, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', autosize=False, width=840,
                      height=600)
    fig.update_layout(legend=dict(font=dict(color=color)))
    fig.update_xaxes(color=color)
    fig.update_yaxes(color=color)
    fig.write_image("static/img/pro.png")
    print("Productivity updated")

def dtgraph(legacyfolder, timespan, color):
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
    fig.update_layout(title="Downtime", title_font_color=color, paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)', autosize=False, width=840,
                      height=600)
    fig.update_layout(legend=dict(font=dict(color=color)))
    fig.update_xaxes(color=color)
    fig.update_yaxes(color=color)
    fig.write_image("static/img/dt.png")
    print("Downtime updated")

def collective(folder, time, color):
    ftfgraph(folder, time, color)
    prodgraph(folder, time, color)
    dtgraph(folder, time, color)

def pdfit(legacyfolder, timespan):
    collective(legacyfolder, timespan, "black")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.cell(200, 10, txt="Marquardt Inc.",ln=1, align='C')
    pdf.cell(200, 10, txt="Floor Report", ln=1, align='C')
    s=72
    pdf.image("static/img/mar2.png", 0, 0, 0,20)
    pdf.image("static/img/ppm.png", 108, 30, 0, s)
    pdf.image("static/img/pro.png", 10, 100, 0, s)
    pdf.image("static/img/dt.png", 108, 100, 0, s)
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt="",ln=1, align='l')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(200, 10, txt="Average FTF: "+str(round(average(ftfcalcoverall(legacyfolder, timespan)), 2))+" ppm", ln=1, align='l')
    pdf.cell(200, 10, txt="Average TTP: "+str(round(average(ppcalcoverall(legacyfolder, timespan)), 2))+" ppm", ln=1, align='l')
    pdf.cell(200, 10, txt="Productivity: " + str(round(average(prodcalcoverall(legacyfolder, timespan)), 2)) + "%", ln=1, align='l')
    pdf.cell(200, 10, txt="Downtime Percentage: " + str(round(average(dtcalcoverall(legacyfolder, timespan))/ 6)) + "%", ln=1,align='l')
    pdf.cell(200, 10, txt="Downtime in minutes: " + str(round(average(dtcalcoverall(legacyfolder, timespan)))) + " min", ln=1,align='l')
    pdf.output("static/report.pdf")
    print("Report created")

def pdfita(folderar, timespan):
    collectivear(folderar, timespan, "black")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.cell(200, 10, txt="Marquardt Inc.",ln=1, align='C')
    pdf.cell(200, 10, txt="Floor Report", ln=1, align='C')
    s=72
    pdf.image("static/img/mar2.png", 0, 0, 0,20)
    pdf.image("static/img/ppm.png", 108, 30, 0, s)
    pdf.image("static/img/pro.png", 10, 100, 0, s)
    pdf.image("static/img/dt.png", 108, 100, 0, s)
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt="",ln=1, align='l')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(200, 10, txt="Average FTF: "+str(round(average(ftfcalcall(folderar, timespan)), 2))+" ppm", ln=1, align='l')
    pdf.cell(200, 10, txt="Average TTP: "+str(round(average(ppcalcall(folderar, timespan)), 2))+" ppm", ln=1, align='l')
    pdf.cell(200, 10, txt="Productivity: " + str(round(average(prodcalcall(folderar, timespan)), 2)) + "%", ln=1, align='l')
    pdf.cell(200, 10, txt="Downtime Percentage: " + str(round(average(dtcalcall(folderar, timespan))/ 6)) + "%", ln=1,align='l')
    pdf.cell(200, 10, txt="Downtime in minutes: " + str(round(average(dtcalcall(folderar, timespan)))) + " min", ln=1,align='l')
    pdf.output("static/report.pdf")
    print("Report created")

if __name__ == '__main__':
    data = "databaseCsv"
    data2 = "databaseCsv2"
    ldata = "legacyDatabases"
    ldata2 = "legacyDatabases2"
    time = 100000
    collective(ldata, time, "white")
