from datetime import date
import matplotlib.pyplot as plt
import mne

raw = mne.io.read_raw_edf("sample-data/00000258_s002_t000.edf", preload=True)
raw.info
raw.info["sfreq"]
print raw.info["ch_names"]
date.fromtimestamp(raw.info["meas_date"])

print mne.channels.get_builtin_montages()

#https://cbrnr.github.io/2017/10/23/loading-eeg-data/


plt.plot(raw._data[-1])