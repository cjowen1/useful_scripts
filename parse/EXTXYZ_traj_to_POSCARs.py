import numpy as np
from ase.io import read, write
import os, glob, shutil, sys, time

n_frames = 0
tic = time.time()
dft_file = sys.argv[1]
trj = read(dft_file, index=":")
lmp_trj = []
for i, frame in enumerate(trj):
    write(f"frame_{i}.xyz",frame,format='vasp')
