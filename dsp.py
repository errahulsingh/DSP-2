import matplotlib.pyplot as plt
import numpy as np
import scipy as sc

t = np.arange(700)
n = np.zeros((700,), dtype=complex)
n[50:650] = np.exp(1j*np.random.uniform(0, 2*np.pi, (600,)))
s = np.fft.fft(n)

plt.subplot(321)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.plot(t, n)

plt.subplot(322)
plt.xlabel('frequency')
plt.ylabel('amplitude')
plt.plot(t, s.real, 'b-', t, s.imag, 'r--')

s1 = np.copy(s)
s1[0:200]=0
plt.subplot(324)
plt.xlabel('frequency')
plt.ylabel('amplitude')
plt.plot(t, s1.real, 'b-', t, s1.imag, 'r--')

n1=np.fft.ifft(s1)
plt.subplot(323)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.plot(t, n1)

s2 = np.copy(s)
s2[500:]=0
plt.subplot(326)
plt.xlabel('frequency')
plt.ylabel('amplitude')
plt.plot(t, s2.real, 'b-', t, s2.imag, 'r--')

n2=np.fft.ifft(s2)
plt.subplot(325)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.plot(t, n2)

plt.show()