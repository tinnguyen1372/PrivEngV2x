# from generate_path import G_pro
import threading
import osmnx as ox
from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, url_for
import pickle
import joblib
import time
import os
# import generate_copy
import runpy
import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure


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

# global G_pro, fig, ax


def run_map_init():

    print("Loading map!")

    # draw a figure of trajectory with map
    # ---------------------------------------------------------------------------------------
    # draw_map
    global G_pro
    global fig
    global ax
    G_pro = joblib.load('NTU_project_map_filled.pkl')
    fig, ax = ox.plot_graph(G_pro, show=False, close=False,
                            node_color='#16d2d9', bgcolor="#ffffff")

    print("Loaded map!")
    # draw_trajectory


def run_path_live():
    # read data
    # ---------------------------------------------------------------------------------------
    bsm_file = "./output_raw.txt"
    sanitized_bsm_file = "./output_sanitized.txt"
    data_bsm = read_txt_column(bsm_file)
    sanitized_bsm = read_txt_column(sanitized_bsm_file)

    x = data_bsm[:, 0]
    y = data_bsm[:, 1]
    s_x = sanitized_bsm[:, 0]
    s_y = sanitized_bsm[:, 1]
    # ax.scatter(s_x[0], s_y[0], s=70, label='EKF Start', c='y', marker='o')
    # ax.scatter(x[0], y[0], s=70, label='Start', c='g', marker='*')

    plt.plot(s_x[::5], s_y[::5], '+', mfc='none',
             #  label='EKF Position',
             c='k', markersize=5)
    plt.plot(x[::10], y[::10], 'o', mfc='none',
             #  label='GPS Measurements',
             c='r', markersize=5)

    # plt.plot(s_x[-1], s_y[-1], 's', label='EKF Goal', c='r', markersize=10)
    # plt.plot(x[-1], y[-1], 'X',  label='Goal', c='b', markersize=10)
    plt.plot(s_x[-1], s_y[-1], 's',  c='r', markersize=10)
    plt.plot(x[-1], y[-1], 'X',   c='b', markersize=10)
    plt.xlabel('X [m]')
    plt.ylabel('Y [m]')
    plt.legend(loc='best')
    plt.axis('equal')
    plt.savefig("./static/live.jpg", dpi=200)
    # plt.show()


app = Flask(__name__)
# app.config['UPLOAD_EXTENSIONS'] = ['.txt']


@app.route('/input.html', methods=['GET', 'POST'])
@app.route('/input', methods=['GET', 'POST'])
def input():
    if os.path.isfile('./static/path.jpg'):
        os.remove("./static/path.jpg")
    if os.path.isfile('./static/result.mp4'):
        os.remove("./static/result.mp4")
    if os.path.isfile('./static/live.jpg'):
        os.remove("./static/live.jpg")
    if os.path.isfile('x_y_bsm_sanitized.txt'):
        os.remove("x_y_bsm_sanitized.txt")
    if os.path.isfile('x_y_bsm.txt'):
        os.remove("x_y_bsm.txt")
    if request.method == 'POST':
        raw_file = request.files['raw']
        sanitized_file = request.files['sanitized']
        if raw_file.filename != '':
            raw_file.save("x_y_bsm.txt")
        if sanitized_file.filename != '':
            sanitized_file.save("x_y_bsm_sanitized.txt")
        # file = open('generate_copy.py', 'r').read()
        if sanitized_file.filename != '' and raw_file.filename != '':
            runpy.run_path(path_name='generate_copy.py')
            runpy.run_path(path_name='generate_path.py')
            return redirect(url_for('main'))
    return render_template("input.html")


count = 0


@app.route('/live.html', methods=["GET", "POST"])
@app.route('/live', methods=["GET", "POST"])
def live():
    global count
    if count == 0:
        run_map_init()
        count = count + 1
    run_path_live()
    # runpy.run_path(path_name='generate_path_live.py')

    return render_template("live.html")


# @app.route("/loading.html")
# @app.route("/loading")
# # def run_script():
# #     file = open(r'generate_copy.py', 'r').read()
# #     return exec(file)
# # def loading():
# #     redirect(url_for('main'))
# #     return render_template("loading.html")
# def redirect():
#     return redirect(url_for('main'))

@app.route("/imageshow.html")
def imageShow():
    return render_template("imageshow.html")


@app.route("/main.html")
@app.route("/main")
def main():
    return render_template("main.html")


@app.route("/login.html")
@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register.html")
@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/tutorial.html")
@app.route("/tutorial")
def tutorial():
    return render_template("tutorial.html")


@app.route("/About.html")
@app.route("/about")
def about():
    return render_template("About.html")


@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    # app.run(debug=True)
    from livereload import Server
    server = Server(app.wsgi_app)
    # server.watch('x_y_bsm_sanitized_test.txt')
    server.watch('output_raw.txt')
    server.watch('output_sanitized.txt')
    server.serve(open_url_delay=0, debug=False)
