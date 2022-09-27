import os

ball_young_list = ['1e9', '1e10', '3e10', '5e10', '1e11']
bond_young_list = ['1e7', '1e8', '3e8', '5e8', '1e9']
confining_stress_list = ['0.34e6', '6.89e6', '13.79e6']

# creat the BTS_peak_points.dat
BTS_peak_points_path_and_name = os.path.join(os.getcwd(),'Triaxial_young_error.dat')
with open(BTS_peak_points_path_and_name, "w") as f_w_peak_points:

    for ball_young in ball_young_list:

        for bond_young in bond_young_list:

            error_ratio = 0.0

            for confining_stress in confining_stress_list:

                #creat new folder
                aim_folder_name = 'Triaxial_pE' + ball_young + '_bE' + bond_young + '_P' + str(confining_stress)
                aim_path_and_name = os.path.join(os.getcwd(),'Generated_Triaxial_cases', aim_folder_name, 'G-Triaxial_Graphs', 'G-Triaxial_graph_young.grf')

                triaxial_data_list = []
                with open(aim_path_and_name, 'r') as tensile_data:
                    for line in tensile_data:
                        values = [float(s) for s in line.split()]
                        triaxial_data_list.append(values[1] * 1e-6) 
                if confining_stress == '0.34e6':
                    error_ratio += 100 * abs(max(triaxial_data_list) - 7.12776) / 7.12776
                elif confining_stress == '6.89e6':
                    error_ratio += 100 * abs(max(triaxial_data_list) - 21.3874) / 21.3874
                elif confining_stress == '13.79e6':
                    error_ratio += 100 * abs(max(triaxial_data_list) - 39.6693) / 39.6693

            # write BTS_peak_points.dat
            f_w_peak_points.write(ball_young + ' ' + bond_young + ' ' + str(error_ratio / 3.0) + '\n')
