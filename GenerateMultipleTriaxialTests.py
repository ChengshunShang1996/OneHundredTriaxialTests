import os
import shutil
#import numpy as np

confining_stress_list = ['0.34e6', '6.89e6', '13.79e6']


# creat the cases_run.sh
cases_run_path_and_name = os.path.join(os.getcwd(),'cases_run.sh')
with open(cases_run_path_and_name, "w") as f_w_cases_run:
    f_w_cases_run.write('#!/bin/bash'+'\n')

    xy_data_file = os.path.join(os.getcwd(),'Tensile_data.txt')
    with open(xy_data_file, "r") as f_xy_data:
        count = 4
        for line in f_xy_data.readlines():
            count += 1
            if count % 5 == 0:
                values = [float(s) for s in line.split()]
                sigma_limit = int(values[0])
                shear_limit = int(values[1])

                for confining_stress in confining_stress_list:

                    #creat new folder
                    new_folder_name = 'Triaxial_Sigma' + str(sigma_limit) + '_Shear' + str(shear_limit) + '_P' + str(confining_stress)
                    aim_path = os.path.join(os.getcwd(),'Generated_Triaxial_cases', new_folder_name)
                    if os.path.exists(aim_path):
                        shutil.rmtree(aim_path)
                    os.mkdir(aim_path)

                    #copy source file
                    seed_file_name_list = ['decompressed_material_triaxial_test_PBM_220912.py', 'G-TriaxialDEM_FEM_boundary.mdpa', 'G-TriaxialDEM.mdpa', 'ProjectParametersDEM.json', 'MaterialsDEM.json', 'run_omp.sh']
                    for seed_file_name in seed_file_name_list:
                        seed_file_path_and_name = os.path.join(os.getcwd(),'Triaxial_seed_files',seed_file_name)
                        aim_file_path_and_name = os.path.join(aim_path, seed_file_name)

                        if seed_file_name == 'MaterialsDEM.json':
                            with open(seed_file_path_and_name, "r") as f_material:
                                with open(aim_file_path_and_name, "w") as f_material_w:
                                    for line in f_material.readlines():
                                        if "BOND_SIGMA_MAX" in line:
                                            line = line.replace("1e3", str(sigma_limit))
                                        if "BOND_TAU_ZERO" in line:
                                            line = line.replace("2.6e6", str(shear_limit))
                                        f_material_w.write(line)
                        elif seed_file_name == 'ProjectParametersDEM.json':
                            with open(seed_file_path_and_name, "r") as f_parameter:
                                with open(aim_file_path_and_name, "w") as f_parameter_w:
                                    for line in f_parameter.readlines():
                                        if "ConfinementPressure" in line:
                                            line = line.replace("0.34e6", confining_stress)
                                        f_parameter_w.write(line)
                        elif seed_file_name == 'run_omp.sh':
                            with open(seed_file_path_and_name, "r") as f_run_omp:
                                with open(aim_file_path_and_name, "w") as f_run_omp_w:
                                    for line in f_run_omp.readlines():
                                        if "BTS-Q-Ep6.2e10-T1e3-f0.1" in line:
                                            line = line.replace("BTS-Q-Ep6.2e10-T1e3-f0.1", new_folder_name)
                                        f_run_omp_w.write(line)
                        else:
                            shutil.copyfile(seed_file_path_and_name, aim_file_path_and_name) 

                    # write the cases_run.sh
                    f_w_cases_run.write('cd '+ aim_path + '\n')
                    f_w_cases_run.write('sbatch run_omp.sh' + '\n')


