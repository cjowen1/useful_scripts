from ase.io import read, write
from ase import Atoms
import numpy as np
import os
import sys
from ase.io.extxyz import write_extxyz

# Read the input file
atoms_list = read('v4_all.xyz', index=":")

new_atoms_list = []

# Iterate over each Atoms object in atoms_list
for atoms in atoms_list:
    # Create a new Atoms object with the same atomic structure
    new_atoms = Atoms(atoms.get_chemical_symbols(), positions=atoms.get_positions())

    # Copy energy and stress from the original Atoms object to the new Atoms object
    if 'Lattice' in atoms.info:
        new_atoms.info['Lattice'] = atoms.info['Lattice']
    if 'energy' in atoms.info:
        new_atoms.info['energy'] = atoms.info['energy']
    if 'stress' in atoms.info:
        new_atoms.info['stress'] = atoms.info['stress']
    if 'target_atoms' in atoms.info:
        new_atoms.info['target_atoms'] = atoms.info['target_atoms']
    if 'pbc' in atoms.info: # may return "F F F" regardless, so check results
        new_atoms.info['pbc'] = atoms.info['pbc']

    # Iterate through the available arrays and copy them to the new Atoms object, except for 'magmoms'
    for key, value in atoms.arrays.items():
        if key != 'magmoms':
            if key not in new_atoms.arrays:  # Check if the array is not already present
                new_atoms.new_array(key, value)

    new_atoms_list.append(new_atoms)

# Write the new Atoms objects to extxyz files
for i, new_atoms in enumerate(new_atoms_list):
    with open(f'frame_{i}.xyz', 'w') as f:
        write(f, new_atoms, format="extxyz")

print(f'# v4 frames = ', len(new_atoms_list))
