from flask import Flask, render_template
import main

app = Flask(__name__, template_folder="templates")
data = "databaseCsv"
ldata = "legacyDatabases"
ldata2 = "legacyDatabasestest"
time = 100
f1p = [3000,2000]
f2p = [2000,1500,2090]

@app.route("/")
def index():
    main.dbstore(data, ldata)
    return render_template("FrontEnd/LoginPage.html")


@app.route("/Main/")
def mainpage():
    main.collective(ldata, f2p, time)
    if (main.average(main.prodcalcoverall(ldata, time, f2p))) < 85:
        g = "red"
    else:
        g = "green"
    if main.average(main.dtcalcoverall(ldata, time))/6 > 10:
        b = "red"
    else:
        b = "green"
    return render_template("FrontEnd/f1/Mainpage.html",
                           #ppm=round(main.average(main.ftfcalcoverall(ldata, time)), 2),
                           #pro=round(main.average(main.prodcalcoverall(ldata, time, f2p)), 2),
                           #tt=(main.ppcalcoverall(ldata, time)[1]),
                           #dt=round(main.average(main.dtcalcoverall(ldata, time)) / 6),
                           #w=round(main.add(main.ftfcalcoverall(ldata, time))),
                           #y=(main.ppcalcoverall(ldata, time)),
                           #z=round(main.average(main.dtcalcoverall(ldata, time))),
                           #f="Floor 1",
                           #pcolor=g,
                           #dtcolor=b,
                           #ttgcolor="green",
                           #ttfcolor="red",
                           )

@app.route("/ppm/")
def ppm():
    main.ftfgraph(ldata, time)
    return render_template("FrontEnd/f1/ppm.html")

@app.route("/pro/")
def pro():
    main.prodgraph(ldata, time, f2p)
    return render_template("FrontEnd/f1/pro.html")

@app.route("/tt/")
def totalthr():
    main.ttgraph(ldata, time)
    return render_template("FrontEnd/f1/totalthr.html")

@app.route("/dt/")
def downtime():
    main.dtgraph(ldata, time)
    return render_template("FrontEnd/f1/downtime.html")

@app.route("/Main2/")
def mainpage2():
    main.collective(ldata, f2p, time)
    if (main.average(main.prodcalc(ldata2, f2p))) < 85:
        g = "red"
    else:
        g = "green"
    if main.average(main.dtcalc(ldata2))/6 > 10:
        b = "red"
    else:
        b = "green"
    return render_template("FrontEnd/f2/Mainpagef2.html",
                           #ppm=round(main.average(main.ftfcalc(ldata2)), 2),
                           #pro=round(main.average(main.prodcalc(ldata2, f2p)), 2),
                           #tt=(main.ttcalc(ldata2)[0] + (main.ttcalc(ldata2)[1])),
                           #dt=round(main.average(main.dtcalc(ldata2)) / 6),
                           #w=round(main.add(main.ftfcalc(ldata2))),
                           #y=(main.ttcalc(ldata2)[2]),
                           #z=round(main.average(main.dtcalc(ldata2))),
                           #f="Floor 2",
                           #pcolor=g,
                           #dtcolor=b,
                           #ttgcolor="green",
                           #ttfcolor="red",
                           )

@app.route("/ppm2/")
def ppm2():
    main.ftfgraph(ldata2, time)
    return render_template("FrontEnd/f2/ppm2.html")

@app.route("/pro2/")
def pro2():
    main.prodgraph(ldata2, time, f2p)
    return render_template("FrontEnd/f2/pro2.html")

@app.route("/tt2/")
def totalthr2():
    main.ttgraph(ldata2, time)
    return render_template("FrontEnd/f2/totalthr2.html")

@app.route("/dt2/")
def downtime2():
    main.dtgraph(ldata2, time)
    return render_template("FrontEnd/f2/downtime2.html")

@app.route("/Main3/")
def mainpage3():
    main.collectivear([ldata, ldata2], [f1p, f2p])
    if main.average(main.prodcalcall([ldata, ldata2], [f1p, f2p])) < 85:
        g = "red"
    else:
        g = "green"
    if main.average(main.dtcalcall([ldata, ldata2]))/6 > 10:
        b = "red"
    else:
        b = "green"
    return render_template("FrontEnd/f3/Mainpagef2.html",
                           ppm=round(main.average(main.ppmcalcall([ldata, ldata2])), 2),
                           pro=round(main.average(main.prodcalcall([ldata, ldata2], [f1p, f2p])), 2),
                           tt=(main.ttcalcall([ldata, ldata2])[1][0] + (main.ttcalcall([ldata, ldata2])[1][1])),
                           dt=round(main.average(main.dtcalcall([ldata, ldata2])) / 6),
                           w=round(main.add(main.ppmcalcall([ldata, ldata2]))),
                           y=(main.ttcalcall([ldata, ldata2])[1][2]),
                           z=round(main.average(main.dtcalcall([ldata, ldata2]))),
                           f="All Floors",
                           pcolor=g,
                           dtcolor=b,
                           ttgcolor="green",
                           ttfcolor="red",
                           )

