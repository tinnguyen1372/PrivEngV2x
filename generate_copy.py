import joblib
import osmnx as ox

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


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

G_pro = joblib.load('NTU_project_map_filled.pkl')
fig, ax = ox.plot_graph(G_pro, show=False, close=False,
                        node_color='#16d2d9', bgcolor="#ffffff")
ax.scatter(x[0], y[0], s=60, label='Start', c='y')

ax.scatter(s_x[0], s_y[0], s=60, label='EKF Start', c='g')
ax.legend(loc='best')
# plt.pause(3)
ax.set_title('Driver behavior: Normal')

xdata, ydata = [], []
s_xdata, s_ydata = [], []
raw_trj, = plt.plot([], [], '+', mfc='none',
                    label='EKF Position', c='k', markersize=5)
est_trj, = plt.plot([], [], 'o', mfc='none',
                    label='GPS Measurements', c='r', markersize=5)


def init():
    ax.legend(loc='best')
    return raw_trj, est_trj,


def animate(i):
    if i < len(x)//15:
        print(i)
        xdata.append(x[15*i])
        ydata.append(y[15*i])
        s_xdata.append(s_x[15*i])
        s_ydata.append(s_y[15*i])
        raw_trj.set_data(xdata, ydata)
        est_trj.set_data(s_xdata, s_ydata)
        return raw_trj, est_trj,
    if i == len(x)//15:
        print(i)
        EKF_GAOL = ax.scatter(s_x[-1], s_y[-1], s=60, label='EKF Goal', c='r')
        GOAL = ax.scatter(x[-1], y[-1], s=60, label='Goal', c='b')
        ax.legend(loc='best')
        return EKF_GAOL, GOAL


# ax.scatter(s_x[-1], s_y[-1], s=60, label='EKF Goal', c='r')
# ax.scatter(x[-1], y[-1], s=60, label='Goal', c='b')
# ax.legend(loc='best')
anim = animation.FuncAnimation(fig, animate,
                               interval=200, repeat=False, save_count=len(x)//15+1,
                               init_func=init, blit=False)
# plt.show()
anim.save('./static/result.mp4', dpi=150)
