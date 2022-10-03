import os

#sigma_limit_list = [10, 100, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000]
#tension_limit_list = [10, 100, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000]
#sigma_limit_list = [100, 500, 1000, 5000, 10000, 50000, 100000, 500000]
#shear_limit_list = [10000, 50000, 100000, 200000, 300000, 400000, 500000, 600000]
#friction_list = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
#phi_list = [15.0, 20.0, 25.5, 30.0, 35.0]
confining_stress_list = ['0.34e6', '6.89e6', '13.79e6']

# creat the BTS_peak_points.dat
BTS_peak_points_path_and_name = os.path.join(os.getcwd(),'Triaxial_peak_points_errors.dat')
with open(BTS_peak_points_path_and_name, "w") as f_w_peak_points:

    xy_data_file = os.path.join(os.getcwd(),'Tensile_data_low.txt')
    with open(xy_data_file, "r") as f_xy_data:
        count = 1
        for line in f_xy_data.readlines():
            count += 1
            if count % 2 == 0 and count < 19:
                values = [float(s) for s in line.split()]
                sigma_limit = int(values[0])
                shear_limit = int(values[1])

                rel_error = 0.0

                for confining_stress in confining_stress_list:

                    #creat new folder
                    aim_folder_name = 'Triaxial_Sigma' + str(sigma_limit) + '_Shear' + str(shear_limit) + '_P' + confining_stress
                    aim_path_and_name = os.path.join(os.getcwd(),'Generated_Triaxial_cases', aim_folder_name, 'G-Triaxial_Graphs', 'G-Triaxial_graph.grf')

                    triaxial_data_list = []
                    with open(aim_path_and_name, 'r') as tensile_data:
                        for line in tensile_data:
                            values = [float(s) for s in line.split()]
                            if len(values) > 2:
                                triaxial_data_list.append(values[1])
                            else:
                                triaxial_data_list.append(0.0) 
                    
                    if confining_stress == '0.34e6':
                        rel_error += 100 * abs(max(triaxial_data_list) - 2.5842e6) / 2.5842e6
                    elif confining_stress == '6.89e6':
                        rel_error += 100 * abs(max(triaxial_data_list) - 11.9814e6) / 11.9814e6
                    elif confining_stress == '13.79e6':
                        rel_error += 100 * abs(max(triaxial_data_list) - 20.4294e6) / 11.9814e6

                # write BTS_peak_points.dat
                f_w_peak_points.write(str(sigma_limit) + ' ' + str(shear_limit) + ' ' + str(rel_error) + '\n')
