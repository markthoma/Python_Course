#!/usr/bin/python3.6

import glob2
import datetime

files = glob2.glob("*.txt")

with open(datetime.datetime.now().strftime("%Y-%m-%d")+".txt",'a+') as filename:
    for i in files:
        with open(i,'r') as f:
            filename.write(f.read()+"\n")
