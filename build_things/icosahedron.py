from ase.cluster.icosahedron import Icosahedron
from ase.io import write

shells = [12] # include number of shells in NP

for i in shells:
    atoms = Icosahedron('Au', noshells=i, latticeconstant=4.16)
    total = len(atoms) # check length to determine if shells are appropriate
    print(total)                          

    atoms.center(vacuum=50, axis=(0, 1, 2), about=None) # center NP in vacuum
    
    write(f'Au{total}_icos.dat',atoms,format="lammps-data") # write NP to file in lammps-data format for MD
