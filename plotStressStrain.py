import os
import numpy as np
import matplotlib.pyplot as plt

#phi_list = [20.0]
phi_list = [15.0, 20.0, 25.5, 30.0, 35.0]
confining_stress_list = ['0.34e6', '6.89e6', '13.79e6']

plt.figure(1)
#plt.title('Hertz model')  
plt.xlabel('Strain / %')  
plt.ylabel('Peak strength / MPa')   
# creat the BTS_peak_points.dat
xy_data_file = os.path.join(os.getcwd(),'Tensile_data.txt')
with open(xy_data_file, "r") as f_xy_data:
    count = 29
    for line in f_xy_data.readlines():
        count += 1
        if count % 10 == 0 and count < 71 and count > 69:
            values = [float(s) for s in line.split()]
            sigma_limit = int(values[0])
            shear_limit = int(values[1])

            for phi in phi_list:

                for confining_stress in confining_stress_list:

                    #creat new folder
                    aim_folder_name = 'Triaxial_Sigma' + str(sigma_limit) + '_Shear' + str(shear_limit) + '_Phi' + str(phi) + '_P' + str(confining_stress)
                    aim_path_and_name = os.path.join(os.getcwd(),'Generated_Triaxial_cases', aim_folder_name, 'G-Triaxial_Graphs', 'G-Triaxial_graph.grf')

                    if os.path.isfile(aim_path_and_name):
                        X11, Y11 = [], []
                        with open(aim_path_and_name, 'r') as Young_data:
                            for line in Young_data:
                                values = [float(s) for s in line.split()]
                                if confining_stress == '6.89e6':
                                    X11.append(values[0])
                                elif confining_stress == '13.79e6':
                                    X11.append(values[0])
                                else:
                                    X11.append(values[0])
                                Y11.append((values[1] - float(confining_stress))* 1e-6)
                        
                        plt.plot(X11, Y11, '--', label = aim_folder_name)

#plt.axhline(y=7.12776, color='red', linestyle='-')

X11, Y11 = [], []
with open('exp_0.34.txt', 'r') as Young_data:
    for line in Young_data:
        values = [float(s) for s in line.split()]
        X11.append(values[0]+0.05) 
        Y11.append(values[1])
X12, Y12 = [], []
with open('exp_6.89.txt', 'r') as Young_data:
    for line in Young_data:
        values = [float(s) for s in line.split()]
        X12.append(values[0]) 
        Y12.append(values[1])
X13, Y13 = [], []
with open('exp_13.79.txt', 'r') as Young_data:
    for line in Young_data:
        values = [float(s) for s in line.split()]
        X13.append(values[0]) 
        Y13.append(values[1])

#plt.plot(X11, Y11, '-',color='black', label = "experiment-0.34")
##plt.plot(X12, Y12, '-',color='red', label = "experiment-6.89")
#plt.plot(X13, Y13, '-',color='blue', label = "experiment-13.79")


#plt.xlim((0, 4))
#plt.ylim((0, 40))
plt.legend(prop={'size': 8})
plt.show()  

        