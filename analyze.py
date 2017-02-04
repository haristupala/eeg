from pylab import *
from numpy import *
import cPickle
from scipy import fftpack

N = 2
t = array(cPickle.load(open('data.pick')))
sp = fftpack.fft(t[:,N])
freq = np.fft.fftfreq(t[:,N].shape[-1])
sp = sp.real[len(sp.real)/2:]
freq = freq[len(freq)/2:]
plot(1/freq/170, sp.real) #, freq, sp.imag)
show()
'''
subplot(3,2,1)
plot(m[:,1])
subplot(3,2,2)
plot(m[:,2])
subplot(3,2,3)
plot(m[:,3])
subplot(3,2,4)
plot(m[:,4])
subplot(3,2,5)
plot(m[:,4])
subplot(3,2,6)
plot(m[:,0])

show()
'''
