import os

ball_young_list = ['1e9', '1e10', '3e10', '5e10', '1e11']
bond_young_list = ['1e7', '1e8', '3e8', '5e8', '1e9']

# creat the BTS_peak_points.dat
BTS_peak_points_path_and_name = os.path.join(os.getcwd(),'Triaxial_max_young.dat')
with open(BTS_peak_points_path_and_name, "w") as f_w_peak_points:

    for ball_young in ball_young_list:
        for bond_young in bond_young_list:

            #creat new folder
            aim_folder_name = 'Triaxial_pE' + ball_young + '_bE' + bond_young
            aim_path_and_name = os.path.join(os.getcwd(),'Generated_Triaxial_cases', aim_folder_name, 'G-Triaxial_Graphs', 'G-Triaxial_graph_young.grf')

            triaxial_data_list = []
            with open(aim_path_and_name, 'r') as tensile_data:
                for line in tensile_data:
                    values = [float(s) for s in line.split()]
                    triaxial_data_list.append(values[1]) 

            # write BTS_peak_points.dat
            f_w_peak_points.write(ball_young + ' ' + bond_young + ' ' + str(max(triaxial_data_list)) + '\n')
