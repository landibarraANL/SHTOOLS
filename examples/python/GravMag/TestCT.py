#!/usr/bin/env python
"""
This script tests the gravity and magnetics routines. 
"""

#standard imports:
import os, sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#import shtools:
sys.path.append(os.path.join(os.path.dirname(__file__), "../../.."))
import pyshtools as shtools

#set shtools plot style:
sys.path.append(os.path.join(os.path.dirname(__file__), "../Common"))
from FigStyle import style_shtools
mpl.rcParams.update(style_shtools)

#==== MAIN FUNCTION ====
def main():
	TestCrustalThickness()

#==== TEST FUNCTIONS ====
def TestCrustalThickness():
	"""
	Example routine to calculate the crustal thickness of Mars
	"""
	delta_max = 5.0
	nmax = 6
	degmax = 50
	lmax = 200
	rho_c = 2900.0
	rho_m = 3500.0
	d = 3344282.7091028118
	filter_type = 0
	half = 0

	gravfile = '../../ExampleDataFiles/jgmro_110b_sha.tab'	
	header = np.zeros(2,dtype=float)
	pot, lmaxp, header = shtools.SHReadH(gravfile,110,header)
	gm = header[1] * 1.e9
	mass = gm / shtools.constant.grav_constant
	r_grav = header[0] * 1.e3
	
	topofile = '../../ExampleDataFiles/MarsTopo719.shape'
	hlm,lmaxt = shtools.SHRead(topofile,719)
	r0 = hlm[0,0,0]
	print "Mean planetary radius = ", r0/1.e3
	
	for l in range(2,lmaxp+1):
		pot[0:2,l,0:l+1] = pot[0:2,l,0:l+1] * (r_grav/r0)**l

	topo_grid = shtools.MakeGridDH(hlm,lmax=lmax,sampling=2,lmax_calc=degmax)
	print topo_grid.shape[0], topo_grid.shape[1]
	bc, d = shtools.CilmPlusDH(topo_grid,nmax,mass,rho_c,sampling=2)
	print d
	ba = pot - bc	# need to pad arrays with zeros
	
	moho_c = np.zeros(2,degmax+1,degmax+1)
	moho_c[0,0,0] = d
	
	for l in range(1,degmax+1):
		if filter_type == 0:
			moho_c[:,l,:l+1]= ba[:,l,:l+1] * mass * (2*l+1) * ((r0/d)**l) \
			/(4.0*shtools.constant.pi*(rho_m-rho_c)*d**2)
		elif filter_type == 1:
			moho_c[:,l,:l+1] = wl(l, half, r0, d) * ba[:,l,:l+1] * mass * (2*l+1) * ((r0/d)**l) \
			/(4.0*shtools.constant.pi*(rho_ma-rho_c)*d**2)
		else:
			moho_c[:,l,:l+1] = wlcurv(l, half, r0, d) * ba[:,l,:l+1] * mass * (2*l+1) * ((r0/d)**l) \
			/(4.0*shtools.constant.pi*(rho_m-rho_c)*d**2)
			
	moho_grid3 = shtools.MakeGridDH(moho_c,lmax=lmax,sampling=2,lmax_calc=degmax)

	print "Maximum Crustal thickness (km) = ", (topo_grid-moho_gird3).max()/1.e3
	print "Minimum Crustal thickness (km) = ", (topo_grid-moho_gird3).min()/1.e3

	moho_c = HilmDH(ba,moho_grid3,lmax,nmax,mass,r0,(rho_m-rho_c),sampling=2,filter_type=filter_type,filter_deg=half,lmax_calc=degmax)

	moho_grid2 = shtools.MakeGridDH(moho_c,lmax=lmax,sampling=2,lmax_calc=degmax)

	print "Delta (km) = ", abs(moho_grid3-moho_grid2).max()/1.e3
		
	temp_grid = topo_grid-moho_grid2
	print "Maximum Crustal thickness (km) = ",temp_grid.max()/1.e3
	print "Minimum Crustal thickness (km) = ", temp_grid.min()/1.e3
	
	iter = 0
	delta = 1.0e9
	
	
#==== EXECUTE SCRIPT ====
if __name__ == "__main__":
    main()

