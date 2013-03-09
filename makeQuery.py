#to run just type: python makeQuery.py 
import ast
import pickle
import re
import sys
import urllib2
import urllib
from xml.dom.minidom import parseString
import math
#copied pearson_def from stackoverflow
def average(x):
    assert len(x) > 0
    return float(sum(x)) / len(x)

def pearson_def(x, y):

    assert len(x) == len(y)
    n = len(x)
    assert n > 0
    avg_x = average(x)
    avg_y = average(y)
    diffprod = 0
    xdiff2 = 0
    ydiff2 = 0
    for idx in range(n):
        xdiff = x[idx] - avg_x
        ydiff = y[idx] - avg_y
        diffprod += xdiff * ydiff
        xdiff2 += xdiff * xdiff
        ydiff2 += ydiff * ydiff
    return diffprod / math.sqrt(xdiff2 * ydiff2)
    

def makeQuery(query):
    #modquery = urllib.urlencode({'q':query})
    #print modquery
    file = urllib2.urlopen('http://api.wolframalpha.com/v2/query?input='+query+'&appid=LRAE88-5AJ25HER8K')
    data = file.read()
    file.close()
    dom = parseString(data)
   
    xmlTag = dom.getElementsByTagName('plaintext')[0].toxml()
    xmlData=xmlTag.replace('<plaintext>','').replace('</plaintext>','')
    physicalUnit = '(physical quantity)'
    if physicalUnit in xmlData:
        xmlData =  xmlData[:xmlData.rfind(physicalUnit)]
        return xmlData
    try:
        unitTag = dom.getElementsByTagName('plaintext')[6].toxml()
        unitData = unitTag.replace('<plaintext>','').replace('</plaintext>','')
        #print unitData
    except:
        return None
    englishWord = '(English word)'
    character = '(character)'
    if englishWord in xmlData or character in xmlData:
        return None
    #xmlData.replace(" ", "")
    return xmlData

var = raw_input("type: ")
lines = var.replace(".", " ").replace(",", " ").replace("?", " ").split()  #lazy regex. will fix later
#print lines
dict = {}
hill, kine, proj, = 'H', 'K', 'P' #hill, kinematics or projectile problem
memoUnit, memoProb, memoHill, memoKine, memoProj = {},{}, {}, {}, {} #memoize for speed

for word in lines:
    readFile1 = open("memoUnit.p", "rb")
    readFile2 = open("memoProb.p", "rb")
    readFile3 = open("hillProb.p", "rb")
    readFile4 = open("kineProb.p", "rb")
    readFile5 = open("projProb.p", "rb")
    
    try: 
        memoUnit = pickle.load(readFile1)
        """
        memoProb = pickle.load(readFile2)
        memoHill = pickle.load(readFile3)
        memoKine = pickle.load(readFile4)
        memoProj = pickle.load(readFile5)
        readFile1.close()
        readFile2.close()
        readFile3.close()
        readFile4.close()
        readFile5.close()
        """
        readFile1.close()
        #print memoUnit
        print ("before ")
        if not word in memoUnit:
            memoUnit[word] = makeQuery(word)
        dict[word] = memoUnit[word]
        
        
        """maxValLen=0
        for counter in range(3):    
           
            if word not in memoHill:
                maxValLen = max([len(memoHill[x]) for x in memoHill])
                memoHill[word] = []
                for count in range(maxValLen):                  
                    memoHill[word].append(0)
                memoHill[word].append(1)
            else:
                if len(memoHill[word]) is maxValLen:
                    memoHill[word].append(memoHill[word][-1] + 1)
                else:
                    i = 0
                    lastVal = memoHill[word][-1] + 1
                    while(len(memoHill[word]) is not maxValLen):
                        memoHill[word].append(0)
                        i+=1
                    else:
                        memoHill[word].append(lastVal)
           
            if word not in memoKine:
                maxValLen = max([len(memoKine[x]) for x in memoKine])
                memoKine[word] = []
                for count in range(maxValLen):                  
                    memoKine[word].append(0)
                memoKine[word].append(1)
            else:
                if len(memoKine[word]) is maxValLen:
                    memoKine[word].append(memoKine[word][-1] + 1)
                else:
                    i = 0
                    lastVal = memoKine[word][-1] + 1
                    while(len(memoKine[word]) is not maxValLen):
                        memoKine[word].append(0)
                        i+=1
                    else:
                        memoKine[word].append(lastVal)
           
            if word not in memoProj:
                maxValLen = max([len(memoProj[x]) for x in memoProj])
                memoProj[word] = []
                for count in range(maxValLen):                  
                    memoProj[word].append(0)
                memoProj[word].append(1)
            else:
                if len(memoProj[word]) is maxValLen:
                    memoProj[word].append(memoProj[word][-1] + 1)
                else:
                    i = 0
                    lastVal = memoProj[word][-1] + 1
                    while(len(memoProj[word]) is not maxValLen):
                        memoProj[word].append(0)
                        i+=1
                    else:
                        memoProj[word].append(lastVal)
    """
    except:
        pass


try:
 
    writeFile=open("memoUnit.p", "wb")
    pickle.dump(memoUnit, writeFile)
    writeFile.close()
except:
    pass
"""
for word in lines:
    modWord = ""
    if dict[word] is not None:
        modWord = dict[word]
        output += modWord + " "
    else:
        output += word + " "
print ("With units added: " + output)
print dict
"""
print dict
