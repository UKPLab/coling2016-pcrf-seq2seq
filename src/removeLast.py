#! /usr/bin/python

import sys

for line in sys.stdin:
  line = line.strip()
  a,b = line.split()
  print "%s\t%s"%(a[:-1],b[:-1])
