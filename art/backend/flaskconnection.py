from flask import Flask, render_template, request
import main

app = Flask(__name__, template_folder="templates")
data = "databaseCsv"
data2 = "databaseCsv2"
ldata = "legacyDatabases"
ldata2 = "legacyDatabases2"
time = 100000

@app.route("/")
def index():
    main.dbstore(data, ldata)
    main.dbstore(data2,ldata2)
    main.zipit(ldata, "Csvs")
    main.zipit(ldata2, "Csvs")
    main.zipit("Csvs", "static")
    return render_template("FrontEnd/LoginPage.html")

@app.route("/Main/", methods=['GET', 'POST'])
def mainpage():
    global time
    if request.method == "POST":
        time = int(request.form.get("num"))
    main.pdfit(ldata, time)
    main.collective(ldata, time, "white")
    if (main.average(main.prodcalcoverall(ldata, time))) < 85:
        g = "red"
    else:
        g = "green"
    if main.average(main.dtcalcoverall(ldata, time))/6 > 10:
        b = "red"
    else:
        b = "green"
    return render_template("FrontEnd/f1/Mainpage.html",
                           ppm=round(main.average(main.ftfcalcoverall(ldata, time)), 2),
                           pro=round(main.average(main.prodcalcoverall(ldata, time)), 2),
                           dt=round(main.average(main.dtcalcoverall(ldata, time)) / 6),
                           w=round(main.average(main.ppcalcoverall(ldata, time))),
                           z=round(main.average(main.dtcalcoverall(ldata, time))),
                           f="Floor 1",
                           pcolor=g,
                           dtcolor=b,
                           )

@app.route("/ppm/", methods=['GET', 'POST'])
def ppm():
    global time
    if request.method == "POST":
        time = int(request.form.get("num"))
    main.pdfit(ldata, time)
    main.ftfgraph(ldata, time, "white")
    return render_template("FrontEnd/f1/ppm.html")

@app.route("/pro/", methods=['GET', 'POST'])
def pro():
    global time
    if request.method == "POST":
        time = int(request.form.get("num"))
    main.pdfit(ldata, time)
    main.prodgraph(ldata, time, "white")
    return render_template("FrontEnd/f1/pro.html")

@app.route("/dt/", methods=['GET', 'POST'])
def downtime():
    global time
    if request.method == "POST":
        time = int(request.form.get("num"))
    main.pdfit(ldata, time)
    main.dtgraph(ldata, time, "white")
    return render_template("FrontEnd/f1/downtime.html")

@app.route("/Main2/", methods=['GET', 'POST'])
def mainpage2():
    global time
    if request.method == "POST":
        time = int(request.form.get("num"))
    main.pdfit(ldata2, time)
    main.collective(ldata2, time, "white")
    if (main.average(main.prodcalcoverall(ldata2, time))) < 85:
        g = "red"
    else:
        g = "green"
    if main.average(main.dtcalcoverall(ldata2, time)) / 6 > 10:
        b = "red"
    else:
        b = "green"
    return render_template("FrontEnd/f2/Mainpagef2.html",
                           ppm=round(main.average(main.ftfcalcoverall(ldata2, time)), 2),
                           pro=round(main.average(main.prodcalcoverall(ldata2, time)), 2),
                           dt=round(main.average(main.dtcalcoverall(ldata2, time)) / 6),
                           w=round(main.average(main.ppcalcoverall(ldata2, time))),
                           z=round(main.average(main.dtcalcoverall(ldata2, time))),
                           f="Floor 1",
                           pcolor=g,
                           dtcolor=b,
                           )

@app.route("/ppm2/", methods=['GET', 'POST'])
def ppm2():
    global time
    if request.method == "POST":
        time = int(request.form.get("num"))
    main.pdfit(ldata2, time)
    main.ftfgraph(ldata2, time, "white")
    return render_template("FrontEnd/f2/ppm2.html")

@app.route("/pro2/", methods=['GET', 'POST'])
def pro2():
    global time
    if request.method == "POST":
        time = int(request.form.get("num"))
    main.pdfit(ldata2, time)
    main.prodgraph(ldata2, time, "white")
    return render_template("FrontEnd/f2/pro2.html")

@app.route("/dt2/", methods=['GET', 'POST'])
def downtime2():
    global time
    if request.method == "POST":
        time = int(request.form.get("num"))
    main.pdfit(ldata2, time)
    main.dtgraph(ldata2, time, "white")
    return render_template("FrontEnd/f2/downtime2.html")

