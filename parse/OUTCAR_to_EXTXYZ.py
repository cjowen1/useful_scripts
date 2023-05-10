import numpy as np
from ase.io.vasp import read_vasp_out
import os
from ase.io import write
import shutil

if not os.path.exists('recalc'): # create directory to collect new frames
    os.mkdir("recalc")
        
i = 0   
for n in range(1,318,1):
    os.chdir(f"frame_{n}") # loops over directories labeled frame_{n} where independent vasp calculations were completed
    
    traj = read_vasp_out("OUTCAR", index=slice(None)) # read VASP output, index = -1 might be necessary

    answ = os.path.exists("frame_{n}.xyz") # try to write new file
    if(answ):
        pass
    else:
        write(f"frame_{n}.xyz",traj,format='extxyz')

    ansf = os.path.exists("../recalc/frame_{n}.xyz") # move new file to collection-directory
    if(ansf):
        pass
    else:
        shutil.move(f"frame_{n}.xyz", "../recalc/")

    os.chdir("../")
    print('successfully parsed frame', i)  # job status
    i += 1
