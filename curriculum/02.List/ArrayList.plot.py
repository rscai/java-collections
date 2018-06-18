# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

def plotBenchmark(x,y,title):
    plt.plot(x,y)
    plt.xlabel("(n)")
    plt.ylabel("ops/s")
    plt.title(title)
    return plt

seq = [10000,100000,1000000,10000000]
add_scores = [133096.896,93916.433,15222.869,543.267]

add_plot = plotBenchmark(seq,add_scores,"add(int index, E element) Benchmark")


