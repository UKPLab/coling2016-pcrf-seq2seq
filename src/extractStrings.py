#! /usr/bin/python

import sys

chars = []
preds = []
EMPTY="EMPTY"

for line in sys.stdin:
    line = line.strip()
    if line=="":
        print "%s\t%s"%(" ".join(chars)," ".join(preds))
        chars = []
        preds = []
    else:
        x = line.split("\t")
        char = x[1]
        pred = x[5]
	#if pred[-1] in ["0","1","2"]: pred = pred[:-1]
	if char!=EMPTY:
          chars.append(char)
	if pred!=EMPTY:
          preds.append(pred)
