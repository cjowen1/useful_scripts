import ase
from ase.io import read, write
from ase.build import fcc100, fcc111, fcc110
import random
import os
import sys
import re

element = 'Cu'   # element name

slab = fcc100(element, size=(3,3,6), a=3.62, vacuum=10, periodic=True) # choose miller indices, element, periodic replications (size), lattice constant, vacuum, and periodicity
#print(slab.get_positions()) # print positions in terminal for sanity

write('Cu100_slab_3x3x6.xyz', slab)#, format="lammps-data") # write slab using ase write to whatever file type
