#!/bin/bash
#SBATCH -A m4297
#SBATCH -C gpu
#SBATCH --job-name=project
#SBATCH -N 80 # number of GPU nodes (each with 4 A100s)
#SBATCH -t 4:00:00 # wall-time, always run with more nodes on shorter times due to Perlmutter queue policies
#SBATCH -q regular # QOS
#SBATCH --ntasks-per-node=4 # call for all 4 GPUs on each node
#SBATCH --cpus-per-task=1
#SBATCH --gpus-per-task=1
#SBATCH --gpu-bind=none
#SBATCH --mail-type=begin,end,fail
#SBATCH --mail-user=email@g.harvard.edu,email@g.harvard.edu

module list

date
nvidia-smi
hostname
lscpu

export FLUX=1

MPICH_GPU_SUPPORT_ENABLED=1

P=60
srun /global/cfs/cdirs/m4297/rmasslammps/build/lmp -sf kk -k on g 4 -pk kokkos newton on neigh full gpu/aware off -v P $((P*10000)) -in in_${i}.lammps # run set of lammps inputs on GPUs using FLARE exec
