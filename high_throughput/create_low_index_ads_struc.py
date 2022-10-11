import os
import re
import sys
import ase
import shutil
import random
import numpy as np
from ase.io import read, write
from ase.io.vasp import read_vasp_out
from ase.build import fcc100, fcc111, fcc110
from ase.io.lammpsdata import read_lammps_data

# lammps input file and flare coeff file should be in 
# Create master geometry files 
element = "Pt"

# enumerate binding sites and coordinates from file
top_111 = np.array([0.0,0.0,0.0])
bri_111 = np.array([1.403606961, 0.0, 0.0])
fcc_111 = np.array([1.4036069606552968, 0.8103728565707679, 0.0])
hcp_111 = np.array([2.8072139213105936, 1.6207457131415359, 0.0])

top_100 = np.array([0.0,0.0,0.0])
bri_100 = np.array([1.403606961, 0.0, 0.0])
hol_100 = np.array([1.403606961, 1.403606961, 0.0])

top_110 = np.array([0.0,0.0,0.0])
bri_110 = np.array([0.0, 1.403606961, 0.0])
lbri_110 = np.array([1.985, 0.0, 0.0])
hol_110 = np.array([1.9849999999999999, 1.403606961, 0.0])

os.mkdir('111_CO')
os.chdir('111_CO')
shutil.copyfile('../1.in','./1.in')
shutil.copyfile('../lmp_0.0075.flare','./lmp_0.0075.flare')

# CO/Pt(111) Benchmarks

perp_ads_111 = ["111_top_perp", "111_bri_perp", "111_fcc_perp", "111_hcp_perp"]
perp_ads_i_111 = ["111_top_perp_i", "111_bri_perp_i", "111_fcc_perp_i", "111_hcp_perp_i"]
para_ads_111 = ["111_top_para", "111_top_para1", "111_bri_para", "111_bri_para1", "111_fcc_para", "111_fcc_para1", "111_hcp_para", "111_hcp_para1"]

for n in perp_ads_111:
    os.mkdir(f"{n}")
    os.chdir(f"{n}")
    shutil.copyfile('../1.in',f'./1.in')
    shutil.copyfile('../lmp_0.0075.flare',f'./lmp_0.0075.flare')

    h_C = 20.82
    h_O = 21.96

    i = 0
    j = 0

    for m in range(1,51,1):
        os.mkdir(f"{m}")

        shutil.copyfile('../1.in',f'{m}/1.in')
        shutil.copyfile('../lmp_0.0075.flare',f'{m}/lmp_0.0075.flare')
        
        slab_111 = fcc111(element, size=(3,3,6), a=4.03, vacuum=10, periodic=True)
        write('Pt111_top.dat', slab_111, format="lammps-data")

        traj = read("Pt111_top.dat",format="lammps-data",style="atomic")

        if n == '111_top_perp':
            relative = top_111 + np.array([0.0, 0.0, h_C])
            relative1 = top_111 + np.array([0.0, 0.0, h_O])

        elif n == "111_bri_perp":
            relative = bri_111 + np.array([0.0, 0.0, h_C])
            relative1 = bri_111 + np.array([0.0, 0.0, h_O])

        elif n == "111_fcc_perp": 
            relative = fcc_111 + np.array([0.0, 0.0, h_C])
            relative1 = fcc_111 + np.array([0.0, 0.0, h_O])

        elif n == "111_hcp_perp":
            relative = hcp_111 + np.array([0.0, 0.0, h_C])
            relative1 = hcp_111 + np.array([0.0, 0.0, h_O])
        
        traj.append('He')
        traj.positions[-1] = relative

        traj.append('Li')
        traj.positions[-1] = relative1

        write("CO_Pt111_top.dat",traj,format='lammps-data')
        shutil.move("CO_Pt111_top.dat",f"{m}/CO_Pt111_top.dat")        

        print('successfully parsed frame', i)
        i += 1
        h_C += 0.1
        h_O += 0.1

    os.chdir('../')
    
