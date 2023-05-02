import matplotlib.pyplot as plt
import numpy as np
from ase.io import read

# Read the input file
atoms_list = read('v4_all_mod.xyz', index=":")

# Extract stress values from each Atoms object
stress_values = []

for atoms in atoms_list:
    if 'stress' in atoms.info:
        stress_values.append(np.abs(atoms.info['stress']).flatten())

# Convert the list of stress values to a NumPy array
stress_values = np.concatenate(stress_values)

# Plot a histogram of stress values
plt.hist(stress_values, bins=50, density=True, alpha=0.75)

plt.xlabel('Stress')
plt.ylabel('Frequency')
plt.title('Distribution of absolute stress values')

plt.grid(True)
plt.savefig("stress.png",dpi=300)
