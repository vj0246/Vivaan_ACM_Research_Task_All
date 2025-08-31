#inp=input("Enter the string you ant to format")
#transform_text(inp)
import numpy as np
from datetime import datetime as dt
from dateutil import parser

def redacter(i):
    l=len(i)
    str="******"
    for j in i[-4:]:
        str=str+j
    return str

def transform_text(str):
    str=str.strip() 
    arr=str.split()
    for i in arr:
        if(i=="Python"):
            i=i.replace("Python","🐍")
            continue
        count=0
        for j in i:
            if j.isdigit():
                count+=1
            elif j=='-':
                break
        if count==5:
            i=i.replace(i,redacter(i))
        elif count==4:
            date=i.split('-')[-1]
            lst1=list(["1","21","31"])
            lst2=list(["2","22"])
            lst3=list(["3","23"])
            if date in lst1:
                add_on="st"
            elif date in lst2:
                add_on="nd"
            elif date in lst3:
                add_on="rd"
            else:
                add_on="th"
            date_obj = parser.parse(i)#chatgpt
            i=i.replace(i,date_obj.strftime(f"%d{add_on}  %B %Y"))
        print(i,end=" ")
        
inp=input("Enter the string you want to format:")
transform_text(inp)