for n in perp_ads_i_111:
    os.mkdir(f"{n}")
    os.chdir(f"{n}")
    shutil.copyfile('../1.in',f'./1.in')
    shutil.copyfile('../lmp_0.0075.flare',f'./lmp_0.0075.flare')

    h_C = 21.96
    h_O = 20.82

    i = 0
    j = 0

    for m in range(1,51,1):
        os.mkdir(f"{m}")

        shutil.copyfile('../1.in',f'{m}/1.in')
        shutil.copyfile('../lmp_0.0075.flare',f'{m}/lmp_0.0075.flare')

        slab_111 = fcc111(element, size=(3,3,6), a=4.03, vacuum=10, periodic=True)
        write('Pt111_top.dat', slab_111, format="lammps-data")

        traj = read("Pt111_top.dat",format="lammps-data",style="atomic")

        if n == '111_top_perp_i':
            relative = top_111 + np.array([0.0, 0.0, h_C])
            relative1 = top_111 + np.array([0.0, 0.0, h_O]) 

        elif n == "111_bri_perp_i":
            relative = bri_111 + np.array([0.0, 0.0, h_C])
            relative1 = bri_111 + np.array([0.0, 0.0, h_O])

        elif n == "111_fcc_perp_i":
            relative = fcc_111 + np.array([0.0, 0.0, h_C])
            relative1 = fcc_111 + np.array([0.0, 0.0, h_O])

        elif n == "111_hcp_perp_i":
            relative = hcp_111 + np.array([0.0, 0.0, h_C])
            relative1 = hcp_111 + np.array([0.0, 0.0, h_O])

        traj.append('He')
        traj.positions[-1] = relative

        traj.append('Li')
        traj.positions[-1] = relative1

        write("CO_Pt111_top.dat",traj,format='lammps-data')
        shutil.move("CO_Pt111_top.dat",f"{m}/CO_Pt111_top.dat")

        print('successfully parsed frame', i)
        i += 1
        h_C += 0.1
        h_O += 0.1

    os.chdir('../')

for n in para_ads_111:
    os.mkdir(f"{n}")
    os.chdir(f"{n}")
    shutil.copyfile('../1.in',f'./1.in')
    shutil.copyfile('../lmp_0.0075.flare',f'./lmp_0.0075.flare')

    h_C = 20.82
    h_O = 20.82

    i = 0
    j = 0

    for m in range(1,51,1):
        os.mkdir(f"{m}")

        shutil.copyfile('../1.in',f'{m}/1.in')
        shutil.copyfile('../lmp_0.0075.flare',f'{m}/lmp_0.0075.flare')

        slab_111 = fcc111(element, size=(3,3,6), a=4.03, vacuum=10, periodic=True)
        write('Pt111_top.dat', slab_111, format="lammps-data")

        traj = read("Pt111_top.dat",format="lammps-data",style="atomic")

        if n == '111_top_para':
            relative = top_111 + np.array([-0.57, 0.0, h_C])
            relative1 = top_111 + np.array([0.57, 0.0, h_O])

        elif n == '111_top_para1':
            relative = top_111 + np.array([0.0, -0.57, h_C])
            relative1 = top_111 + np.array([0.0, 0.57, h_O])

        elif n == "111_bri_para":
            relative = bri_111 + np.array([-0.57, 0.0, h_C])
            relative1 = bri_111 + np.array([0.57, 0.0, h_O])

        elif n == "111_bri_para1":
            relative = bri_111 + np.array([0.0, -0.57, h_C])
            relative1 = bri_111 + np.array([0.0, 0.57, h_O])

        elif n == "111_fcc_para":
            relative = fcc_111 + np.array([-0.57, 0.0, h_C])
            relative1 = fcc_111 + np.array([0.57, 0.0, h_O])

        elif n == "111_fcc_para1":
            relative = fcc_111 + np.array([0.0, -0.57, h_C])
            relative1 = fcc_111 + np.array([0.0, 0.57, h_O])

        elif n == "111_hcp_para":
            relative = hcp_111 + np.array([-0.57, 0.0, h_C])
            relative1 = hcp_111 + np.array([0.57, 0.0, h_O])

        elif n == "111_hcp_para1":
            relative = hcp_111 + np.array([0.0, -0.57, h_C])
            relative1 = hcp_111 + np.array([0.0, 0.57, h_O])
        traj.append('He')
        traj.positions[-1] = relative

        traj.append('Li')
        traj.positions[-1] = relative1

        write("CO_Pt111_top.dat",traj,format='lammps-data')
        shutil.move("CO_Pt111_top.dat",f"{m}/CO_Pt111_top.dat")

        print('successfully parsed frame', i)
        i += 1
        h_C += 0.1
        h_O += 0.1

    os.chdir('../')

os.chdir('../')

# CO/Pt(100) Benchmarks

os.mkdir('100_CO')
os.chdir('100_CO')
shutil.copyfile('../2.in','./2.in')
shutil.copyfile('../lmp_0.0075.flare','./lmp_0.0075.flare')

