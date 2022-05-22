import ase
from ase.io import read, write
from ase.build import fcc100, fcc111, fcc110
import random
import os
import sys
import re

element = 'Au'   # element name

slab = fcc111(element, size=(3,3,6), a=4.16, vacuum=10, periodic=True) # choose miller indices, element, periodic replications (size), PBE lattice constant, vacuum, and periodicity
#print(slab.get_positions()) # print positions in terminal for sanity

write('Au111_slab_3x3x6.xyz', slab)#, format="lammps-data") # write slab using ase write to whatever file type
