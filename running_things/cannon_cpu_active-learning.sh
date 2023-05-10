#!/bin/sh
#SBATCH -n 96
#SBATCH -t 7-00:00
#SBATCH -e error.err
#SBATCH -p seas_compute,imasc
#SBATCH -o out.out
#SBATCH --mem-per-cpu=0
#SBATCH --mail-type=ALL
#SBATCH --mail-user=email@g.harvard.edu
#SBATCH --no-requeue

module load Anaconda3/5.0.1-fasrc01
source activate pyfpp10

module load cmake/3.17.3-fasrc01
module load gcc/9.3.0-fasrc01
module load intel-mkl/2017.2.174-fasrc01
module load openmpi/4.0.5-fasrc01

export ASE_VASP_COMMAND="srun -n 96 --mpi=pmi2 ${HOME}/vaspbin/vasp-vtst.std"
export VASP_PP_PATH=${HOME}/Potentials_5.4.1
export OMP_NUM_THREADS=48

flare-otf example.yaml