perp_ads_100 = ["100_top_perp", "100_bri_perp", "100_hol_perp"]
perp_ads_i_100 = ["100_top_perp_i", "100_bri_perp_i", "100_hol_perp_i"]
para_ads_100 = ["100_top_para", "100_bri_para", "100_bri_para1", "100_hol_para"]

for n in perp_ads_100:
    os.mkdir(f"{n}")
    os.chdir(f"{n}")
    shutil.copyfile('../2.in',f'./2.in')
    shutil.copyfile('../lmp_0.0075.flare',f'./lmp_0.0075.flare')

    h_C = 19.285
    h_O = 20.425

    i = 0
    j = 0

    for m in range(1,51,1):
        os.mkdir(f"{m}")

        shutil.copyfile('../2.in',f'{m}/2.in')
        shutil.copyfile('../lmp_0.0075.flare',f'{m}/lmp_0.0075.flare')

        slab_100 = fcc100(element, size=(3,3,6), a=4.03, vacuum=10, periodic=True)
        write('Pt100_top.dat', slab_100, format="lammps-data")

        traj = read("Pt100_top.dat",format="lammps-data",style="atomic")

        if n == '100_top_perp':
            relative = top_100 + np.array([0.0, 0.0, h_C])
            relative1 = top_100 + np.array([0.0, 0.0, h_O])

        elif n == "100_bri_perp":
            relative = bri_100 + np.array([0.0, 0.0, h_C])
            relative1 = bri_100 + np.array([0.0, 0.0, h_O])

        elif n == "100_hol_perp":
            relative = hol_100 + np.array([0.0, 0.0, h_C])
            relative1 = hol_100 + np.array([0.0, 0.0, h_O])

        traj.append('He')
        traj.positions[-1] = relative

        traj.append('Li')
        traj.positions[-1] = relative1

        write("CO_Pt100_top.dat",traj,format='lammps-data')
        shutil.move("CO_Pt100_top.dat",f"{m}/CO_Pt100_top.dat")

        print('successfully parsed frame', i)
        i += 1
        h_C += 0.1
        h_O += 0.1

    os.chdir('../')

for n in perp_ads_i_100:
    os.mkdir(f"{n}")
    os.chdir(f"{n}")
    shutil.copyfile('../2.in',f'./2.in')
    shutil.copyfile('../lmp_0.0075.flare',f'./lmp_0.0075.flare')

    h_C = 20.425
    h_O = 19.285

    i = 0
    j = 0

    for m in range(1,51,1):
        os.mkdir(f"{m}")

        shutil.copyfile('../2.in',f'{m}/2.in')
        shutil.copyfile('../lmp_0.0075.flare',f'{m}/lmp_0.0075.flare')

        slab_100 = fcc100(element, size=(3,3,6), a=4.03, vacuum=10, periodic=True)
        write('Pt100_top.dat', slab_100, format="lammps-data")

        traj = read("Pt100_top.dat",format="lammps-data",style="atomic")

        if n == '100_top_perp_i':
            relative = top_100 + np.array([0.0, 0.0, h_C])
            relative1 = top_100 + np.array([0.0, 0.0, h_O])

        elif n == "100_bri_perp_i":
            relative = bri_100 + np.array([0.0, 0.0, h_C])
            relative1 = bri_100 + np.array([0.0, 0.0, h_O])

        elif n == "100_hol_perp_i":
            relative = hol_100 + np.array([0.0, 0.0, h_C])
            relative1 = hol_100 + np.array([0.0, 0.0, h_O])

        traj.append('He')
        traj.positions[-1] = relative

        traj.append('Li')
        traj.positions[-1] = relative1

        write("CO_Pt100_top.dat",traj,format='lammps-data')
        shutil.move("CO_Pt100_top.dat",f"{m}/CO_Pt100_top.dat")

        print('successfully parsed frame', i)
        i += 1
        h_C += 0.1
        h_O += 0.1

    os.chdir('../')

