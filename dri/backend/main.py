import os
import matplotlib.pyplot as pl
import pandas as pd
import plotly.express as px
import numpy as np

PPMfile = open("databaseCsv/pmdci_data.csv").readlines()
direct = open("Workerinput/ceiling.csv")

# arrays arrays for days

PPMs = []
PPMf = []


# Combines relevant data and creates a list Matrices
def mat():
    TheL = []
    x = 0
    D = os.listdir("Workerinput")
    while x < D.__len__():
        TheL.append(ar(open("Workerinput/"+str(D[x])).readlines()))
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
def specify(arr, column):
    ob = []
    x = 1
    while x < arr.__len__():
        ob.append(arr[x][column])
        x = x + 1
    return ob


# Collects failure and successes
def ppmcol():
    mat()
    overall = []
    x = 0
    while x < mat().__len__():
        success = specify(mat()[x], 3)
        fail = specify(mat()[x], 4)
        overall.append(success)
        overall.append(fail)
        x = x + 1
    return overall



# Separates success from failures
#def ppmv(thelist):
#    x = 1
#    y = 2
#    while y < thelist[1].__len__():
#        PPMs.append(add(thelist, x))
#        PPMf.append(add(thelist, y))
#        x = x + 2
#        y = y + 2


def ppmg(theList):
    print("Success: " + str(PPMs))
    print("Fail: " + str(PPMf))
    x = np.arange(len(PPMs))
    fig, ax = pl.subplots()
    Sbar = ax.bar(x - 0.4/2, PPMs, 0.4, label="Successes")
    Fbar = ax.bar(x + 0.4/2, PPMf, 0.4, label="Failures")
    ax.bar_label(Sbar, padding=2)
    ax.bar_label(Fbar, padding=2)
    pl.show()


if __name__ == '__main__':
    print(ar(PPMfile))
    print(ppmcol())
