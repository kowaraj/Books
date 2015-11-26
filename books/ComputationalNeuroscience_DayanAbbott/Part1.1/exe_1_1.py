import numpy as np
import matplotlib.pyplot as plt
from math import pow, exp, factorial
from random import random

# Poisson rate
rate = 100. # [Hz]

# Generate 1000 samples = 100 time per 10 sec
interval = 1000. # [sec]
f_sampl = 10000. # to get time in [ms]
dt = 1./f_sampl
NS = f_sampl/rate # number of different IS intervals


# Show the prob. dist for chosen params

NN = int(NS)#int(f_sampl/rate) # for the first 100 dt's, normally = [ms]
def fpp(rT):
    pp = np.array([(rT*i) * exp(-rT*i)/exp(-1) for i in range(NN)])
    return pp
plt.figure(1)
plt.plot(np.arange(0,NN), fpp(rate*dt)) #r = 100Hz, fs = 1000Hz 
plt.draw()

def pk(r, T, rv):
    #p = pow(r*T, k) *  exp(-r*T) / factorial(k)
    #rv = random()
    p_raw = r * T * exp(-r*T)
    p = p_raw/exp(-1) #max value of p
    # print 'rv = (', rv, ')   p[', T, '] = ', p
    # raw_input()
    if p > rv:
        return 1
    else:
        return 0

def gen_pulses(r, interval, fs):
    N = interval*fs # number of samples
    dt = 1/fs # bucket size -> 0
    print 'dt = ', dt
    pulse = 0
    k = 1 # number of buckets without firing
    rho = np.zeros(N) # N zeros
    spike_cnt_per_interval = np.zeros(NS+1) # 100 intervals
    i = 0
    rv = random() #a random for the first pulse
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
                rv = random()
            else:
                spike_cnt_per_interval[NS] +=1 #count N of spikes at >k-th: in the last element
                
            k = 1
            rv = random() #new random value (for the next pulse)
            
    return rho, spike_cnt_per_interval[1:]

rho, scounts = gen_pulses(rate, interval, f_sampl)

total_sum = 0
for i in range(len(scounts)):
     total_sum += scounts[i]*i
total_sum_norm = total_sum/sum(scounts)
print 'av = ', total_sum_norm

     
     
#print
print 'scounts = ', scounts
plt.figure(2)
plt.plot(np.arange(0,len(scounts)), scounts)
plt.draw()


#count N in each interval
Nbucket = 10
Ny = len(scounts)/Nbucket + 1
isi = np.zeros(Ny)
isi_total = sum(scounts)
isi_total_norm = isi_total/10.
print 'total = ', isi_total
print 'norm = ', isi_total_norm

for x in range(Ny):
    print 'x = ', x
    isi_x = sum(scounts[x*Nbucket : (x+1)*Nbucket])
    isi[x] = isi_x
    print 'isi[x] = ', isi_x

plt.figure(3)    
plt.plot(np.arange(0,len(isi)), isi/isi_total)
plt.draw()

plt.show()





