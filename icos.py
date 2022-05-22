from ase.cluster.icosahedron import Icosahedron
from ase.io import write
from ase.build import fcc111, add_adsorbate

shells = [2,3,4,5,6,7,8,9,10,11,12,13,14,15] # determine number and size of clusters to make

for i in shells:    # loop through shells list
    atoms = Icosahedron('Pt', noshells=i, latticeconstant=3.97) # use Icosahedron package from ASE to make clusters
    total = len(atoms) # remember total number of atoms for each cluster
    #print(total)                          

    atoms.center(vacuum=8, axis=(0, 1, 2), about=None) # add vacuum to cluster and center in periodic cell

    write(f'Pt{total}.xyz',atoms)#,format="lammps-data") # write to file and include number of atoms in name
