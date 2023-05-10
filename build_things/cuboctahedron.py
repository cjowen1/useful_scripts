from ase.cluster import Octahedron
from ase.io import write

cutoff = [2,3,4,5]

for i in cutoff:
    atoms = Octahedron('Au', length=2*i+1, cutoff=i, latticeconstant=4.16, alloy=False)

    total = len(atoms) # check length of atoms to make sure cutoff is correct
    print(total)

    atoms.center(vacuum=10, axis=(0, 1, 2), about=None) # center NPs in vacuum

    write(f'Au{total}_cuboct.dat',atoms,format="lammps-data") # write to file for MD
