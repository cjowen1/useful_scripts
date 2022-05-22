from ase.cluster import Octahedron
from ase.io import write

cutoff = [22] # define cluster number and sizes

for i in cutoff: # loop through cutoff list
    atoms = Octahedron('Pt', length=2*i+1, cutoff=i, latticeconstant=3.97, alloy=False) # use ASE octahedron package to make cluster, can set alloy to true but need list of elements to make l1,2 structure

    total = len(atoms) # record number of atoms

    #print(total)

    atoms.center(vacuum=8, axis=(0, 1, 2), about=None) # center cluster in cell and introduced vacuum

    write(f'Pt{total}.xyz',atoms)#,format="lammps-data") # write to file
