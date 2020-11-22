import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import openpyxl
from openpyxl import load_workbook

from openpyxl.chart import BarChart, Reference
from openpyxl.utils.dataframe import dataframe_to_rows


os.chdir("C:/Users/leeseungkyu/PycharmProjects/localhostwebserver")

xlsx = pd.read_excel('C:/Users/leeseungkyu/PycharmProjects/localhostwebserver/test.xlsx')



wb = openpyxl.load_workbook('test.xlsx')


#print(xlsx.head())
#print()
#print(xlsx.tail())
#print()
#print(xlsx.shape)

xnp = np.array(xlsx)
np_t = xnp[:,4]
np_log = xnp[:,3]
print(xlsx)
plt.figure(figsize=(30,10))
plt.plot(np_t, np_log)
plt.show()
