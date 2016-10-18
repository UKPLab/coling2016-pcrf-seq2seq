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
  joinSym=""
  for i in xrange(-window,window-n+2,1):
    #print "s%d:"%(counter) + "/".join(["%%x[%d,%d]"%(i+j,stringIndex) for j in xrange(n)])
    f = []
    for j in xrange(n):
      if stringIndex+i+j>=0 and stringIndex+i+j<m:
        f.append( mystring[stringIndex+i+j] )
      else:
        f.append( "-" )
    features.append( "feat_%d_%d=%s"%(n,integer+counter,joinSym.join(f)) )
    counter += 1
  return features,integer+counter
      


def printForCRF(splittedStrngX,splittedStrngY=None):
    #strAsList = [x for x in str]
    window = WINDOW # NUMBER MUST MATCH WITH NUMBER IN makeSeg.py in the decoder
    N = MY_N # NUMBER MUST MATCH WITH NUMBER IN makeSeg.py in the decoder
    for i in xrange(len(splittedStrngX)):
	globalCounter = 0
	allFeatures = []
        for n in xrange(1,N+1,1):
          features,globalCounter = createNgramTemplate(globalCounter,splittedStrngX,n,window,i)
	  globalCounter = 0
	  allFeatures += features
	  #print n,features
	try:
          if splittedStrngY!=None:
            print "%s\t%s\t%s"%(splittedStrngX[i].encode("utf-8"),splittedStrngY[i].encode("utf-8"),"#".join(allFeatures).encode("utf-8"))
          else:
            print "%s\t%s"%(splittedStrngX[i].encode("utf-8"),"#".join(allFeatures).encode("utf-8"))
	except IndexError:
	  sys.stderr.write("ERROR:%s\t%s\n"%(" ".join(splittedStrngX)," ".join(splittedStrngY))) #b,str
	  sys.exit(1)


if __name__ == "__main__":

    splitSym="-"
    splitSym="|"
    coding = "utf-8"
    #coding = "latin-1"
    i = 0
    for line in sys.stdin.readlines():
	if i%100==0:
	  sys.stderr.write("\r>>%d"%i)
	#if i>20000: break
	try:
          line = line.decode(coding)
	except UnicodeDecodeError:
	  sys.stderr.write("FAULTY LINE (%d):|%s|\n"%(i,line))
	  sys.exit(1) 
        try:
            x,y = line.strip().split("\t")
        except ValueError:
            x = line.strip()
	if x.strip()=="": continue
        printForCRF(x.split(splitSym),y.split(splitSym))
        print
	i+=1
