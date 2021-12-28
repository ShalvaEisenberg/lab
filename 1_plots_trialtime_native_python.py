import pandas as pd
import matplotlib.pyplot as plt

'''this program plots data from a given csv file'''

data_file = open('/home/shlava/Downloads/Output_Shalva1.csv', newline='')

def line_to_list(line):
    ''' converts a csv line (string) to a list of items '''
    line = line.rstrip('\n')
    return [s for s in line.split(',')]

def restart_file():
    ''' callobrates rile reading to begin at the first row after the header '''
    data_file.seek(0)
    data_file.readline()

def get_info(header_i):
    ''' returns a list of the data belonging to the sent column header '''
    # reset to first line (header) and read it
    restart_file()
    col_data = []
    # itirate through each row of data to collect the relevant cell in each row
    for line in data_file:
        line_list = line_to_list(line)
        col_data.append(float(line_list[header_i]))
    # return list of all data under sent header 
    return col_data

def get_times():
    ''' returns a list of timestamps from each trial '''
    # reset to first line (header) and read it
    restart_file()
    times_formatted = []
    # itirate through each row of data
    for line in data_file:
        line_list = line_to_list(line)
        # the time up till now is the last element in the list of times (each time value is cumulative):
        sum_times = times_formatted[-1] if len(times_formatted) > 0 else 0
        # save the sum of (times till now + current time) into the list
        times_formatted.append(sum_times + float(line_list[-1]))
    return times_formatted

def get_trial_time(id):
    ''' returns the time until given id '''
    restart_file()
    time = 0
    for line in data_file:
        line_list = line_to_list(line)
        time += float(line_list[-1])
        if id == int(line_list[0]):
            return time



################


# receive headers as list
line_1 = data_file.readline()
headers = line_to_list(line_1)

# receive x_axis data
x_axis_header = "time"
x_axis_data = get_times()

# if we want some other column, instead of time, for the x_axis:
# x_axis_header = "id" #change to whatever column you want
# x_header_i = headers.index(x_axis_header)
# x_axis_data = get_info(x_header_i, True)

# receive y1_axis data
y1_axis_header = "vel_y_vec" #change to whatever column you want
y1_header_i = headers.index(y1_axis_header)
y1_axis_data = get_info(y1_header_i)

# receive y2_axis data
y2_axis_header = "acc_y_vec" #change to whatever column you want
y2_header_i = headers.index(y2_axis_header)
y2_axis_data = get_info(y2_header_i)



# print trial time of given trial id
print(get_trial_time(2500))

# plot lines 
plt.figure()
plt.plot(x_axis_data, y1_axis_data, 'b', label=y1_axis_header, linewidth=0.8)
plt.plot(x_axis_data, y2_axis_data, 'y', label=y2_axis_header, linewidth=0.5)
plt.xlabel(x_axis_header)
plt.ylabel(y1_axis_header)
# plt.title('Graph of ' + y1_axis_header + ' as a function of ' + x_axis_header)
plt.legend()
plt.show()