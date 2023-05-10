import ase
from ase.io import write
from ase.build import fcc100, fcc111, fcc110

element = 'Au'   # element name

# Build Au(111) surface slab that is DFT sized
slab = fcc111(element, size=(3,3,6), a=4.16, vacuum=10, periodic=True) # choose miller indices, element, periodic replications (size), PBE lattice constant, vacuum, and periodicity
#print(slab.get_positions()) # print positions in terminal for sanity
write('Au111_slab_3x3x6.xyz', slab, format='extxyz') # write slab using ase write to whatever file type

# Build Au(110) surface slab that is DFT sized
slab = fcc110(element, size=(3,2,10), a=4.16, vacuum=10, periodic=True)
write('Au110_slab_3x2x10.xyz', slab, format='extxyz')

# Build Au(100) surface slab that is DFT sized
slab = fcc100(element, size=(3,3,6), a=4.16, vacuum=10, periodic=True)
write('Au100_slab_3x3x6.xyz', slab, format='extxyz')
