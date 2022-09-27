import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

dates = []
values_real = []
values_predicted = []
df = pd.read_csv('neural_net/predictions_relative.csv')

for i in range(len(df)):
    date = df.loc[i].iat[0]
    dates.append(date.replace("-", "/"))
    values_predicted.append(df.loc[i].iat[1])
    values_real.append(df.loc[i].iat[2])


x = [datetime.strptime(d, '%Y/%m/%d').date() for d in dates]
indx = np.arange(len(x))
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(indx - width/2, values_predicted, width, label='Prediction')
rects2 = ax.bar(indx + width/2, values_real, width, label='Real')

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.legend()
ax.grid()
fig.tight_layout()

plt.show()