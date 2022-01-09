import numpy as np
import wavio
import matplotlib.pylab as plt

# Parameters
rate = 44100        # samples per second
T = 0           # sample duration (seconds)
f = 0

# receive time from user
while f == 0:
    try:
        f = float(input("enter the sound frequency you'd like to save: "))       # sound frequency (Hz)
    except:
        f = 0

# receive time from user
while T == 0:
    try:
        T = int(input("enter the number of seconds you'd like for this sound: "))
    except:
        T = 0

# Compute waveform samples
t = np.linspace(0, T, 1000, endpoint=False)
x = np.sin(2*np.pi * f * t)
# Write the samples to a file
wavio.write("A" + str(int(f)) + ".wav", x, rate, sampwidth=3)

# plot lines
plt.figure()
plt.plot(t, x, 'b', label="wave", linewidth=0.8)
plt.xlabel("seconds")
plt.ylabel("wave")
plt.legend()
plt.show()
