import joblib
import osmnx as ox

import numpy as np
import matplotlib.pyplot as plt


def read_txt_column(data_name, f_row='delete'):
    data = open(data_name)
    result = []
    for line in data.readlines():
        a = line.split(',')
        result.append(a)
    if f_row == 'delete':
        del result[0]
    result_array = np.array(result, dtype=float)
    return result_array


# read data
# ---------------------------------------------------------------------------------------
bsm_file = "./x_y_bsm.txt"
sanitized_bsm_file = "./x_y_bsm_sanitized.txt"
data_bsm = read_txt_column(bsm_file)
sanitized_bsm = read_txt_column(sanitized_bsm_file)

x = data_bsm[:, 0]
y = data_bsm[:, 1]
s_x = sanitized_bsm[:, 0]
s_y = sanitized_bsm[:, 1]


# # draw a figure of trajectory with map
# #---------------------------------------------------------------------------------------
# # draw_map
# G_pro=joblib.load('NTU_project_map_filled.pkl')
# fig,ax=ox.plot_graph(G_pro,show=False,close=False,node_color='#999999')

# # draw_trajectory
# ax.scatter(s_x[0],s_y[0], s=70, label='EKF Start', c='y',marker='o')
# ax.scatter(x[0], y[0], s=70, label='Start', c='g',marker='*')

# plt.plot(s_x[::5],s_y[::5], '+',mfc='none',label='EKF Position', c='k', markersize=5)
# plt.plot(x[::10],y[::10],'o',mfc='none',label='GPS Measurements',c='r',markersize=5)

# plt.plot(s_x[-1],s_y[-1], 's', label='EKF Goal', c='r',markersize=10)
# plt.plot(x[-1],y[-1],'X',  label='Goal', c='b',markersize=10)

# plt.xlabel('X [m]')
# plt.ylabel('Y [m]')
# plt.legend(loc='best')
# plt.axis('equal')
# plt.show()

# generate video
# ----------------------------------------------------------------------------
plt.ion()
G_pro = joblib.load('NTU_project_map_filled.pkl')
fig, ax = ox.plot_graph(G_pro, show=False, close=False,
                        node_color='#16d2d9', bgcolor="#ffffff")

ax.scatter(x[0], y[0], s=60, label='Start', c='y')
plt.pause(1)
ax.scatter(s_x[0], s_y[0], s=60, label='EKF Start', c='g')
ax.legend(loc='best')
plt.pause(3)

for i in range(len(x)//5):
    ax.set_title('Driver behavior: Normal')
    ax.scatter(x[5*i], y[5*i], s=50,
               label='GPS Measurements', c='r', marker='+')
    plt.pause(0.001)
    ax.scatter(s_x[5*i], s_y[5*i], s=50,
               label='EKF Position', c='k', marker='+')
    if i == 0:
        plt.pause(2)
        ax.legend(loc='best')
    plt.pause(0.001)

ax.scatter(s_x[-1], s_y[-1], s=60, label='EKF Goal', c='r')
ax.scatter(x[-1], y[-1], s=60, label='Goal', c='b')
ax.legend(loc='best')
plt.pause(2)
