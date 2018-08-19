#!/usr/bin/env python

from datetime import date
import matplotlib.pyplot as plt
import pyedflib
import numpy as np
import re
import ast

sf = None
raw = None
f = None
sigbufs = None
signal_labels = None

def setSource(filepath):
	global sf
	global raw
	global f
	sf = filepath
	#raw = mne.io.read_raw_edf(filepath, preload=True)
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
	
def infoData():
	global sigbufs
	infodt = "Channel : "+str(len(sigbufs))+"; Time(ms) : "+str(len(sigbufs[0]))
	return infodt

def plotCh(sinyal):
	plt.plot(sinyal)
	plt.plot(3000,0, color="green", linewidth=1.0, linestyle="-")
	plt.ylabel('microVolts')
	plt.xlabel('ms')
	plt.title('Judul')
	plt.axis([0, len(sinyal), min(sinyal), max(sinyal)])
	plt.legend()
	plt.show()

def addEvent(x1,x2):
	sq=[x1,x2],[0,0]

def diffamp(a,b):
	#the differential amplifier
	c = a
	for i in range(0,len(a)):
		print "a: "+str(a[i])+", b: "+str(b[i])
		if a[i] == b[i]:
			c[i]=0
			print "nolkan index ke"+str(i)
			print c[i]
		else:
			c[i]=max(a[i],b[i])
			print "maksimalkan indek ke"+str(i)
			print c[i]
	return c

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

def mtgIn2():
	input2 = montage.split(",")[1].split(":")[1].split("--")[1].strip()
	return input2

def evntList(rawevents):
	events = re.split(r'\n',rawevents)
	return events
	
def evntMtg(event):
	return event.split("=")[1].split(",")[4].strip()
	
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
		
	
