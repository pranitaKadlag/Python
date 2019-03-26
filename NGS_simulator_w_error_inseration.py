#!/usr/bin/python

import re
import random		

dataSize = int(input())
readLength = int(input())
errorRate = 0.01

header = seq = completeGenomeSeq = ""
chrDict = {"chr" : [], "start" : [], "end": []}
dictForError = {}
dictforReadInfo = {}

phredQuality = {"0":"!", "1":"\"", "2":"#", "3":"$", "4":"%", "5":"&", "6":"'", "7":"(", "8":")", "9":"*", "10":"+", "11":",", "12":"-", "13":".", "14":"/", "15":"0", "16":"1", "17":"2", "18":"3", "19":"4", "20":"5", "21":"6", "22":"7", "23":"8", "24":"9", "25":":", "26":";", "27":"<", "28":"=", "29":"?", "30":"?", "31":"@", "32":"A", "33":"B", "34":"C", "35":"D", "36":"E", "37":"F", "38":"G", "39":"H", "40":"I", "41":"J"}

def get_header(readCounter,startPos, endPos):
	for i in range(len(chrDict["chr"])):
		if((startPos <= chrDict["end"][i]) and (endPos >= chrDict["start"][i])):
			return "@Read_" + str(readCounter) + ":" + chrDict["chr"][i] + ":" + str(startPos) + ":" + str(endPos) + ":length" + str(readLength)
def getPhredScore():
	phredStr = ""
	for i in range(readLength):
		phredStr += phredQuality["" + str(random.randint(0,41))]
	return phredStr

for line in open("input.fasta", "r"):
	line = line.strip()
	if(re.match(">", line)):
		if(len(completeGenomeSeq) != 0):
			if(len(chrDict["chr"]) == 0):
				chrDict["start"].append(0)
				chrDict["end"].append(len(completeGenomeSeq))
			else:
				chrDict["start"].append(chrDict["end"][-1])
				chrDict["end"].append(len(completeGenomeSeq))
			chrDict["chr"].append(header)
		header = line.replace(">", "")
	else:
		completeGenomeSeq += line

chrDict["chr"].append(header)
chrDict["start"].append(chrDict["end"][-1])
chrDict["end"].append(len(completeGenomeSeq))

fwrite = open("simulated.reads.orig.fq", "w")

for i in range(dataSize):
	randNo = random.randint(0,len(completeGenomeSeq))
	phredQual = getPhredScore()
	
	dictforReadInfo[i] = {}
	dictforReadInfo[i][0] = get_header(i + 1, randNo, randNo + readLength)
	dictforReadInfo[i][1] = completeGenomeSeq[randNo:(randNo + readLength)]
	dictforReadInfo[i][2] = "+"
	dictforReadInfo[i][3] = phredQual
	fwrite.write(get_header(i + 1, randNo, randNo + readLength) + "\n" + completeGenomeSeq[randNo:(randNo + readLength)] + "\n+\n" + phredQual + "\n")

fwrite.close()

for i in range(readLength):
	for index in random.sample(range(dataSize), int(dataSize*errorRate)):
		ntList = ["A", "T", "G", "C", "N"]
		tempList = list(dictforReadInfo[index][1])
		
		if(dictforReadInfo[index][1][i] in ntList):	#handle exception for unusual bases like W, R, Y etc
			ntList.remove(dictforReadInfo[index][1][i])
			tempList[i] = ntList[random.randint(0,len(ntList)-1)]
		else:
			tempList[i] = ntList[random.randint(0,len(ntList)-1)]
		dictforReadInfo[index][1] = ''.join(tempList)
		
fwrite = open("final.simulated.reads.w.random.errors.fq", "w")

for header in dictforReadInfo:
	fwrite.write(dictforReadInfo[header][0] + "\n" + dictforReadInfo[header][1] + "\n" + dictforReadInfo[header][2] + "\n" + dictforReadInfo[header][3] + "\n")

fwrite.close()
