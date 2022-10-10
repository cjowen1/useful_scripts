import numpy as np
from ase.io.vasp import read_vasp_out
import os
from ase.io import read, write
import shutil
from ase.io.lammpsdata import read_lammps_data

i = 0
h = 21.58        

for n in range(1,101,1):
    os.mkdir(f"{n}")
    
    os.chdir(f"{n}")
    
    traj = read(f"../h_pt_111_top.dat",format="lammps-data",style="atomic")

    traj.pop(-1)   
    traj.pop(-1)    

    relative = (-0.38, 0.0, h)

    relative1 = (0.38, 0.0, h)

    traj.append('He')
    traj.positions[-1] = relative
     
    traj.append('He')
    traj.positions[-1] = relative1

    write(f"h_pt_111_top.dat",traj,format='lammps-data')

    os.chdir("../")
    print('successfully parsed frame', i) 
    i += 1
    h += 0.04
