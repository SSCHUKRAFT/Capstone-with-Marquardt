from flask import Flask, render_template
import main

app = Flask(__name__, template_folder="templates")
data = "databaseCsv"

@app.route("/")
def index():
    return render_template("FrontEnd/LoginPage.html")


@app.route("/Main/")
def mainpage():
    main.collective("databaseCsv")
    return render_template("FrontEnd/f1/Mainpage.html",
                           #ppm=round(main.ochange(main.ppmcalc("databaseCsv"))/main.ochange(main.expectedouptput)*100,2),
                           #pro=round((main.prodcalc("databaseCsv")[1])/main.ochange(main.prodcalc("databaseCsv"))*100,2),
                           #tt=round(main.ochange(main.ttcalc("databaseCsv"))/((main.ochange(main.expectedouptput))/(main.ttcalc("databaseCsv").__len__()))*100,2),
                           #dt=round(main.ochange(main.dtcalc("databaseCsv"))/(main.dtcalc("databaseCsv").__len__()*600)*100,2),
                           #w=round(main.ochange(main.ppmcalc("databaseCsv")),2),
                           #x=round(main.prodcalc("databaseCsv")[1],2),
                           #y=round(main.ochange(main.ttcalc("databaseCsv")),2),
                           #z=round(main.ochange(main.dtcalc("databaseCsv")),2)
           )

@app.route("/ppm/")
def ppm():
    main.ppmgraph("databaseCsv")
    return render_template("FrontEnd/f1/ppm.html")

@app.route("/pro/")
def pro():
    main.prodgraph("databaseCsv")
    return render_template("FrontEnd/f1/pro.html")

@app.route("/tt/")
def totalthr():
    main.ttgraph("databaseCsv")
    return render_template("FrontEnd/f1/totalthr.html")

@app.route("/dt/")
def downtime():
    main.dtgraph("databaseCsv")
    return render_template("FrontEnd/f1/downtime.html")

@app.route("/Main2/")
def mainpage2():
    main.collective("databaseCsv2")
    return render_template("FrontEnd/f2/Mainpagef2.html",
                           ppm=round(
                               main.ochange(main.ppmcalc("databaseCsv2")) / main.ochange(main.expectedouptput) * 100, 2),
                           pro=round(
                               (main.prodcalc("databaseCsv2")[1]) / main.ochange(main.prodcalc("databaseCsv2")) * 100, 2),
                           tt=round(main.ochange(main.ttcalc("databaseCsv2")) / ((main.ochange(main.expectedouptput)) / (
                               main.ttcalc("databaseCsv2").__len__())) * 100, 2),
                           dt=round(main.ochange(main.dtcalc("databaseCsv2")) / (
                                       main.dtcalc("databaseCsv2").__len__() * 600) * 100, 2),
                           w=round(main.ochange(main.ppmcalc("databaseCsv2")), 2),
                           x=round(main.prodcalc("databaseCsv2")[1],2),
                           y=round(main.ochange(main.ttcalc("databaseCsv2")), 2),
                           z=round(main.ochange(main.dtcalc("databaseCsv2")), 2))

@app.route("/ppm2/")
def ppm2():
    main.ppmgraph("databaseCsv2")
    return render_template("FrontEnd/f2/ppm2.html")

@app.route("/pro2/")
def pro2():
    main.prodgraph("databaseCsv2")
    return render_template("FrontEnd/f2/pro2.html")

@app.route("/tt2/")
def totalthr2():
    main.ttgraph("databaseCsv2")
    return render_template("FrontEnd/f2/totalthr2.html")

@app.route("/dt2/")
def downtime2():
    main.dtgraph("databaseCsv2")
    return render_template("FrontEnd/f2/downtime2.html")

@app.route("/Main3/")
def mainpage3():
    main.ppmgraphar(main.ppmcalc("databaseCsv"), main.ppmcalc("databaseCsv2"))
    main.prodgraphar(main.prodcalc("databaseCsv"), main.prodcalc("databaseCsv2"))
    main.ttgraphar(main.ttcalc("databaseCsv"), main.ttcalc("databaseCsv2"))
    main.dtgraphar(main.dtcalc("databaseCsv"), main.dtcalc("databaseCsv2"))
    return render_template("FrontEnd/f3/Mainpagef2.html",
                           ppm=round(
                               main.ochange(main.average(main.ppmcalc("databaseCsv"), main.ppmcalc("databaseCsv2"))) / main.ochange(main.expectedouptput) * 100, 2),
                           pro=round(
                               (main.average(main.prodcalc("databaseCsv"), main.prodcalc("databaseCsv2"))[1]) / main.ochange(main.average(main.prodcalc("databaseCsv"), main.prodcalc("databaseCsv2"))) * 100, 2),
                           tt=round(main.ochange(main.average(main.ttcalc("databaseCsv"), main.ttcalc("databaseCsv2"))) / ((main.ochange(main.expectedouptput)) / (
                               main.average(main.ttcalc("databaseCsv"), main.ttcalc("databaseCsv2")).__len__())) * 100, 2),
                           dt=round(
                               main.ochange(main.average(main.dtcalc("databaseCsv"), main.dtcalc("databaseCsv2"))) / (
                                       main.average(main.dtcalc("databaseCsv"),
                                                    main.dtcalc("databaseCsv2")).__len__() * 600) * 100, 2),
                           w=round(
                               main.ochange(main.average(main.ppmcalc("databaseCsv"), main.ppmcalc("databaseCsv2"))),
                               2),
                           x=round(main.average(main.prodcalc("databaseCsv"), main.prodcalc("databaseCsv2"))[1], 2),
                           y=round(main.ochange(main.average(main.ttcalc("databaseCsv"), main.ttcalc("databaseCsv2"))), 2),
                           z=round(main.ochange(main.average(main.dtcalc("databaseCsv"), main.dtcalc("databaseCsv2"))), 2))

