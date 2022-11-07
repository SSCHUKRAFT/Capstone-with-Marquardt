from flask import Flask, render_template
import main

app = Flask(__name__, template_folder="templates")
data = "databaseCsv"
data2 = "databaseCsvtest"
f1p = [3000,2000]
f2p = [2000,1500,2090]

@app.route("/")
def index():
    return render_template("FrontEnd/LoginPage.html")


@app.route("/Main/")
def mainpage():
    main.collective(data, f1p)
    if (main.average(main.prodcalc(data, f1p))) < 85:
        g = "red"
    else:
        g = "green"
    if main.average(main.dtcalc(data))/6 > 10:
        b = "red"
    else:
        b = "green"
    return render_template("FrontEnd/f1/Mainpage.html",
                           ppm=round(main.average(main.ppmcalc(data)), 2),
                           pro=round(main.average(main.prodcalc(data, f1p)), 2),
                           tt=(main.ttcalc(data)[0]+(main.ttcalc(data)[1])),
                           dt=round(main.average(main.dtcalc(data))/6),
                           w=round(main.ochange(main.ppmcalc(data))),
                           y=(main.ttcalc(data)[2]),
                           z=round(main.average(main.dtcalc(data))),
                           f="Floor 1",
                           pcolor=g,
                           dtcolor=b,
                           ttgcolor="green",
                           ttfcolor="red",
           )

@app.route("/ppm/")
def ppm():
    main.ppmgraph(data)
    return render_template("FrontEnd/f1/ppm.html")

@app.route("/pro/")
def pro():
    main.prodgraph(data, f1p)
    return render_template("FrontEnd/f1/pro.html")

@app.route("/tt/")
def totalthr():
    main.ttgraph(data)
    return render_template("FrontEnd/f1/totalthr.html")

@app.route("/dt/")
def downtime():
    main.dtgraph(data)
    return render_template("FrontEnd/f1/downtime.html")

@app.route("/Main2/")
def mainpage2():
    main.collective(data, f2p)
    if (main.average(main.prodcalc(data2, f2p))) < 85:
        g = "red"
    else:
        g = "green"
    if main.average(main.dtcalc(data2))/6 > 10:
        b = "red"
    else:
        b = "green"
    return render_template("FrontEnd/f2/Mainpagef2.html",
                           ppm=round(main.average(main.ppmcalc(data2)), 2),
                           pro=round(main.average(main.prodcalc(data2, f2p)), 2),
                           tt=(main.ttcalc(data2)[0] + (main.ttcalc(data2)[1])),
                           dt=round(main.average(main.dtcalc(data2))/6),
                           w=round(main.ochange(main.ppmcalc(data2))),
                           y=(main.ttcalc(data2)[2]),
                           z=round(main.average(main.dtcalc(data2))),
                           f="Floor 2",
                           pcolor=g,
                           dtcolor=b,
                           ttgcolor="green",
                           ttfcolor="red",
           )

@app.route("/ppm2/")
def ppm2():
    main.ppmgraph(data2)
    return render_template("FrontEnd/f2/ppm2.html")

@app.route("/pro2/")
def pro2():
    main.prodgraph(data2, f2p)
    return render_template("FrontEnd/f2/pro2.html")

@app.route("/tt2/")
def totalthr2():
    main.ttgraph(data2)
    return render_template("FrontEnd/f2/totalthr2.html")

@app.route("/dt2/")
def downtime2():
    main.dtgraph(data2)
    return render_template("FrontEnd/f2/downtime2.html")

@app.route("/Main3/")
def mainpage3():
    main.collectivear([data, data2], [f1p, f2p])
    if main.average(main.prodcalcall([data, data2], [f1p, f2p])) < 85:
        g = "red"
    else:
        g = "green"
    if main.average(main.dtcalcall([data,data2]))/6 > 10:
        b = "red"
    else:
        b = "green"
    return render_template("FrontEnd/f3/Mainpagef2.html",
                           ppm=round(main.average(main.ppmcalcall([data, data2])), 2),
                           pro=round(main.average(main.prodcalcall([data, data2], [f1p, f2p])), 2),
                           tt=(main.ttcalcall([data, data2])[1][0] + (main.ttcalcall([data, data2])[1][1])),
                           dt=round(main.average(main.dtcalcall([data, data2])) / 6),
                           w=round(main.ochange(main.ppmcalcall([data, data2]))),
                           y=(main.ttcalcall([data, data2])[1][2]),
                           z=round(main.average(main.dtcalcall([data, data2]))),
                           f="All Floors",
                           pcolor=g,
                           dtcolor=b,
                           ttgcolor="green",
                           ttfcolor="red",
           )

