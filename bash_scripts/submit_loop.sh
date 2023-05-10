#!/bin/bash

for i in {1..12}; do cd ${i}/; sbatch run_script; cd ../; done
