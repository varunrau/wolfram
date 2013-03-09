import re
import sys
import urllib2
import urllib
from xml.dom.minidom import parseString

def makeQuery(query):
    #modquery = urllib.urlencode({'q':query})
    #print modquery
    file = urllib2.urlopen('http://api.wolframalpha.com/v2/query?input='+query+'&appid=LRAE88-5AJ25HER8K')
    data = file.read()
    file.close()
    dom = parseString(data)

    xmlTag = dom.getElementsByTagName('plaintext')[0].toxml()
    xmlData=xmlTag.replace('<plaintext>','').replace('</plaintext>','')

    try:
        unitTag = dom.getElementsByTagName('plaintext')[10].toxml()
        unitData = unitTag.replace('<plaintext>','').replace('</plaintext>','')
    except:
        return None

    physicalUnit = '(physical quantity)'
    if physicalUnit in xmlData:
        xmlData = xmlData[:xmlData.rfind(word)]
    englishWord = '(English word)'
    if englishWord in xmlData:
        return None
    return xmlData

var = raw_input("type: ")
lines = var.split()
dict = {}
for word in lines:
    dict[word] = makeQuery(word)
print dict
