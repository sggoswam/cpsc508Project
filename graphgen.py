import sys 
# Note: I only need this on my system because mpl has a weird path issue
sys.path.append("/usr/local/lib/python3.7/site-packages")
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# Wrapper to create a new figure and axis
def plot_figure(title, xlabel, ylabel, xticks=None):
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return (ax, fig)

# Wrapper to create a bar chart
def create_bar_chart(ax, fig, xdata, ydata, xticks=None):
    ax.bar(xdata, ydata, tick_label=xticks, log=True)

ydata_dram = [183897.16, 187320.044, 181281.336]
ydata_pmem = [185642.472, 189318.422, 185432.812]
xticks=["4K", "2M", "1G"]

ax_redis, fig_redis = plot_figure("GETs/second - PMEM vs DRAM", "Page Size", "Throughput (GETs/sec)")

ax_redis.plot(xticks, ydata_dram, label="DRAM")
ax_redis.plot(xticks, ydata_pmem, label="PMEM")
ax_redis.legend()

# PMEM 1G Accesses FIO 
ax_bar_fio_pmem_1g, fig_bar_fio_pmem_1g = plot_figure("PMEM dTLB Misses (1GB Sequential Read - FIO)", "Page Size", "dTLB Misses")
ydata_fio_1gp = [8.46E+08, 4.17E+06, 1.73E+06]
create_bar_chart(ax_bar_fio_pmem_1g, fig_bar_fio_pmem_1g, [1, 2, 3], ydata_fio_1gp, xticks)

# TODO: DRAM 1G Accesses FIO

# TODO: PMEM 4K Read FIO 

# TODO: DRAM 4K Read FIO 

plt.show()