import numpy as np
from ase.io import read, write
import os, glob, shutil, sys, time

trj_file = sys.argv[1] # read in trajectory file using system argument
trj = read(trj_file, index=":") # parse individual frames into trj 

for i, frame in enumerate(trj): # loop over frames and print POSCARs for use in VASP
    write(f"POSCAR_{i}",frame,format='vasp')