for n in para_ads_100:
    os.mkdir(f"{n}")
    os.chdir(f"{n}")
    shutil.copyfile('../2.in',f'./2.in')
    shutil.copyfile('../lmp_0.0075.flare',f'./lmp_0.0075.flare')

    h_C = 19.285
    h_O = 19.285

    i = 0
    j = 0

    for m in range(1,51,1):
        os.mkdir(f"{m}")

        shutil.copyfile('../2.in',f'{m}/2.in')
        shutil.copyfile('../lmp_0.0075.flare',f'{m}/lmp_0.0075.flare')

        slab_100 = fcc100(element, size=(3,3,6), a=4.03, vacuum=10, periodic=True)
        write('Pt100_top.dat', slab_100, format="lammps-data")

        traj = read("Pt100_top.dat",format="lammps-data",style="atomic")

        if n == '100_top_para':
            relative = top_100 + np.array([-0.57, 0.0, h_C])
            relative1 = top_100 + np.array([0.57, 0.0, h_O])

        elif n == "100_bri_para":
            relative = bri_100 + np.array([-0.57, 0.0, h_C])
            relative1 = bri_100 + np.array([0.57, 0.0, h_O])

        elif n == "100_bri_para1":
            relative = bri_100 + np.array([0.0, -0.57, h_C])
            relative1 = bri_100 + np.array([0.0, 0.57, h_O])

        elif n == "111_hol_para":
            relative = hol_100 + np.array([-0.57, 0.0, h_C])
            relative1 = hol_100 + np.array([0.57, 0.0, h_O])

        traj.append('He')
        traj.positions[-1] = relative

        traj.append('Li')
        traj.positions[-1] = relative1

        write("CO_Pt100_top.dat",traj,format='lammps-data')
        shutil.move("CO_Pt100_top.dat",f"{m}/CO_Pt100_top.dat")

        print('successfully parsed frame', i)
        i += 1
        h_C += 0.1
        h_O += 0.1

    os.chdir('../')

os.chdir('../')

# CO/Pt(100) Benchmarks
os.mkdir('110_CO')
os.chdir('110_CO')
shutil.copyfile('../3.in','./3.in')
shutil.copyfile('../lmp_0.0075.flare','./lmp_0.0075.flare')

perp_ads_110 = ["110_top_perp", "110_bri_perp", "110_lbri_perp", "110_hol_perp"]
perp_ads_i_110 = ["110_top_perp_i", "110_bri_perp_i", "110_lbri_perp_i", "110_hol_perp_i"]
para_ads_110 = ["110_top_para", "110_top_para1", "110_bri_para", "110_bri_para1", "110_lbri_para", "110_lbri_para1", "110_hol_para", "110_hol_para1"]

for n in perp_ads_110:
    os.mkdir(f"{n}")
    os.chdir(f"{n}")
    shutil.copyfile('../3.in',f'./3.in')
    shutil.copyfile('../lmp_0.0075.flare',f'./lmp_0.0075.flare')

    h_C = 16.38
    h_O = 17.52

    i = 0
    j = 0

    for m in range(1,51,1):
        os.mkdir(f"{m}")

        shutil.copyfile('../3.in',f'{m}/3.in')
        shutil.copyfile('../lmp_0.0075.flare',f'{m}/lmp_0.0075.flare')

        slab_110 = fcc110(element, size=(3,3,6), a=4.03, vacuum=10, periodic=True)
        write('Pt110_top.dat', slab_110, format="lammps-data")

        traj = read("Pt110_top.dat",format="lammps-data",style="atomic")

        if n == '110_top_perp':
            relative = top_110 + np.array([0.0, 0.0, h_C])
            relative1 = top_110 + np.array([0.0, 0.0, h_O])

        elif n == "110_bri_perp":
            relative = bri_110 + np.array([0.0, 0.0, h_C])
            relative1 = bri_110 + np.array([0.0, 0.0, h_O])

        elif n == "110_lbri_perp":
            relative = lbri_110 + np.array([0.0, 0.0, h_C])
            relative1 = lbri_110 + np.array([0.0, 0.0, h_O])

        elif n == "110_hol_perp":
            relative = hol_110 + np.array([0.0, 0.0, h_C])
            relative1 = hol_110 + np.array([0.0, 0.0, h_O])

        traj.append('He')
        traj.positions[-1] = relative

        traj.append('Li')
        traj.positions[-1] = relative1

        write("CO_Pt110_top.dat",traj,format='lammps-data')
        shutil.move("CO_Pt110_top.dat",f"{m}/CO_Pt110_top.dat")

        print('successfully parsed frame', i)
        i += 1
        h_C += 0.1
        h_O += 0.1

    os.chdir('../')

