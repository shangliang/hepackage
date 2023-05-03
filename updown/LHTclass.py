import math

MW = 80.385;
MZ = 91.1876;
Me = 5.11e-4;
MM = 0.10566;
MTA = 1.777;
MU = 2.55e-3;
MC = 1.27;
MT = 172;
MD = 5.04e-3;
MS = 0.101;
MB = 4.7;
MH = 125;

aEWM1 = 127.9;
Gf = 1.16637e-5;
aS = 0.1184;
ymdo = 5.04e-3;
ymup = 2.55e-3;
yms = 0.101;
ymc = 1.27;
ymb	= 4.7;
ymt	= 172;
yme = 5.11e-4;
ymm	= 0.10566;
ymtau = 1.777;
cabi = 0.227736; #unit is "rad" here.

aEW = 1/aEWM1;
sw2 = 1-(MW/MZ)**2;
ee = (4*math.pi*aEW)**0.5;
cw = (1-sw2)**0.5;
sw = sw2**0.5;
gw = ee/sw;
g1 = ee/cw;
gs = (4*math.pi*aS)**0.5;
vev = 2*MW*sw/ee;
lam	= MH**2/(2*vev**2);
muH = (vev**2*lam)**0.5;
ye = 2**0.5*yme/vev;
ym = 2**0.5*ymm/vev;
ytau = 2**0.5*ymtau/vev;
yup = 2**0.5*ymup/vev;
yc = 2**0.5*ymc/vev;
yt = 2**0.5*ymt/vev;
ydo = 2**0.5*ymdo/vev;
ys = 2**0.5*yms/vev;
yb = 2**0.5*ymb/vev;
CKM11 = math.cos(cabi);
CKM12 = math.sin(cabi);
CKM13 = 0;
CKM21 = -math.sin(cabi);
CKM22 = math.cos(cabi);
CKM23 = 0;
CKM31 = 0;
CKM32 = 0;
CKM33 = 1;

g1I	= 2**0.5*g1;
gwI = 2**0.5*gw;
xH = 5./4*(gw*g1)/(5*gw**2 - g1**2);