@app.route("/ppm3/")
def ppm3():
    main.ppmgraphar(main.ppmcalc("databaseCsv"),main.ppmcalc("databaseCsv2"))
    return render_template("FrontEnd/f3/ppm2.html")

@app.route("/pro3/")
def pro3():
    main.prodgraphar(main.prodcalc("databaseCsv"),main.prodcalc("databaseCsv2"))
    return render_template("FrontEnd/f3/pro2.html")

@app.route("/tt3/")
def totalthr3():
    main.ttgraphar(main.ttcalc("databaseCsv"),main.ttcalc("databaseCsv2"))
    return render_template("FrontEnd/f3/totalthr2.html")

@app.route("/dt3/")
def downtime3():
    main.dtgraphar(main.dtcalc("databaseCsv"),main.dtcalc("databaseCsv2"))
    return render_template("FrontEnd/f3/downtime2.html")

@app.route("/f1/")
def f1():
    main.collective("databaseCsv")
    return render_template("FrontEnd/f1/Mainpage.html",
                           ppm=round(
                               main.ochange(main.ppmcalc("databaseCsv")) / main.ochange(main.expectedouptput) * 100, 2),
                           pro=round(
                               (main.prodcalc("databaseCsv")[1]) / main.ochange(main.prodcalc("databaseCsv")) * 100, 2),
                           tt=round(main.ochange(main.ttcalc("databaseCsv")) / ((main.ochange(main.expectedouptput)) / (
                               main.ttcalc("databaseCsv").__len__())) * 100, 2),
                           dt=round(main.ochange(main.dtcalc("databaseCsv")) / (
                                       main.dtcalc("databaseCsv").__len__() * 600) * 100, 2),
                           w=round(main.ochange(main.ppmcalc("databaseCsv")), 2),
                           x=round(main.prodcalc("databaseCsv")[1], 2),
                           y=round(main.ochange(main.ttcalc("databaseCsv")), 2),
                           z=round(main.ochange(main.dtcalc("databaseCsv")), 2))

@app.route("/f2/")
def f2():
    main.collective("databaseCsv2")
    return render_template("FrontEnd/f2/Mainpagef2.html",
                           ppm=round(
                               main.ochange(main.ppmcalc("databaseCsv2")) / main.ochange(main.expectedouptput) * 100,
                               2),
                           pro=round(
                               (main.prodcalc("databaseCsv2")[1]) / main.ochange(main.prodcalc("databaseCsv2")) * 100, 2),
                           tt=round(main.ochange(main.ttcalc("databaseCsv2"))/((main.ochange(main.expectedouptput))/(main.ttcalc("databaseCsv2").__len__()))*100,2),
                           dt=round(main.ochange(main.dtcalc("databaseCsv2")) / (
                                   main.dtcalc("databaseCsv2").__len__() * 600) * 100, 2),
                           w=round(main.ochange(main.ppmcalc("databaseCsv2")), 2),
                           x=round(main.prodcalc("databaseCsv2")[1],2),
                           y=round(main.ochange(main.ttcalc("databaseCsv2")), 2),
                           z=round(main.ochange(main.dtcalc("databaseCsv2")), 2))

@app.route("/f3/")
def f3():
    main.ppmgraphar(main.ppmcalc("databaseCsv"), main.ppmcalc("databaseCsv2"))
    main.prodgraphar(main.prodcalc("databaseCsv"), main.prodcalc("databaseCsv2"))
    main.ttgraphar(main.ttcalc("databaseCsv"), main.ttcalc("databaseCsv2"))
    main.dtgraphar(main.dtcalc("databaseCsv"), main.dtcalc("databaseCsv2"))
    return render_template("FrontEnd/f3/Mainpagef2.html",
                           ppm=round(
                               main.ochange(main.average(main.ppmcalc("databaseCsv"),
                                                         main.ppmcalc("databaseCsv2"))) / main.ochange(
                                   main.expectedouptput) * 100, 2),
                           pro=round(
                               (main.average(main.prodcalc("databaseCsv"), main.prodcalc("databaseCsv2"))[
                                   1]) / main.ochange(
                                   main.average(main.prodcalc("databaseCsv"), main.prodcalc("databaseCsv2"))) * 100, 2),
                           tt=round(
                               main.ochange(main.average(main.ttcalc("databaseCsv"), main.ttcalc("databaseCsv2"))) / (
                                           (main.ochange(main.expectedouptput)) / (
                                       main.average(main.ttcalc("databaseCsv"),
                                                    main.ttcalc("databaseCsv2")).__len__())) * 100, 2),
                           dt=round(main.ochange(main.average(main.dtcalc("databaseCsv"), main.dtcalc("databaseCsv2"))) / (
                                   main.average(main.dtcalc("databaseCsv"), main.dtcalc("databaseCsv2")).__len__() * 600) * 100, 2),
                           w=round(
                               main.ochange(main.average(main.ppmcalc("databaseCsv"), main.ppmcalc("databaseCsv2"))),
                               2),
                           x=round(main.average(main.prodcalc("databaseCsv"), main.prodcalc("databaseCsv2"))[1], 2),
                           y=round(main.ochange(main.average(main.ttcalc("databaseCsv"), main.ttcalc("databaseCsv2"))),
                                   2),
                           z=round(main.ochange(main.average(main.dtcalc("databaseCsv"), main.dtcalc("databaseCsv2"))),
                                   2))


if __name__ == "__main__":
    app.run()