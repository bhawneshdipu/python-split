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
    '''split each data with : and get the index and value'''
    split_value=[(lambda x: x.split(":"))(x) for x in pythondata]
    max_col=-1#set to -1
    ''' get all the split_values except 1st one as it is a filename'''
    split_value=split_value[1:]
    #print(value)
    for row in value:
        '''
        if the split_value in 1 index is not 'yes' then it is a feature value 
            so increment the max_column count; 
        else  
            if we get first yes keyword then the first row ends, we get our
            max_column value
        '''
        if(row[1]!='yes'):
            max_col+=1
        else:
            max_col+=1
            break;
    '''
        k is index to traverse the list until k>=len(value)
    '''
    k=0
    ''' final_value is result list of list'''
    final_value=[]
    ''' get the value attribute of the list value which is value[i][1] for each i'''
    value_list=[(lambda x: x[1])(x) for x in split_value]
    #print(value_data)
    ''' labels list which contains the labels of training data'''
    labels=[] 
    ''' testdata contains the data to be tested in the classifier'''
    testdata=[]
    while(k<len(value_list)):
        value_row=[]
        for j in range(max_col+1):
            if(value_list[k].lower()=='yes'):
                labels.append(0)
            elif(value_list[k].lower()=='no'):
                labels.append(1)
            elif(value_list[k]==''):
                pass
            else:
                value_row.append(value_list[k])
            k+=1
            if(k>=len(value_list)):
                ''' no more element break the loop'''
                break;
        final_value.append(value_row)
        if(k>=len(value_list)):
                ''' no more element to iterate break the loop'''
                break;
    ''' the testdata contains the last list of final_value'''
    testdata.append(final_value[-1])
    '''the final_value list contains the features list except the last list in final_value''' 
    features=final_value[:-1]
    return features,labels,testdata



if __name__ == "__main__":
    '''imports from php'''
    who = sys.argv
    
    '''turns json data into string'''
    json_string = json.dumps(who)
    pythondata = json.loads(json_string)
    #print(json_string)
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
    
    '''
    pythondata=['test.py', 
     '00:2', '01:67', '02:12', '03:20000','04:1444','05:15478','06:0555', '04:yes',
     '10:5', '11:54', '12:14', '13:45000','04:1444','05:15478','06:0555', '14:yes',
     '20:12', '21:60', '22:45', '23:450000','04:1444','05:15478','06:0555', '24:no', 
     '30:10', '31:50', '32:20', '33:100000','04:1444','05:15478', '34:']
    '''
    
    
   
    features,labels,testdata=prepare_data(pythondata)
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features, labels)
    answer = clf.predict(testdata)
    
    
    if answer == 0:
        print('yes')
    else:
        print('no')
