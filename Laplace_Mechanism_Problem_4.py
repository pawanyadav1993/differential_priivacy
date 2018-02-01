import csv
import sys  
import math
import numpy as np
from pandas import Series
import matplotlib.pyplot as plt
from Tkinter import Tk
import tkFileDialog
import matplotlib.patches as mpatches
 
root = Tk()
D = tkFileDialog.askopenfilename(parent=root)
E = tkFileDialog.asksaveasfilename(parent=root)
root.withdraw()

reload(sys)  
sys.setdefaultencoding('utf8')
ifi = open( D, 'rb')
reader = csv.reader(ifi,delimiter='\t')
ofi = open(E, 'wb')
writer = csv.writer(ofi, delimiter='\t')
reader = csv.reader(ifi) 
s=list()
'''
Selecting row 13 "native country" to 
introduce differential privacy
'''
for row in reader:     
        p = row[13]
        s.append(p)
        
ifi.close() 
s = [i.rstrip(' ?') for i in s]
s = [x for x in s if x != '']

for x in s:
    writer.writerow(x)
ofi.close()
q = s.pop(0)
s = Series(s)
vc = s.value_counts()
print vc
d= vc.to_dict()
a = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
b=list()

''' Using laplace mechanism to introduce noise, 
so that data cannot be inferred 
'''
for x in a:
    count = 0
    for i in range(1,51):
        t = vc.to_dict()
        p = 0.0
        for k,v in t.items():
            t[k] = t[k] + np.random.laplace(0,float(1/x))
            p = float(p + float(math.pow((t[k] - d[k]),2)))
        count = count + float(p/len(t))
    b.append(float(count/50))
	
	
print "Different values of Epsilon", a
print "Mean Square Error corresponding to Epsilon values", b
plt.figure()
plt.plot(a,b)
plt.xlabel("Epsilon")
plt.ylabel("Mean Square Error")
plt.title('Histogram for MSE after adding Laplace Noise')
blue_patch = mpatches.Patch(color='blue', label="Epsilon")
plt.legend(handles=[blue_patch])
plt.show()