import math 
import pyslha

from LHTclass import *

sini=pyslha.read('LHTset.ini', ignorenobr=True, ignorenomass=True)
ff=sini.blocks['LHT'][1]
rr=sini.blocks['LHT'][2]
kaq1=sini.blocks['LHT'][3]
kaq2=sini.blocks['LHT'][4]
kaq3=sini.blocks['LHT'][5]
kal1=sini.blocks['LHT'][6]
kal2=sini.blocks['LHT'][7]
kal3=sini.blocks['LHT'][8]

o = param(ff,rr,kaq1,kaq2,kaq3,kal1,kal2,kal3);
print("sH,cH,v,lam2,xL,d2,lamphi2,lamhphiphih,lamphi2phi2,lamphi4", 
       o.cH, o.v, o.lam2, o.xL, o.d2, o.lamphi2, o.lamhphiphih, o.lamphi2phi2, o.lamphi4);

print("MAH, MWH, MZH, MHve, MHvm, MHvt, MHe, MHmu, MHta, MHu, MHc, MHt, MHd, MHs, MHb, MHTodd, MHTeven, MPhi0, MPhiP, MPhiC, MPhiCC", o.MAH, o.MWH, o.MZH, o.MHve, o.MHvm, o.MHvt, o.MHe, o.MHmu, o.MHta, o.MHu, o.MHc, o.MHt, o.MHd, o.MHs, o.MHb, o.MHTodd, o.MHTeven, o.MPhi0, o.MPhiP, o.MPhiC, o.MPhiCC)


print(aEW)
o.writespec("param_card.dat")
