import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties



def insert_plot():
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.set_title("INSERT operation: Comparision the performance of MongoDB between Go, C++, Java, Python")
    ax1.set_xlabel("Total number of inserts")
    ax1.set_ylabel("Time consuming (s)")
    s = 20

    x_go = [10,100,1000,10000]
    y_go = [0.229612, 0.266048, 0.452230, 1.151501]

    x_cpp = [10,100,1000,10000]
    y_cpp = [0.261295,0.280558,0.313579,1.22066]

    x_java = [10,100,1000,10000]
    y_java = [0.2121, 0.253, 0.4392, 1.0695]

    x_python = [10,100,1000,10000]
    y_python = [0.22376224994659424, 0.2863401174545288, 0.46742677688598633, 3.0006872177124024]

    s = 20

    ax1.scatter(x_go,y_go,s=s,c="k", marker="o")
    ax1.plot(x_go,y_go,c='r',ls="-",label='Go')

    ax1.scatter(x_cpp,y_cpp,s=s,c="k", marker="x")
    ax1.plot(x_cpp,y_cpp,c='y',ls=":",label='C++')

    ax1.scatter(x_java,y_java,s=s,c="k", marker="+")
    ax1.plot(x_java,y_java,c='g',ls="-.",label='Java')

    ax1.scatter(x_python,y_python,s=s,c="k", marker="*")
    ax1.plot(x_python,y_python,c='b',ls="--",label='Python')

    fontP = FontProperties()
    fontP.set_size('small')
    plt.legend(prop=fontP, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=3)  # Move legend outside of figure in matplotlib

    plt.show()

def update_oneByOne_plot():
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.set_title("UPDATE operation(one by one): Comparision the performance of MongoDB between Go, C++, Java, Python")
    ax1.set_xlabel("Total number of updates")
    ax1.set_ylabel("Time consuming (s)")
    s = 20

    x_go = [10,100,1000,10000]
    y_go = [0.005159, 0.055728, 0.356072, 27.228654]

    x_cpp = [10,100,1000,10000]
    y_cpp = [0.005478, 0.0187123, 0.327923, 29.3875]

    x_java = [10,100,1000,10000]
    y_java = [0.0161, 0.0324, 0.3155, 28.5541]

    x_python = [10,100,1000,10000]
    y_python = [0.011017060279846192, 0.030140042304992676, 0.5247245073318482, 33.805678081512454]

    s = 20

    ax1.scatter(x_go,y_go,s=s,c="k", marker="o")
    ax1.plot(x_go,y_go,c='r',ls="-",label='Go')

    ax1.scatter(x_cpp,y_cpp,s=s,c="k", marker="x")
    ax1.plot(x_cpp,y_cpp,c='y',ls=":",label='C++')

    ax1.scatter(x_java,y_java,s=s,c="k", marker="+")
    ax1.plot(x_java,y_java,c='g',ls="-.",label='Java')

    ax1.scatter(x_python,y_python,s=s,c="k", marker="*")
    ax1.plot(x_python,y_python,c='b',ls="--",label='Python')

    fontP = FontProperties()
    fontP.set_size('small')
    plt.legend(prop=fontP, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=3)  # Move legend outside of figure in matplotlib

    plt.show()

def update_random_plot():
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.set_title("UPDATE operation(randomly): Comparision the performance of MongoDB between Go, C++, Java, Python")
    ax1.set_xlabel("Total number of updates")
    ax1.set_ylabel("Time consuming (s)")
    s = 20

    x_go = [10,100,1000,10000]
    y_go = [0.005194, 0.031363, 0.377351, 29.825594]

    x_cpp = [10,100,1000,10000]
    y_cpp = [0.0053837, 0.0129166, 0.336743, 30.5121]

    x_java = [10,100,1000,10000]
    y_java = [0.0114, 0.0179, 0.32399999, 31.70710]

    x_python = [10,100,1000,10000]
    y_python = [0.010803699493408203, 0.029072666168212892, 0.5410110473632812, 36.167938923835756]

    s = 20


    ax1.scatter(x_go,y_go,s=s,c="k", marker="o")
    ax1.plot(x_go,y_go,c='r',ls="-",label='Go')

    ax1.scatter(x_cpp,y_cpp,s=s,c="k", marker="x")
    ax1.plot(x_cpp,y_cpp,c='y',ls=":",label='C++')

    ax1.scatter(x_java,y_java,s=s,c="k", marker="+")
    ax1.plot(x_java,y_java,c='g',ls="-.",label='Java')

    ax1.scatter(x_python,y_python,s=s,c="k", marker="*")
    ax1.plot(x_python,y_python,c='b',ls="--",label='Python')

    fontP = FontProperties()
    fontP.set_size('small')
    plt.legend(prop=fontP, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=3)  # Move legend outside of figure in matplotlib

    plt.show()

