#!/usr/bin/python

import sys
import numpy as np 

from ase.io.vasp import read_vasp_out

narg = len(sys.argv)

if( narg < 2 ):
	print "You have passed " + str(narg-1) + " arguments to the script"
	print "This script needs 2 parameters"
	print "Scrips exits"
	exit()

arg1 = sys.argv[1]

if( arg1 == "conv"):
    print "Brawo.\n";
elif(True):
    print "Only single-digit numbers are allowed\n";




#ini = int(  sys.argv[1])
#fin = int(  sys.argv[2])


#outcar = read_vasp_out('OUTCAR', slice(1,None,1))
#n = len(outcar)

#forces = outcar[n-1].get_forces()

#tip_force = [0.0,0.0,0.0]

#for i in range(ini-1,fin):
#    tip_force += forces[i]
##    print i, tip_force
#print tip_force[0],tip_force[1],tip_force[2],
