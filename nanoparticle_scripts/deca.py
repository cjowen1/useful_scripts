from ase.cluster.decahedron import Decahedron
from ase.io import write

size = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] # number and size of clusters

for n in size: # loop through size list
    atoms = Decahedron('Pt', # element
                       p=n,  # natoms on 100 face normal to 5-fold axis
                       q=n,  # natoms 0n 100 parallel to 5-fold axis
                       r=0,  # depth of the Marks re-entrance?
                       latticeconstant=3.96, # lattice constant for Pt
                       )

    length = len(atoms) # record number of atoms for each cluster

    #print(length)

    write(f'Pt{length}_deca_PBE.dat', atoms, format="lammps-data") # write to file