def find_onebyOne_plot():
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.set_title("FIND operation(one by one): Comparision the performance of MongoDB between Go, C++, Java, Python")
    ax1.set_xlabel("Total number of finds")
    ax1.set_ylabel("Time consuming (s)")
    s = 20

    x_go = [10,100,1000,10000]
    y_go = [0.004473, 0.016279, 0.365470, 30.415884]

    x_cpp = [10,100,1000,10000]
    y_cpp = [0.004717, 0.0104032, 0.312359, 31.7203]

    x_java = [10,100,1000,10000]
    y_java = [0.008599999999999998, 0.0224, 0.5, 60.9134]

    x_python = [10,100,1000,10000]
    y_python = [0.010096120834350585, 0.029318642616271973, 0.5403760194778442, 36.07794299125671]

    s = 20

    ax1.scatter(x_go,y_go,s=s,c="k", marker="o")
    ax1.plot(x_go,y_go,c='r',ls="-",label='Go')

    ax1.scatter(x_cpp,y_cpp,s=s,c="k", marker="x")
    ax1.plot(x_cpp,y_cpp,c='y',ls=":",label='C++')

    ax1.scatter(x_java,y_java,s=s,c="k", marker="+")
    ax1.plot(x_java,y_java,c='g',ls="-.",label='Java')

    ax1.scatter(x_python,y_python,s=s,c="k", marker="*")
    ax1.plot(x_python,y_python,c='b',ls="--",label='Python')

    fontP = FontProperties()
    fontP.set_size('small')
    plt.legend(prop=fontP, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=3)  # Move legend outside of figure in matplotlib

    plt.show()

def find_random_plot():
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.set_title("FIND operation(randomly): Comparision the performance of MongoDB between Go, C++, Java, Python")
    ax1.set_xlabel("Total number of finds")
    ax1.set_ylabel("Time consuming (s)")
    s = 20

    x_go = [10,100,1000,10000]
    y_go = [0.003767, 0.012533, 0.337167, 25.481959]

    x_cpp = [10,100,1000,10000]
    y_cpp = [0.0042596, 0.0102128, 0.325007, 31.4733]

    x_java = [10,100,1000,10000]
    y_java = [0.0059, 0.0212, 0.49729, 59.313]

    x_python = [10,100,1000,10000]
    y_python = [0.009424471855163574, 0.029928922653198242, 0.5431848287582397, 36.9468789100647]

    s = 20

    ax1.scatter(x_go,y_go,s=s,c="k", marker="o")
    ax1.plot(x_go,y_go,c='r',ls="-",label='Go')

    ax1.scatter(x_cpp,y_cpp,s=s,c="k", marker="x")
    ax1.plot(x_cpp,y_cpp,c='y',ls=":",label='C++')

    ax1.scatter(x_java,y_java,s=s,c="k", marker="+")
    ax1.plot(x_java,y_java,c='g',ls="-.",label='Java')

    ax1.scatter(x_python,y_python,s=s,c="k", marker="*")
    ax1.plot(x_python,y_python,c='b',ls="--",label='Python')

    fontP = FontProperties()
    fontP.set_size('small')
    plt.legend(prop=fontP, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=3)  # Move legend outside of figure in matplotlib

    plt.show()

def delete_plot():
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.set_title("DELETE operation: Comparision the performance of MongoDB between Go, C++, Java, Python")
    ax1.set_xlabel("Total number of deletes")
    ax1.set_ylabel("Time consuming (s)")
    s = 20

    x_go = [10,100,1000,10000]
    y_go = [0.004108, 0.011556, 0.144360, 1.851979]

    x_cpp = [10,100,1000,10000]
    y_cpp = [0.0037879, 0.009664, 0.114718, 1.75771]

    x_java = [10,100,1000,10000]
    y_java = [0.0042, 0.0152, 0.10319, 1.68709]

    x_python = [10,100,1000,10000]
    y_python = [0.009040498733520507, 0.024552202224731444, 0.2704391717910767, 3.5884851932525637]

    s = 20

    ax1.scatter(x_go,y_go,s=s,c="k", marker="o")
    ax1.plot(x_go,y_go,c='r',ls="-",label='Go')

    ax1.scatter(x_cpp,y_cpp,s=s,c="k", marker="x")
    ax1.plot(x_cpp,y_cpp,c='y',ls=":",label='C++')

    ax1.scatter(x_java,y_java,s=s,c="k", marker="+")
    ax1.plot(x_java,y_java,c='g',ls="-.",label='Java')

    ax1.scatter(x_python,y_python,s=s,c="k", marker="*")
    ax1.plot(x_python,y_python,c='b',ls="--",label='Python')

    fontP = FontProperties()
    fontP.set_size('small')
    plt.legend(prop=fontP, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=3)  # Move legend outside of figure in matplotlib
    plt.show()

if __name__ == "__main__":
    insert_plot()
    update_oneByOne_plot()
    update_random_plot()
    find_onebyOne_plot()
    find_random_plot()
    delete_plot()