@app.route("/ppm3/")
def ppm3():
    main.ppmgraphar([data, data2])
    return render_template("FrontEnd/f3/ppm2.html")

@app.route("/pro3/")
def pro3():
    main.prodgraphar([data, data2], [f1p, f2p])
    return render_template("FrontEnd/f3/pro2.html")

@app.route("/tt3/")
def totalthr3():
    main.ttgraphar([data, data2])
    return render_template("FrontEnd/f3/totalthr2.html")

@app.route("/dt3/")
def downtime3():
    main.dtgraphar([data, data2])
    return render_template("FrontEnd/f3/downtime2.html")

@app.route("/f1/")
def f1():
    main.collective(data, f1p)
    if (main.average(main.prodcalc(data, f1p))) < 85:
        g = "red"
    else:
        g = "green"
    if main.average(main.dtcalc(data))/6 > 10:
        b = "red"
    else:
        b = "green"
    return render_template("FrontEnd/f1/Mainpage.html",
                           ppm=round(main.average(main.ppmcalc(data)), 2),
                           pro=round(main.average(main.prodcalc(data, f1p)), 2),
                           tt=(main.ttcalc(data)[0] + (main.ttcalc(data)[1])),
                           dt=round(main.average(main.dtcalc(data2))/6),
                           w=round(main.ochange(main.ppmcalc(data))),
                           y=(main.ttcalc(data)[2]),
                           z=round(main.average(main.dtcalc(data))),
                           f="Floor 1",
                           pcolor=g,
                           dtcolor=b,
                           ttgcolor="green",
                           ttfcolor="red",
                           )

@app.route("/f2/")
def f2():
    main.collective(data2, f2p)
    if (main.average(main.prodcalc(data2, f2p))) < 85:
        g = "red"
    else:
        g = "green"
    if main.average(main.dtcalc(data2))/6 > 10:
        b = "red"
    else:
        b = "green"
    return render_template("FrontEnd/f2/Mainpagef2.html",
                           ppm=round(main.average(main.ppmcalc(data2)), 2),
                           pro=round(main.average(main.prodcalc(data2, f2p)), 2),
                           tt=(main.ttcalc(data2)[0] + (main.ttcalc(data2)[1])),
                           dt=round(main.average(main.dtcalc(data2))/6),
                           w=round(main.ochange(main.ppmcalc(data2))),
                           y=(main.ttcalc(data2)[2]),
                           z=round(main.average(main.dtcalc(data2))),
                           f="Floor 2",
                           pcolor=g,
                           dtcolor=b,
                           ttgcolor="green",
                           ttfcolor="red",
                           )


@app.route("/f3/")
def f3():
    main.collectivear([data, data2], [f1p, f2p])
    if main.average(main.prodcalcall([data, data2], [f1p, f2p])) < 85:
        g = "red"
    else:
        g = "green"
    if main.average(main.dtcalcall([data, data2]))/6 > 10:
        b = "red"
    else:
        b = "green"
    return render_template("FrontEnd/f3/Mainpagef2.html",
                           ppm=round(main.average(main.ppmcalcall([data, data2])), 2),
                           pro=round(main.average(main.prodcalcall([data, data2], [f1p, f2p])), 2),
                           tt=(main.ttcalcall([data, data2])[1][0] + (main.ttcalcall([data, data2])[1][1])),
                           dt=round(main.average(main.dtcalcall([data, data2])) / 6),
                           w=round(main.ochange(main.ppmcalcall([data, data2]))),
                           y=(main.ttcalcall([data, data2])[1][2]),
                           z=round(main.average(main.dtcalcall([data, data2]))),
                           f="All Floors",
                           pcolor=g,
                           ttgcolor="green",
                           ttfcolor="red",
                           )



if __name__ == "__main__":
    app.run()