for n in perp_ads_i_110:
    os.mkdir(f"{n}")
    os.chdir(f"{n}")
    shutil.copyfile('../3.in',f'./3.in')
    shutil.copyfile('../lmp_0.0075.flare',f'./lmp_0.0075.flare')

    h_C = 17.52
    h_O = 16.38

    i = 0
    j = 0

    for m in range(1,51,1):
        os.mkdir(f"{m}")

        shutil.copyfile('../3.in',f'{m}/3.in')
        shutil.copyfile('../lmp_0.0075.flare',f'{m}/lmp_0.0075.flare')

        slab_110 = fcc110(element, size=(3,3,6), a=4.03, vacuum=10, periodic=True)
        write('Pt110_top.dat', slab_110, format="lammps-data")

        traj = read("Pt110_top.dat",format="lammps-data",style="atomic")

        if n == '110_top_perp_i':
            relative = top_110 + np.array([0.0, 0.0, h_C])
            relative1 = top_110 + np.array([0.0, 0.0, h_O])

        elif n == "110_bri_perp_i":
            relative = bri_110 + np.array([0.0, 0.0, h_C])
            relative1 = bri_110 + np.array([0.0, 0.0, h_O])

        elif n == "110_lbri_perp_i":
            relative = lbri_110 + np.array([0.0, 0.0, h_C])
            relative1 = lbri_110 + np.array([0.0, 0.0, h_O])

        elif n == "110_hol_perp_i":
            relative = hol_110 + np.array([0.0, 0.0, h_C])
            relative1 = hol_110 + np.array([0.0, 0.0, h_O])

        traj.append('He')
        traj.positions[-1] = relative

        traj.append('Li')
        traj.positions[-1] = relative1

        write("CO_Pt110_top.dat",traj,format='lammps-data')
        shutil.move("CO_Pt110_top.dat",f"{m}/CO_Pt110_top.dat")

        print('successfully parsed frame', i)
        i += 1
        h_C += 0.1
        h_O += 0.1

    os.chdir('../')

for n in para_ads_110:
    os.mkdir(f"{n}")
    os.chdir(f"{n}")
    shutil.copyfile('../3.in',f'./3.in')
    shutil.copyfile('../lmp_0.0075.flare',f'./lmp_0.0075.flare')

    h_C = 16.38
    h_O = 16.38

    i = 0
    j = 0

    for m in range(1,51,1):
        os.mkdir(f"{m}")

        shutil.copyfile('../3.in',f'{m}/3.in')
        shutil.copyfile('../lmp_0.0075.flare',f'{m}/lmp_0.0075.flare')

        slab_110 = fcc110(element, size=(3,3,6), a=4.03, vacuum=10, periodic=True)
        write('Pt110_top.dat', slab_110, format="lammps-data")

        traj = read("Pt110_top.dat",format="lammps-data",style="atomic")

        if n == '110_top_para':
            relative = top_110 + np.array([-0.57, 0.0, h_C])
            relative1 = top_110 + np.array([0.57, 0.0, h_O])

        elif n == '110_top_para1':
            relative = top_110 + np.array([0.0, -0.57, h_C])
            relative1 = top_110 + np.array([0.0, 0.57, h_O])

        elif n == "110_bri_para":
            relative = bri_110 + np.array([-0.57, 0.0, h_C])
            relative1 = bri_110 + np.array([0.57, 0.0, h_O])

        elif n == "110_bri_para1":
            relative = bri_110 + np.array([0.0, -0.57, h_C])
            relative1 = bri_110 + np.array([0.0, 0.57, h_O])

        elif n == "110_lbri_para":
            relative = lbri_110 + np.array([-0.57, 0.0, h_C])
            relative1 = lbri_110 + np.array([0.57, 0.0, h_O])

        elif n == "110_lbri_para1":
            relative = lbri_110 + np.array([0.0, -0.57, h_C])
            relative1 = lbri_110 + np.array([0.0, 0.57, h_O])

        elif n == "110_hol_para":
            relative = hol_110 + np.array([-0.57, 0.0, h_C])
            relative1 = hol_110 + np.array([0.57, 0.0, h_O])

        elif n == "110_hol_para1":
            relative = hol_110 + np.array([0.0, -0.57, h_C])
            relative1 = hol_110 + np.array([0.0, 0.57, h_O])

        traj.append('He')
        traj.positions[-1] = relative

        traj.append('Li')
        traj.positions[-1] = relative1
        
        write("CO_Pt110_top.dat",traj,format='lammps-data')
        shutil.move("CO_Pt110_top.dat",f"{m}/CO_Pt110_top.dat")

        print('successfully parsed frame', i)
        i += 1
        h_C += 0.1
        h_O += 0.1

    os.chdir('../')

os.chdir('../')

print("Successfully Created All Directories and Files, Job well done")
