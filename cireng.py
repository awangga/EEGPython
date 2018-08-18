#!/usr/bin/env python

from datetime import date
import matplotlib.pyplot as plt
import mne
import pyedflib
import numpy as np

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
	raw = mne.io.read_raw_edf(filepath, preload=True)
	f = pyedflib.EdfReader(sf)
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
	
def getChNames():
	global raw
	return raw.info["ch_names"]

def getMDate():
	global raw
	return date.fromtimestamp(raw.info["meas_date"])
	
def getRaw():
	global raw
	return raw
	
def infoData():
	global sigbufs
	infodt = "Channel : "+str(len(sigbufs))+"; Time(ms) : "+str(len(sigbufs[0]))
	return infodt

def plotCh(sinyal):
	plt.plot(sinyal)
	plt.ylabel('microVolts')
	plt.xlabel('ms')
	plt.axis([0, 8000, -100, 200])
	plt.show()
	
	
	
	
	
	
	
	
	
