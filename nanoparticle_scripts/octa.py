from ase.cluster.octahedron import Octahedron
from ase.io import write

size = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] #size

for n in size: # loop through size list
    atoms = Octahedron('Au', # element
                       length=n, # length of face
                       cutoff=0, # cutoff, 0 = no truncation of octahedral symmetry
                       latticeconstant=4.16, # lattice constant
                       alloy=False # no alloying
                       )

    length = len(atoms) # record total number of atoms

    #print(length)

    write(f'Au{length}_octa.dat', atoms, format="lammps-data") # write to file
