from ase.io import write
from ase.build import bulk
from ase.build import make_supercell
import numpy as np

lats = np.arange(4.06,4.27,0.01) # sweep over bulk lattice cells for use in validation

for i in lats:
    b1 = bulk('Au', 'fcc', a=i, cubic=True)
    b1_sup = b1 * [1,1,1]
    write(f'Au_fcc_1x1x1_{i}.dat',b1_sup,format="vasp")
