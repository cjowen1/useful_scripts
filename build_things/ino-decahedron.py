from ase.cluster.decahedron import Decahedron
from ase.io import write

size = [3,4,5,6]

for n in size:
    atoms = Decahedron('Au',
                       p=n,  # natoms on 100 face normal to 5-fold axis
                       q=n,  # natoms 0n 100 parallel to 5-fold axis
                       r=0,  # depth of the Marks re-entrance?
                       latticeconstant=4.16,
                       )

    length = len(atoms) # check length

    print(length)

    atoms.center(vacuum=10, axis=(0, 1, 2), about=None)

    write(f'Au{length}_deca.dat', atoms, format="lammps-data") # write NP to file
