import numpy as np
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import pandas


df = pandas.read_csv("data.csv")
plt.subplot(1, 2, 1)
plt.plot( df["Time"],df["RPM"], label = "PRM")
plt.plot( df["Time"],df["Tq"], label = "Tq")
plt.legend()



df=(df-df.mean())/df.std()
plt.subplot(1, 2, 2)
plt.plot( df["Time"],df["RPM"], label = "PRM")
plt.plot( df["Time"],df["Tq"], label = "Tq")
plt.legend()
plt.show()