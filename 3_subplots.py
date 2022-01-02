import pandas as pd
import matplotlib.pyplot as plt

'''this program subplots data from a given csv file onto one plot'''

df = pd.read_csv('/home/shlava/Downloads/Output_Shalva1.csv')

# calculate cumulative sum of time 
df['cumsum_time'] = df['time_micros_vec'].cumsum()

# receive x_axis data - time
x_axis_header = "time"
x_axis_data = list(df["cumsum_time"])

# receive y1_axis data
y1_axis_header = "vel_y_vec" #change to whatever column you want
y1_axis_data = list(df[y1_axis_header])

# receive y2_axis data
y2_axis_header = "acc_y_vec" #change to whatever column you want
y2_axis_data = list(df[y2_axis_header])


# plot lines:

plt.figure()

# first subplot
plt.subplot(2,1,1)
plt.plot(x_axis_data, y1_axis_data, 'b', label=y1_axis_header, linewidth=0.8)
plt.ylabel(y1_axis_header)
plt.legend()

# second subplot
plt.subplot(2,1,2)
plt.plot(x_axis_data, y2_axis_data, 'y', label=y2_axis_header, linewidth=0.5)
plt.xlabel(x_axis_header)
plt.ylabel(y2_axis_header)
plt.legend()

plt.show()