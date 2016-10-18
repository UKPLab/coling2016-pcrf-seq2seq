#! /usr/bin/python

import sys

try:
  WINDOW = int(sys.argv[1])
  MY_N = int(sys.argv[2])
except IndexError:
  WINDOW = 6
  MY_N = 6


def createNgramTemplate(integer,mystring,n,window,stringIndex):
  counter = 0
  m = len(mystring)
  features = []
  for i in xrange(-window,window-n+2,1):
    #print "s%d:"%(counter) + "/".join(["%%x[%d,%d]"%(i+j,stringIndex) for j in xrange(n)])
    f = []
    for j in xrange(n):
      if stringIndex+i+j>=0 and stringIndex+i+j<m:
        f.append( mystring[stringIndex+i+j] )
      else:
        f.append( "-" )
    features.append( "feat_%d_%d=%s"%(n,integer+counter,"".join(f)) )
    counter += 1
  return features,integer+counter
      

def printForCRF(splittedStrng):
    str = "".join(splittedStrng)
    #b = splittedString2Binary(splittedStrng)
    #print splittedStrng,b
    strAsList = [x for x in str]
    strAsList = splittedStrng
    window = WINDOW
    N = MY_N
    #globalCounter = 0
    for i in xrange(len(strAsList)):
	globalCounter = 0
	allFeatures = []
        for n in xrange(1,N+1,1):
          features,globalCounter = createNgramTemplate(globalCounter,strAsList,n,window,i)
	  globalCounter = 0
	  allFeatures += features
	  #print n,features
	try:
          print "%s\t%s\t%s"%(strAsList[i].encode("utf-8"),strAsList[i].encode("utf-8"),"#".join(allFeatures).encode("utf-8"))
	except IndexError:
	  print b,str
	  sys.exit(1)


if __name__ == "__main__":

    splitSym="-"
    splitSym=" "
    encoding = "utf-8"
    #encoding = "latin1"

    for line in sys.stdin.readlines():
        line = line.decode(encoding)
        try:
            x,y = line.strip().split("\t")
        except ValueError:
            x = line.strip()
	if x.strip()=="": continue
        printForCRF(x.split(splitSym))
        print
