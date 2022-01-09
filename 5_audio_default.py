import wave
import sys
import numpy as np
import wavio
import matplotlib.pylab as plt

# Parameters
rate = 44100        # samples per second
T = 10           # sample duration (seconds)
f = 440

# Compute waveform samples
t = np.linspace(0, T, T*rate, endpoint=False)
x = np.sin(2*np.pi * f * t)
# Write the samples to a file
wavio.write("A440.wav", x, rate, sampwidth=3)

# plot lines
plt.figure()
plt.plot(t, x, 'b', label="wave", linewidth=0.8)
plt.xlabel("seconds")
plt.ylabel("wave")
plt.legend()
plt.show()
