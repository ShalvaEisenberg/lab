import pandas as pd
import matplotlib.pyplot as plt

'''this program finds RMS for acceleration and generates a histogram for times'''

df = pd.read_csv('/home/shlava/Downloads/Output_Shalva1.csv')

# RMS calculations:

#if we want acceleration in one dimension:
acc_series_1D = pd.Series(df['acc_x_vec']) #or 'acc_y_vec'

# if we want acceleration vector formed from x,y accelerations:
x_y_acc_squared = pd.DataFrame({'acc_x_vec': df['acc_x_vec']**2, 'acc_y_vec': df['acc_y_vec']**2}) #there's probably a neater way to do this...
acc_series = pd.Series(x_y_acc_squared.sum(axis=1)**(1/2))

# set variables:
n = acc_series.size
sum_of_squares = acc_series.map(lambda x: x ** (2)).sum()
sum_divided_by_n = sum_of_squares / n
RMS = sum_divided_by_n ** (1/2)

# print solutions:
print("\nsum of squares divided by n: ", round(sum_divided_by_n, 4))
print("\nRMS: ", round(RMS, 4), "\n")

# histogram:
plt.hist(list(df['time_micros_vec']), 15)
plt.ylabel('number of trials')
plt.xlabel('time')
plt.show()