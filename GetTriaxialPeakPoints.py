import os

#sigma_limit_list = [10, 100, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000]
#tension_limit_list = [10, 100, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000]
#sigma_limit_list = [100, 500, 1000, 5000, 10000, 50000, 100000, 500000]
#shear_limit_list = [10000, 50000, 100000, 200000, 300000, 400000, 500000, 600000]
friction_list = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0]

# creat the BTS_peak_points.dat
BTS_peak_points_path_and_name = os.path.join(os.getcwd(),'Triaxial_peak_points.dat')
with open(BTS_peak_points_path_and_name, "w") as f_w_peak_points:

    xy_data_file = os.path.join(os.getcwd(),'Tensile_data.txt')
    with open(xy_data_file, "r") as f_xy_data:
        count = 9
        for line in f_xy_data.readlines():
            count += 1
            if count % 10 == 0:
                values = [float(s) for s in line.split()]
                sigma_limit = int(values[0])
                shear_limit = int(values[1])

                for friction in friction_list:

                    friction_to_name = str(friction).replace(".", 'dot')
                    #creat new folder
                    aim_folder_name = 'Triaxial_Sigma' + str(sigma_limit) + '_Shear' + str(shear_limit) + '_Fric' + friction_to_name
                    aim_path_and_name = os.path.join(os.getcwd(),'Generated_Triaxial_cases', aim_folder_name, 'G-Triaxial_Graphs', 'G-Triaxial_graph.grf')

                    triaxial_data_list = []
                    with open(aim_path_and_name, 'r') as tensile_data:
                        for line in tensile_data:
                            values = [float(s) for s in line.split()]
                            triaxial_data_list.append(values[1]) 

                    # write BTS_peak_points.dat
                    f_w_peak_points.write(str(sigma_limit) + ' ' + str(friction) + ' ' + str(max(triaxial_data_list)) + '\n')