@app.route("/ppm3/")
def ppm3():
    main.ftfgraphar([ldata, ldata2])
    return render_template("FrontEnd/f3/ppm2.html")

@app.route("/pro3/")
def pro3():
    main.prodgraphar([ldata, ldata2], [f1p, f2p])
    return render_template("FrontEnd/f3/pro2.html")

@app.route("/tt3/")
def totalthr3():
    main.ttgraphar([ldata, ldata2])
    return render_template("FrontEnd/f3/totalthr2.html")

@app.route("/dt3/")
def downtime3():
    main.dtgraphar([ldata, ldata2])
    return render_template("FrontEnd/f3/downtime2.html")

@app.route("/f1/")
def f1():
    main.collective(ldata, f1p, time)
    if (main.average(main.prodcalc(ldata, f1p))) < 85:
        g = "red"
    else:
        g = "green"
    if main.average(main.dtcalc(ldata))/6 > 10:
        b = "red"
    else:
        b = "green"
    return render_template("FrontEnd/f1/Mainpage.html",
                           #ppm=round(main.average(main.ftfcalc(ldata)), 2),
                           #pro=round(main.average(main.prodcalc(ldata, f1p)), 2),
                           #tt=(main.ttcalc(ldata)[0] + (main.ttcalc(ldata)[1])),
                           #dt=round(main.average(main.dtcalc(ldata2)) / 6),
                           #w=round(main.add(main.ftfcalc(ldata))),
                           #y=(main.ttcalc(ldata)[2]),
                           #z=round(main.average(main.dtcalc(ldata))),
                           #f="Floor 1",
                           #pcolor=g,
                           #dtcolor=b,
                           #ttgcolor="green",
                           #ttfcolor="red",
                           )

@app.route("/f2/")
def f2():
    main.collective(ldata2, time, f2p)
    if (main.average(main.prodcalc(ldata2, f2p))) < 85:
        g = "red"
    else:
        g = "green"
    if main.average(main.dtcalc(ldata2))/6 > 10:
        b = "red"
    else:
        b = "green"
    return render_template("FrontEnd/f2/Mainpagef2.html",
                           ppm=round(main.average(main.ftfcalc(ldata2)), 2),
                           pro=round(main.average(main.prodcalc(ldata2, f2p)), 2),
                           tt=(main.ttcalc(ldata2)[0] + (main.ttcalc(ldata2)[1])),
                           dt=round(main.average(main.dtcalc(ldata2)) / 6),
                           w=round(main.add(main.ftfcalc(ldata2))),
                           y=(main.ttcalc(ldata2)[2]),
                           z=round(main.average(main.dtcalc(ldata2))),
                           f="Floor 2",
                           pcolor=g,
                           dtcolor=b,
                           ttgcolor="green",
                           ttfcolor="red",
                           )


@app.route("/f3/")
def f3():
    main.collectivear([ldata, ldata2], [f1p, f2p])
    if main.average(main.prodcalcall([ldata, ldata2], [f1p, f2p])) < 85:
        g = "red"
    else:
        g = "green"
    if main.average(main.dtcalcall([ldata, ldata2]))/6 > 10:
        b = "red"
    else:
        b = "green"
    return render_template("FrontEnd/f3/Mainpagef2.html",
                           ppm=round(main.average(main.ppmcalcall([ldata, ldata2])), 2),
                           pro=round(main.average(main.prodcalcall([ldata, ldata2], [f1p, f2p])), 2),
                           tt=(main.ttcalcall([ldata, ldata2])[1][0] + (main.ttcalcall([ldata, ldata2])[1][1])),
                           dt=round(main.average(main.dtcalcall([ldata, ldata2])) / 6),
                           w=round(main.add(main.ppmcalcall([ldata, ldata2]))),
                           y=(main.ttcalcall([ldata, ldata2])[1][2]),
                           z=round(main.average(main.dtcalcall([ldata, ldata2]))),
                           f="All Floors",
                           pcolor=g,
                           ttgcolor="green",
                           ttfcolor="red",
                           )



if __name__ == "__main__":
    app.run()
