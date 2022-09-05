#!/bin/bash
#SBATCH --job-name=UCS-linear
#SBATCH --output=DPBM-ssmall-rR-5e11-Eb1e9-5e4-5e4-0.34-f0.05-ph40%j.out
#SBATCH --error=DPBM-ssmall-rR-5e11-Eb1e9-5e4-5e4-0.34-f0.05-ph40%j.err
#SBATCH --partition=HighParallelization
#SBATCH --ntasks-per-node=10

##Optional - Required memory in MB per node, or per core. Defaults are 1GB per core.
##SBATCH --mem=3096
#SBATCH --mem-per-cpu=3096
##SBATCH --exclusive

##Optional - Estimated execution time
##Acceptable time formats include  "minutes",   "minutes:seconds",
##"hours:minutes:seconds",   "days-hours",   "days-hours:minutes" ,"days-hours:minutes:seconds".
#SBATCH --time=10-0

########### Further details -> man sbatch ##########
#export OMP_NUM_THREADS=10

python3 decompressed_material_triaxial_test_PBM_220905.py