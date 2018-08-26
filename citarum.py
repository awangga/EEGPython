#python eeg using mne
#https://cbrnr.github.io/2017/10/23/loading-eeg-data/
import mne
raw = None

def open(filename):
	global raw
	raw = mne.io.read_raw_edf(filename, preload=True)
	return raw
	
def info():
	global raw
	return raw.info
	
def getSF():
	global raw
	return raw.info["sfreq"]
	
def getBads():
	global raw
	return raw.info["bads"]
	
def getChNames():
	global raw
	return raw.info["ch_names"]
	
def getChProperties():
	global raw
	return raw.info["chs"]

def getHighPass():
	global raw
	return raw.info["highpass"]
	
def getRecDate():
	global raw
	return raw.info["meas_date"]