class param:

	def __init__(self, in1=1500., in2=0.2, in3=1., in4=1., in5=1., in6=1., in7=1., in8=1.):
		self.F = in1; #F>1TeV
		self.R = in2;
		self.kaq1 = in3;
		self.kaq2 = in4;
		self.kaq3 = in5;
		self.kal1 = in6;
		self.kal2 = in7;
		self.kal3 = in8;

		self.sH = xH*vev**2/self.F**2;
		self.cH = (1-self.sH**2)**0.5;
		self.v = self.F/2**0.5*math.acos(1-(vev/self.F)**2);
		self.lam2 = 244.518*(1+self.R**2)**0.5/(self.F*self.R*math.acos(1-60516/self.F**2));
		self.xL = self.R**2/(1+self.R**2);
		self.d2 = -5./6 + 1./2*self.xL**2 + 2*self.xL*(1-self.xL);
		self.lamphi2 = 2*(MH/self.v)**2;
		self.lamhphiphih = -4./3*self.lamphi2;
		self.lamphi2phi2 = -16*(self.R*self.lam2)**2;
		self.lamphi4 = -8./3*(gw**2 + g1**2) + 16./3*(self.R*self.lam2)**2;

		self.MAH = self.F*g1/math.sqrt(5.)*(1-5*vev**2/(8*self.F**2));
		self.MWH = self.F*gw*(1-vev**2/(8*self.F**2));
		self.MZH = self.MWH;
		self.MHve = 2**0.5*self.kal1*self.F;
		self.MHvm = 2**0.5*self.kal2*self.F;
		self.MHvt = 2**0.5*self.kal3*self.F;
		self.MHe = 2**0.5*self.kal1*self.F;
		self.MHmu = 2**0.5*self.kal2*self.F;
		self.MHta = 2**0.5*self.kal3*self.F;
		self.MHu = 2**0.5*self.kaq1*self.F*(1-1/8*vev**2/self.F**2);
		self.MHc = 2**0.5*self.kaq2*self.F*(1-1/8*vev**2/self.F**2);
		self.MHt = 2**0.5*self.kaq3*self.F*(1-1/8*vev**2/self.F**2);
		self.MHd = 2**0.5*self.kaq1*self.F;
		self.MHs = 2**0.5*self.kaq2*self.F;
		self.MHb = 2**0.5*self.kaq3*self.F;
		self.MHTodd = MT/vev*self.F*(1+self.R**2)**0.5/self.R;
		self.MHTeven = self.MHTodd*(1+self.R**2)**0.5;
		self.MPhi0 = 2**0.5*MH*self.F/vev;
		self.MPhiP = 2**0.5*MH*self.F/vev;
		self.MPhiC = 2**0.5*MH*self.F/vev;
		self.MPhiCC = 2**0.5*MH*self.F/vev;


	def writespec(self, filename):
		f=open(filename,'w');

		cont=self.getcont()
		cont=cont.replace("rp1",       str(self.F))
		cont=cont.replace("rp2",       str(self.R))
		cont=cont.replace("rp3",       str(self.kaq1))
		cont=cont.replace("rp4",       str(self.kaq2))
		cont=cont.replace("rp5",       str(self.kaq3))
		cont=cont.replace("rp6",       str(self.kal1))
		cont=cont.replace("rp7",       str(self.kal2))
		cont=cont.replace("rp8",       str(self.kal3))
		cont=cont.replace("rpMHd_",    str(self.MHd))
		cont=cont.replace("rpMHu_",    str(self.MHu))
		cont=cont.replace("rpMHs_",    str(self.MHs))
		cont=cont.replace("rpMHc_",    str(self.MHc))
		cont=cont.replace("rpMHb_",    str(self.MHb))
		cont=cont.replace("rpMHt_",    str(self.MHt))
		cont=cont.replace("rpMHTodd_", str(self.MHTodd))
		cont=cont.replace("rpMHTeven_",str(self.MHTeven))
		cont=cont.replace("rpMHe_",    str(self.MHe))
		cont=cont.replace("rpMHve_",   str(self.MHve))
		cont=cont.replace("rpMHmu_",   str(self.MHmu))
		cont=cont.replace("rpMHvm_",   str(self.MHvm))
		cont=cont.replace("rpMHta_",   str(self.MHta))
		cont=cont.replace("rpMHvt_",   str(self.MHvt))
		cont=cont.replace("rpMAH_",    str(self.MAH))
		cont=cont.replace("rpMZH_",    str(self.MZH))
		cont=cont.replace("rpMWH_",    str(self.MWH))
		cont=cont.replace("rpMPhi0_",  str(self.MPhi0))
		cont=cont.replace("rpMPhiP_",  str(self.MPhiP))
		cont=cont.replace("rpMPhiC_",  str(self.MPhiC))
		cont=cont.replace("rpMPhiCC_", str(self.MPhiCC))

		f.write(cont);
		f.close();

	def LHTspector(in1, in2, in3, in4):
		pass

	def getcont(self):

		cont='''
######################################################################
## PARAM_CARD AUTOMATICALY GENERATED BY MG5 FOLLOWING UFO MODEL   ####
######################################################################
##                                                                  ##
##  Width set on Auto will be computed following the information    ##
##        present in the decay.py files of the model.               ##
##        See  arXiv:1402.1178 for more details.                    ##
##                                                                  ##
######################################################################

###################################
## INFORMATION FOR CKMBLOCK
###################################
Block ckmblock 
    1 2.277360e-01 # cabi 

###################################
## INFORMATION FOR LHTBLOCK
###################################
Block lhtblock 
    1 rp1 # F 
    2 rp2 # R 
    3 rp3 # kaq1 
    4 rp4 # kaq2
    5 rp5 # kaq3 
    6 rp6 # kal1 
    7 rp7 # kal2 
    8 rp8 # kal3 

###################################
## INFORMATION FOR MASS
###################################
Block mass 
    1 5.040000e-03 # MD 
    2 2.550000e-03 # MU 
    3 1.010000e-01 # MS 
    4 1.270000e+00 # MC 
    5 4.700000e+00 # MB 
    6 1.720000e+02 # MT 
   11 5.110000e-04 # Me 
   13 1.056600e-01 # MM 
   15 1.777000e+00 # MTA 
   23 9.118760e+01 # MZ 
   24 8.038500e+01 # MW 
   25 1.250000e+02 # MH 
  8880001 rpMHd_     # MHd 
  8880002 rpMHu_     # MHu 
  8880003 rpMHs_     # MHs 
  8880004 rpMHc_     # MHc 
  8880005 rpMHb_     # MHb 
  8880006 rpMHt_     # MHt 
  8880007 rpMHTodd_  # MHTodd 
  8880008 rpMHTeven_ # MHTeven 
  8880011 rpMHe_     # MHe 
  8880012 rpMHve_    # MHve 
  8880013 rpMHmu_    # MHmu 
  8880014 rpMHvm_    # MHvm 
  8880015 rpMHta_    # MHta 
  8880016 rpMHvt_    # MHvt 
  8880022 rpMAH_     # MAH 
  8880023 rpMZH_     # MZH 
  8880024 rpMWH_     # MWH 
  8880025 rpMPhi0_   # MPhi0 
  8880026 rpMPhiP_   # MPhiP 
  8880027 rpMPhiC_   # MPhiC 
  8880028 rpMPhiCC_  # MPhiCC 
## Dependent parameters, given by model restrictions.
## Those values should be edited following the 
## analytical expression. MG5 ignores those values 
## but they are important for interfacing the output of MG5
## to external program such as Pythia.
  12 0.000000e+00 # ve : 0.0 
  14 0.000000e+00 # vm : 0.0 
  16 0.000000e+00 # vt : 0.0 
  21 0.000000e+00 # g : 0.0 
  22 0.000000e+00 # a : 0.0 

###################################
## INFORMATION FOR SMINPUTS
###################################
Block sminputs 
    1 1.279000e+02 # aEWM1 
    2 1.166370e-05 # Gf 
    3 1.184000e-01 # aS (Note that Parameter not used if you use a PDF set) 

###################################
## INFORMATION FOR YUKAWA
###################################
Block yukawa 
    1 5.040000e-03 # ymdo 
    2 2.550000e-03 # ymup 
    3 1.010000e-01 # yms 
    4 1.270000e+00 # ymc 
    5 4.700000e+00 # ymb 
    6 1.720000e+02 # ymt 
   11 5.110000e-04 # yme 
   13 1.056600e-01 # ymm 
   15 1.777000e+00 # ymtau 

###################################
## INFORMATION FOR DECAY
###################################
#DECAY   6 1.508336e+00 # WT 
#DECAY  23 2.495200e+00 # WZ 
#DECAY  24 2.085000e+00 # WW 
#DECAY  25 5.753088e-03 # WH 
#DECAY 8880001 5.000000e+00 # WHd 
DECAY   6 auto # WT 
DECAY  23 auto # WZ 
DECAY  24 auto # WW 
DECAY  25 auto # WH 
DECAY 8880001 auto # WHd 
DECAY 8880002 auto # WHu 
DECAY 8880003 auto # WHs 
DECAY 8880004 auto # WHc 
DECAY 8880005 auto # WHb 
DECAY 8880006 auto # WHt 
DECAY 8880007 auto # WHTodd 
DECAY 8880008 auto # WHTeven 
DECAY 8880011 auto # WHe 
DECAY 8880012 auto # WHve 
DECAY 8880013 auto # WHmu 
DECAY 8880014 auto # WHvm 
DECAY 8880015 auto # WHta 
DECAY 8880016 auto # WHvt 
DECAY 8880023 auto # WZH 
DECAY 8880024 auto # WWH 
DECAY 8880025 auto # WPhi0 
DECAY 8880026 auto # WPhiP 
DECAY 8880027 auto # WPhiC 
DECAY 8880028 auto # WPhiCC 
## Dependent parameters, given by model restrictions.
## Those values should be edited following the 
## analytical expression. MG5 ignores those values 
## but they are important for interfacing the output of MG5
## to external program such as Pythia.
DECAY  1 0.000000e+00 # d : 0.0 
DECAY  2 0.000000e+00 # u : 0.0 
DECAY  3 0.000000e+00 # s : 0.0 
DECAY  4 0.000000e+00 # c : 0.0 
DECAY  5 0.000000e+00 # b : 0.0 
DECAY  11 0.000000e+00 # e- : 0.0 
DECAY  12 0.000000e+00 # ve : 0.0 
DECAY  13 0.000000e+00 # mu- : 0.0 
DECAY  14 0.000000e+00 # vm : 0.0 
DECAY  15 0.000000e+00 # ta- : 0.0 
DECAY  16 0.000000e+00 # vt : 0.0 
DECAY  21 0.000000e+00 # g : 0.0 
DECAY  22 0.000000e+00 # a : 0.0 
#DECAY  8880022 0.000000e+00 # ah : 0.0 
DECAY  8880022 auto # ah : 0.0 
#===========================================================
# QUANTUM NUMBERS OF NEW STATE(S) (NON SM PDG CODE)
#===========================================================

Block QNUMBERS 8880022  # ah 
        1 0  # 3 times electric charge
        2 3  # number of spin states (2S+1)
        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 0  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 8880023  # zh 
        1 0  # 3 times electric charge
        2 3  # number of spin states (2S+1)
        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 0  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 8880024  # wh+ 
        1 3  # 3 times electric charge
        2 3  # number of spin states (2S+1)
        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 1  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 8880012  # veh 
        1 0  # 3 times electric charge
        2 2  # number of spin states (2S+1)
        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 1  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 8880014  # vmh 
        1 0  # 3 times electric charge
        2 2  # number of spin states (2S+1)
        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 1  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 8880016  # vth 
        1 0  # 3 times electric charge
        2 2  # number of spin states (2S+1)
        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 1  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 8880011  # eh- 
        1 -3  # 3 times electric charge
        2 2  # number of spin states (2S+1)
        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 1  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 8880013  # muh- 
        1 -3  # 3 times electric charge
        2 2  # number of spin states (2S+1)
        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 1  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 8880015  # tah- 
        1 -3  # 3 times electric charge
        2 2  # number of spin states (2S+1)
        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 1  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 8880002  # uh 
        1 2  # 3 times electric charge
        2 2  # number of spin states (2S+1)
        3 3  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 1  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 8880004  # ch 
        1 2  # 3 times electric charge
        2 2  # number of spin states (2S+1)
        3 3  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 1  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 8880006  # th 
        1 2  # 3 times electric charge
        2 2  # number of spin states (2S+1)
        3 3  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 1  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 8880001  # dh 
        1 -1  # 3 times electric charge
        2 2  # number of spin states (2S+1)
        3 3  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 1  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 8880003  # sh 
        1 -1  # 3 times electric charge
        2 2  # number of spin states (2S+1)
        3 3  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 1  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 8880005  # bh 
        1 -1  # 3 times electric charge
        2 2  # number of spin states (2S+1)
        3 3  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 1  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 8880007  # thodd 
        1 2  # 3 times electric charge
        2 2  # number of spin states (2S+1)
        3 3  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 1  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 8880008  # theven 
        1 2  # 3 times electric charge
        2 2  # number of spin states (2S+1)
        3 3  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 1  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 8880025  # phi0 
        1 0  # 3 times electric charge
        2 1  # number of spin states (2S+1)
        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 0  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 8880026  # phip 
        1 0  # 3 times electric charge
        2 1  # number of spin states (2S+1)
        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 0  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 8880027  # phi+ 
        1 3  # 3 times electric charge
        2 1  # number of spin states (2S+1)
        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 1  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 8880028  # phi++ 
        1 6  # 3 times electric charge
        2 1  # number of spin states (2S+1)
        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 1  # Particle/Antiparticle distinction (0=own anti)
'''
		return cont
