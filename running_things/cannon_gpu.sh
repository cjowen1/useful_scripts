#!/bin/bash
#SBATCH --partition=gpu,seas_gpu,kozinsky_gpu 
#SBATCH --time='7-00:00:00'
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --gres=gpu:4
#SBATCH --mem-per-cpu=3000
#SBATCH --constraint=a100
#SBATCH --no-requeue
#SBATCH --mail-type=ALL
#SBATCH --mail-user=email@g.harvard.edu

module load gcc/10.2.0-fasrc01 openmpi/4.1.0-fasrc01 hdf5/1.10.7-fasrc02 intel-mkl/2019.5.281-fasrc01 cuda/11.4.2-fasrc01 cudnn/8.1.0.77_cuda11.2-fasrc01
module list

date
nvidia-smi

srun /n/holystore01/LABS/kozinsky_lab/Lab/Software/LAMMPS/rmasslammps/a100build/lmp -sf kk -k on g 4 -pk kokkos newton on neigh full -v i 1 -in 1.in
echo
echo "My hostname is: $(hostname -s)"
echo
wait
