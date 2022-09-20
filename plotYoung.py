import os
import numpy as np
import matplotlib.pyplot as plt

#ball_young_list = ['1e10']
ball_young_list = ['1e9', '1e10', '3e10', '5e10', '1e11']
bond_young_list = ['1e7', '1e8', '3e8', '5e8', '1e9']
#bond_young_list = ['1e9']

plt.figure(1)
#plt.title('Hertz model')  
plt.xlabel('Strain / %')  
plt.ylabel('Peak strength / MPa')   
# creat the BTS_peak_points.dat
for ball_young in ball_young_list:

    for bond_young in bond_young_list:

        #creat new folder
        aim_folder_name = 'Triaxial_pE' + ball_young + '_bE' + bond_young
        aim_path_and_name = os.path.join(os.getcwd(),'Generated_Triaxial_cases', aim_folder_name, 'G-Triaxial_Graphs', 'G-Triaxial_graph.grf')

        if os.path.isfile(aim_path_and_name):
            X11, Y11 = [], []
            with open(aim_path_and_name, 'r') as Young_data:
                for line in Young_data:
                    values = [float(s) for s in line.split()]
                    X11.append(values[0]) 
                    Y11.append(values[1]* 1e-6)
            
            plt.plot(X11, Y11, '--', label = aim_folder_name)

#plt.axhline(y=7.12776, color='red', linestyle='-')

X11, Y11 = [], []
with open('exp_0.34.txt', 'r') as Young_data:
    for line in Young_data:
        values = [float(s) for s in line.split()]
        X11.append(values[0]+0.05) 
        Y11.append(values[1])

plt.plot(X11, Y11, '-',color='black', label = "experiment")

#plt.xlim((0, 1))
#plt.ylim((0, 5))
plt.legend(prop={'size': 8})
plt.show()  

        