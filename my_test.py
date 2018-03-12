#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 06:24:43 2018

@author: dipu
"""

#!/anaconda3/bin/python


import json
import requests
import sys
from sklearn import tree
import cgi


def prepare_data(pythondata):
    value=[(lambda x: x.split(":"))(x) for x in pythondata]
    max_row=-1
    max_col=-1
    value=value[1:]
    for row in value:
        if(row[1]!='yes'):
            max_col+=1
        else:
            max_col+=1
            break;
    max_row=int(len(value)/(max_col+1))    
    k=0
    final_value=[]
    #value_data=[(lambda x: 1 if(x[1]=='yes') else(0 if x[1]=='no' else int(x[1])))(x) for x in value] 
    value_data=[(lambda x: x[1])(x) for x in value]
    labels=[] 
    testdata=[]
    for i in range(max_row):
        value_row=[]
        for j in range(max_col+1):
            if(value_data[k]=='yes'):
                labels.append(1)
            elif(value_data[k]=='no'):
                labels.append(0)
            elif(value_data[k]==''):
                pass
            else:
                value_row.append(value_data[k])
            k+=1
            if(k>=len(value_data)):
                break;
        final_value.append(value_row)
        if(k>=len(value_data)):
                break;
    testdata.append(final_value[-1])
    return final_value[:-1],labels,testdata


'''imports from php'''
who = sys.argv

'''turns json data into string'''
json_string = json.dumps(who)
pythondata = json.loads(json_string)

''' Gets data from json and splits it into individual "x:x" vars
a = who[1]
b = who[2]
c = who[3]
d = who[4]
e = who[5]
f = who[6]
g = who[7]
h = who[8]
i = who[9]
j = who[10]
k = who[11]
l = who[12]
m = who[13]
n = who[14]
o = who[15]
p = who[16]
q = who[17]
r = who[18]
s = who[19]
t = who[20]
'''


'''splits individual "x:x" vars into 2 seperate vars
A1,A2 = a.split(':')
B1,B2 = b.split(':')
C1,C2 = c.split(':')
D1,D2 = d.split(':')
E1,E2 = e.split(':')

if E2 == 'yes':
    E3 = 0
else:
    E3 = 1

F1,F2 = f.split(':')
G1,G2 = g.split(':')
H1,H2 = h.split(':')
I1,I2 = i.split(':')
J1,J2 = j.split(':')

if J2 == 'yes':
    J3 = 0
else:
    J3 = 1

K1,K2 = k.split(':')
L1,L2 = l.split(':')
M1,M2 = m.split(':')
N1,N2 = n.split(':')
O1,O2 = o.split(':')

if O2 == 'yes':
    O3 = 0
else:
    O3 = 1

P1,P2 = p.split(':')
Q1,Q2 = q.split(':')
R1,R2 = r.split(':')
S1,S2 = s.split(':')
T1,T2 = t.split(':')







machine learning bit
features = [[A2, B2, C2, D2,], [F2, G2, H2, I2], [K2, L2, M2, N2]]
labels = [E3, J3, O3]'''

pythondata=['test.py', 
 '00:2', '01:67', '02:12', '03:20000','04:1444','05:15478','06:0555', '04:yes',
 '10:5', '11:54', '12:14', '13:45000','04:1444','05:15478','06:0555', '14:yes',
 '20:12', '21:60', '22:45', '23:450000','04:1444','05:15478','06:0555', '24:no', 
 '30:10', '31:50', '32:20', '33:100000','04:1444','05:15478','06:0555', '34:']




features,labels,testdata=prepare_data(pythondata)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
answer = clf.predict(testdata)


if answer == 0:
    print('yes')
else:
    print('no')
