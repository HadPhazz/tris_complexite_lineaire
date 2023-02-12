from timeit import timeit
from threading import Thread
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter

def timeitFct(tri, liste, n):
    timeList = []
    for i in range(1, n+1):
        timeList.append(timeit(setup='from tris import {}; from listes import {}'.format(tri, liste),
        stmt='{}({}({}))'.format(tri, liste, i),
        number=n))
    return timeList

def plotter(tris, liste, n):
    x = np.linspace(0, n, n)
    fig, ax = plt.subplots()
    for tri in tris:
        y = timeitFct(tri, liste, n)
        w = savgol_filter(y, n-1, 2)
        ax.plot(x, w, label=tri) 
    plt.title('Complexity (for {:d} lists of 1 to {:d} elements) w/ {}'.format(n, n, liste))
    plt.xlabel('Number of elements', fontsize=14)
    plt.ylabel('Time elapsed (seconds)', fontsize=14)
    ax.legend()
    plt.grid()
    plt.show()

sortReverseWords = ["Python_sort", "Python_sorted", "tri_radix_MSD"]
sortRandomWords = ["Python_sort", "Python_sorted", "tri_radix_MSD"]
sortsRandomIntegers = ["tri_select", "tri_insert", "tri_rapide", "tri_fusion", "tri_radix_LSD", "Python_sort", "Python_sorted"]

thread = Thread(target=plotter, args=(sortReverseWords, "listeMotsReverse", 10))
#thread = Thread(target=plotter, args=(sortRandomWords, "listeMotsAleatoires", 200))
#thread = Thread(target=plotter, args=(sortsRandomIntegers, "listeEntiersAleatoires", 100))


thread.run()
