import numpy as np
from ase.io.vasp import read_vasp_out
import os
from ase.io import write
import shutil

if not os.path.exists('recalc'):
    os.mkdir("recalc")

    # Parse with ASE.
        #write xyz file for each OUTCAR to concatenate later for offline training

for n in range(1,318,1):
    os.chdir(f"frame_{n}")
    
    traj = read_vasp_out("OUTCAR", index=slice(None))

    answ = os.path.exists("frame_{n}.xyz")
    if(answ):
        pass
    else:
        write(f"frame_{n}.xyz",traj,format='extxyz')

    ansf = os.path.exists("../recalc/frame_{n}.xyz")
    if(ansf):
        pass
    else:
        shutil.move(f"frame_{n}.xyz", "../recalc/")

    os.chdir("../")
