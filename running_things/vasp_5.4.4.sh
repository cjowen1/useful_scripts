#!/bin/bash
#SBATCH--job-name=Cu_GSFE
#SBATCH-n 48 # Number of cores requested
#SBATCH-t 1-00:00 # Runtime in days-hours:minutes
#SBATCH-p imasc,seas_compute # Partition to submit to
#SBATCH--mem-per-cpu=0 # Memory per cpu in MB (see also--mem)
#SBATCH-o job.out # Standard out goes to this file
#SBATCH-e job.err # Standard err goes to this file

module load intel/17.0.4-fasrc01 impi/2017.2.174-fasrc01

srun -n 48 --mpi=pmi2 /n/holystore01/LABS/kozinsky_lab/Lab/Software/VASP-VTST/VASP5.4/vasp.5.4.4/bin/vasp_std_skylake;
