import csv
import sys  
from pandas import Series
import matplotlib.pyplot as plt
from Tkinter import Tk
import tkFileDialog
import matplotlib.patches as mpatches
import math
import random
 
root = Tk()
D = tkFileDialog.askopenfilename(parent=root)
root.withdraw()

reload(sys)  
sys.setdefaultencoding('utf8')
ifi = open( D, 'rb')
reader = csv.reader(ifi,delimiter='\t')
reader = csv.reader(ifi) 
s=list()
for row in reader:     
        p = row[13]
        s.append(p)
        
ifi.close() 
s = [i.rstrip(' ?') for i in s]
s = [x for x in s if x != '']
q = s.pop(0)
s = Series(s)
vc = s.value_counts()
print vc
d= vc.to_dict()
a = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0] 
''' Different values of eplison, 
based on which noise is added
'''
b=list()
t = vc.to_dict()
c = 0.0


for k,v in t.items():
     c = c + t[k]
     b.append(int(t[k]))
p = 0.0
e = list()


for k,v in d.items():              #Finding the true probabiltiy
    p = float(d[k])/c
    e.append(p)    
cou = 0

'''Different values assigned,
 based on probability 0-1
 '''
for k,v in t.items():
     t[k] = e[cou]
     cou += 1
vt = Series(t)
t = vt.to_dict()  
for k,v in t.items():
     if t[k]>0.9:
         t[k] = 10
     elif t[k]>0.02:
         t[k] = 3
     elif t[k]>0.003:
         t[k] = 2
     else: t[k] = 1
t= Series(t)
t = t.to_dict()
m = list()

''' Based on Exponential mechanism 
adding noise and prediction value
'''
for x in a:
    count = 0.0
    for i in range(1,101):
        q = vt.to_dict()
        p = 0.0
        w=list()
        v=0.0
        for k,v in q.items():
            q[k] = math.exp((x*q[k])/0.2)
            p = p + q[k]
        for k,v in q.items():
            q[k] = ((q[k])/p) 
            w.append(q[k])
        j = random.uniform(0, 1)
        print j
        if j < q.get(' United-States'):
            count = count + 1
        print count
    m.append(count)

print "Different values of Epsilon", a
print "Fraction Counted corresponding to Epsilon value", m
plt.figure()
plt.plot(a,m)
plt.xlabel("Epsilon")
plt.ylabel("Fraction Count")
plt.title('Histogram for Exponential Mechanism For Predicting Most common native-country')
blue_patch = mpatches.Patch(color='blue', label="Epsilon")
plt.legend(handles=[blue_patch])
plt.show()