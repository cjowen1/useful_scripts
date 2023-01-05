from ase.io import write
from ase.build import bulk
from ase.build import make_supercell
from clusterx.parent_lattice import ParentLattice

a1 = bulk('Cu', 'fcc', a=3.62, cubic=True) # use ase bulk to build bulk cell
a1_sup = a1 * [3,3,3] # replicate 1x1x1 cell to form supercell

write('Pt_bulk30.xyz',a1_sup)#,format="lammps-data") # write to file
