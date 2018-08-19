import cireng

cireng.setSource("dt/2")
chdata = cireng.getData()
chname = cireng.listCh()
labelfile=cireng.readlbl()
lblsection=cireng.lblSection(labelfile)
montages=cireng.mtgList(lblsection[1])
#select 1 montages for example
label = cireng.mtgLbl(montages[0])
input1 = cireng.mtgIn1(montages[0])
input2 = cireng.mtgIn2(montages[0])
idx1 = cireng.chIdx(input1,chname)
idx2 = cireng.chIdx(input2,chname)
bip=cireng.diffamp(chdata[idx1],chdata[idx2])
#get event in montage 0	
eventlist = cireng.evntListonMotages(lblsection[4],lblsection[5],0)
#plotting data
cireng.plotCh(input1+"-"+input2,bip,eventlist)