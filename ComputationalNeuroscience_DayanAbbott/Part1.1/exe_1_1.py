import numpy as np
import matplotlib.pyplot as plt
from math import pow, exp, factorial
from random import random

# Poisson rate
rate = 100. # [Hz]

# Generate 1000 samples = 100 time per 10 sec
interval = 100. # [sec]
f_sampl = 1000. # to get time in [ms]
dt = 1./f_sampl

# def fpp(rT):
#     pp = np.array([(rT*i) * exp(-rT*i) for i in range(NN)])
#     return pp

# NN = 100
# plt.figure(1)
# plt.subplot(411)
# plt.plot(np.arange(0,NN), fpp(0.01)) #r = 100Hz, fs = 1000Hz 
# plt.subplot(412)
# plt.plot(np.arange(0,NN), fpp(0.1))
# plt.subplot(413)
# plt.plot(np.arange(0,NN), fpp(1.))
# plt.subplot(414)
# plt.plot(np.arange(0,NN), fpp(10.))
# plt.show()
# exit()


      
#p_tk = np.zeros(
def pk(r, T, rv):
    #p = pow(r*T, k) *  exp(-r*T) / factorial(k)
    rv = random()
    p = r * T * exp(-r*T)
    print 'rv = (', rv, ')   p[', T, '] = ', p
    raw_input()
    if p > rv:
        return 0
    else:
        return 1
    

def gen_pulses(r, interval, fs):
    N = interval*fs # number of samples
    dt = 1/fs # bucket size -> 0
    print 'dt = ', dt
    pulse = 0
    k = 1 # number of buckets without firing
    rho = np.zeros(N) # N zeros
    NS = 10
    spike_cnt_per_interval = np.zeros(NS+1) # 100 intervals
    i = 0
    rv = 0 #random() #a random for the first pulse
    while N:
        #print '[', i, '] fire? for time = k = ', k 
        pulse = pk(r, k*dt, rv)
        rho[i] = pulse
        N -= 1
        #print 'rho[', i, '] = ', pulse
        #raw_input('...')
        i += 1
        if pulse == 0: #no spike, keep waiting
            k += 1
        else: #spike arrived, reset the prob. (i.i.d)
            if k < NS:
                spike_cnt_per_interval[k] +=1 #count N of spike at k-th interval
                #rv = random()
            else:
                spike_cnt_per_interval[NS] +=1 #count N of spikes at >k-th: in the last element
                
            k = 1
            #rv = random() #new random value (for the next pulse)
            
    return rho, spike_cnt_per_interval

rho, scounts = gen_pulses(rate, interval, f_sampl)

#print
print 'scounts = ', scounts
plt.plot(np.arange(1,len(scounts)), scounts[1:])
plt.show()

#count N in each interval
# Nbucket = 15
# Ny = len(scounts)/Nbucket + 1
# isi = np.zeros(Ny)
# for x in range(Ny):
#     #print 'x = ', x
#     isi_x = sum(scounts[x*Nbucket : (x+1)*Nbucket])
#     isi[x] = isi_x
#     #print 'isi[x] = ', isi_x

# plt.plot(np.arange(0,len(isi)), isi)
# plt.show()