@app.route("/Main3/", methods=['GET', 'POST'])
def mainpage3():
    global time
    if request.method == "POST":
        time = int(request.form.get("num"))
    main.pdfita([ldata, ldata2], time)
    main.collectivear([ldata, ldata2], time, "white")
    if main.average(main.prodcalcall([ldata, ldata2], time)) < 85:
        g = "red"
    else:
        g = "green"
    if main.average(main.dtcalcall([ldata, ldata2], time)) / 6 > 10:
        b = "red"
    else:
        b = "green"
    return render_template("FrontEnd/f3/Mainpagef2.html",
                           ppm=round(main.average(main.ftfcalcall([ldata, ldata2], time)), 2),
                           pro=round(main.average(main.prodcalcall([ldata, ldata2], time)), 2),
                           dt=round(main.average(main.dtcalcall([ldata, ldata2], time)) / 6),
                           w=round(main.average(main.ppcalcall([ldata, ldata2], time))),
                           z=round(main.average(main.dtcalcall([ldata, ldata2], time))),
                           f="Floor 1",
                           pcolor=g,
                           dtcolor=b,
                           )

@app.route("/ppm3/", methods=['GET', 'POST'])
def ppm3():
    global time
    if request.method == "POST":
        time = int(request.form.get("num"))
    main.pdfita([ldata, ldata2], time)
    main.ftfgraphar([ldata, ldata2], time, "white")
    return render_template("FrontEnd/f3/ppm2.html")

@app.route("/pro3/", methods=['GET', 'POST'])
def pro3():
    global time
    if request.method == "POST":
        time = int(request.form.get("num"))
    main.pdfita([ldata, ldata2], time)
    main.prodgraphar([ldata, ldata2], time, "white")
    return render_template("FrontEnd/f3/pro2.html")

@app.route("/dt3/", methods=['GET', 'POST'])
def downtime3():
    global time
    if request.method == "POST":
        time = int(request.form.get("num"))
    main.pdfita([ldata, ldata2], time)
    main.dtgraphar([ldata, ldata2], time, "white")
    return render_template("FrontEnd/f3/downtime2.html")

@app.route("/f1/", methods=['GET', 'POST'])
def f1():
    global time
    if request.method == "POST":
        time = int(request.form.get("num"))
    main.pdfit(ldata, time)
    main.collective(ldata, time, "white")
    if (main.average(main.prodcalcoverall(ldata, time))) < 85:
        g = "red"
    else:
        g = "green"
    if main.average(main.dtcalcoverall(ldata, time)) / 6 > 10:
        b = "red"
    else:
        b = "green"
    return render_template("FrontEnd/f1/Mainpage.html",
                           ppm=round(main.average(main.ftfcalcoverall(ldata, time)), 2),
                           pro=round(main.average(main.prodcalcoverall(ldata, time)), 2),
                           dt=round(main.average(main.dtcalcoverall(ldata, time)) / 6),
                           w=round(main.average(main.ppcalcoverall(ldata, time))),
                           z=round(main.average(main.dtcalcoverall(ldata, time))),
                           f="Floor 1",
                           pcolor=g,
                           dtcolor=b,
                           )

@app.route("/f2/", methods=['GET', 'POST'])
def f2():
    global time
    if request.method == "POST":
        time = int(request.form.get("num"))
    main.pdfit(ldata, time)
    main.collective(ldata2, time, "white")
    if (main.average(main.prodcalcoverall(ldata2, time))) < 85:
        g = "red"
    else:
        g = "green"
    if main.average(main.dtcalcoverall(ldata2, time)) / 6 > 10:
        b = "red"
    else:
        b = "green"
    return render_template("FrontEnd/f2/Mainpagef2.html",
                           ppm=round(main.average(main.ftfcalcoverall(ldata2, time)), 2),
                           pro=round(main.average(main.prodcalcoverall(ldata2, time)), 2),
                           dt=round(main.average(main.dtcalcoverall(ldata2, time)) / 6),
                           w=round(main.average(main.ppcalcoverall(ldata2, time))),
                           z=round(main.average(main.dtcalcoverall(ldata2, time))),
                           f="Floor 1",
                           pcolor=g,
                           dtcolor=b,
                           )

@app.route("/f3/", methods=['GET', 'POST'])
def f3():
    global time
    if request.method == "POST":
        time = int(request.form.get("num"))
    main.pdfita([ldata, ldata2], time)
    main.collectivear([ldata, ldata2], time, "white")
    if main.average(main.prodcalcall([ldata, ldata2], time)) < 85:
        g = "red"
    else:
        g = "green"
    if main.average(main.dtcalcall([ldata, ldata2], time))/6 > 10:
        b = "red"
    else:
        b = "green"
    return render_template("FrontEnd/f3/Mainpagef2.html",
                           ppm=round(main.average(main.ftfcalcall([ldata, ldata2], time)), 2),
                           pro=round(main.average(main.prodcalcall([ldata, ldata2], time)), 2),
                           dt=round(main.average(main.dtcalcall([ldata, ldata2], time)) / 6),
                           w=round(main.average(main.ppcalcall([ldata, ldata2], time))),
                           z=round(main.average(main.dtcalcall([ldata, ldata2], time))),
                           f="All Floors",
                           pcolor=g,
                           dtcolor=b,
                           )

if __name__ == "__main__":
    app.run(host='0.0.0.0')
