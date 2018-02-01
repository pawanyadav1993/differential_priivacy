import csv
import sys  
from pandas import Series
import matplotlib.pyplot as plt
from Tkinter import Tk
import tkFileDialog
import matplotlib.patches as mpatches

root = Tk()
D = tkFileDialog.askopenfilename(parent=root)
root.withdraw()
idx = int(input("Enter the value of idx for Discrete attributes, which include 2 4 6 8 9 10 14 \n"))

''' Function to generate histogram 
on discrete data
'''
def BuildHistogram(D,idx):
    reload(sys)  
    sys.setdefaultencoding('utf8')
    ifi = open( D, 'rb')
    reader = csv.reader(ifi,delimiter='\t')
    reader = csv.reader(ifi) 
    s=list()
    for row in reader:     
            p = row[idx-1]
            s.append(p)
        
    ifi.close() 
    s = [i.rstrip(' ?') for i in s]
    s = [x for x in s if x != '']
    q = s.pop(0)
    s = Series(s)
    vc = s.value_counts()
    print vc
    plt.figure()
    fig = vc.plot(kind='bar')
    fig.set_title("Histogram")
    fig.set_xlabel(q)
    fig.set_ylabel("Count")
    blue_patch = mpatches.Patch(color='blue', label=q)
    plt.legend(handles=[blue_patch])
    plt.show()

BuildHistogram(D,idx)