#!/usr/bin/env python

import matplotlib.pyplot as plt
import pyedflib
import numpy as np
import re
import ast

sf = None
f = None
sigbufs = None
signal_labels = None

def setSource(filepath):
	global sf
	global f
	sf = filepath
	f = pyedflib.EdfReader(sf+".edf")
	return sf
	
def getData():
	global sf
	global f
	global sigbufs
	global signal_labels
	n = f.signals_in_file
	signal_labels = f.getSignalLabels()
	sigbufs = np.zeros((n, f.getNSamples()[0]))
	for i in np.arange(n):
		sigbufs[i, :] = f.readSignal(i)
	return sigbufs

def listCh():
	global signal_labels
	return signal_labels

def readlbl():
	global sf
	with open(sf+'.lbl', 'r') as myfile:
		data=myfile.read()
	return data

def lblSection(rawinput):
	#split into 5 section version,montage,level,symbols,and label.
	section = re.split(r'\n{2,}',rawinput)
	return section

def mtgList(rawmtg):
	montages = re.split(r'\n',rawmtg)
	return montages

def mtgLbl(montage):
	label = montage.split(",")[1].split(":")[0].strip()
	return label

def mtgIn1(montage):
	input1 = montage.split(",")[1].split(":")[1].split("--")[0].strip()
	return input1

def mtgIn2(montage):
	input2 = montage.split(",")[1].split(":")[1].split("--")[1].strip()
	return input2

def chIdx(inputch,chname):
	for index, item in enumerate(chname):
		if item.strip() == inputch:
			return index

def diffamp(a,b):
	#the differential amplifier
	c = []
	for i in range(0,len(a)):
		if a[i] == b[i]:
			c.append(0)
		else:
			c.append(max(a[i],b[i]))
	return c

def evntListonMotages(rawsymbols,rawevents,idxmontages):
	events = evntList(rawevents)
	temp = []
	for event in events:
		if event != "":
			if evntMtg(event) == idxmontages:
				evid = evntId(event)
				evname = getEvntName(evid,rawsymbols)
				estrart = eventStart(event)
				estop = eventStop(event)
				temp.append(evname+","+str(estrart)+","+str(estop))
	return temp
		
def plotCh(Title,sinyal,eventlist):
	for event in eventlist:
		ev=event.split(",")
		plt.plot([float(ev[1]),float(ev[2])],[0,0], label=ev[0])
	plt.plot(sinyal)
	plt.ylabel('microVolts')
	plt.xlabel('ms')
	plt.title(Title)
	plt.axis([0, len(sinyal), min(sinyal), max(sinyal)])
	plt.legend()
	plt.show()
	
def evntList(rawevents):
	events = re.split(r'\n',rawevents)
	return events
	
def evntMtg(event):
	idxmtg= event.split("=")[1].split(",")[4].strip()
	return int(idxmtg)
	
def evntId(event):
	ngok = event.split("=")[1].split("[")[1].split("]")[0].split(",")
	for index, item in enumerate(ngok):
		if item.strip() == "1.0":
			return index
	
def eventStart(event):
	return float(event.split(",")[2])
	
def eventStop(event):
	return float(event.split(",")[3])
	
def getEvntName(idx,symbol):
	eventDict = eval(symbol.split("=")[1])
	return eventDict[idx]
		
def infoData():
	global sigbufs
	infodt = "Channel : "+str(len(sigbufs))+"; Time(ms) : "+str(len(sigbufs[0]))
	return infodt
	
