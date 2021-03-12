import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import Widget

##产生以及发送信号
data = [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1]


PN_code = [1,0,1,0,1,1,1,0,0,1,0,1,0,0,0,1,1,0,0,1,1,1,1,0,0]

def mod_2_plus(a,b):
    c=list(np.zeros_like(a))
    if len(a) == len(b):
        for i in range(len(a)):
            c[i] = np.mod((a[i]+b[i]),2)
    return c

mod_code = mod_2_plus(data,PN_code)


t = np.linspace(0,len(data),1000*len(data))
carrier_Tx = np.sin(4*np.pi*t)

data_plt = list(np.zeros_like(t))
PN_code_plt = list(np.zeros_like(t))
mod_code_plt = list(np.zeros_like(t))

for i in range(len(PN_code)):
    for j in range(1000):
        carrier_Tx[i*1000+j] = carrier_Tx[i*1000+j]*np.cos(np.pi*mod_code[i])
        data_plt[i*1000+j] = data[i]
        PN_code_plt[i*1000+j] = PN_code[i]
        mod_code_plt[i*1000+j] = mod_code[i]
plt.subplot(411)
plt.plot(data_plt)
plt.title('signal data')
plt.subplot(412)
plt.plot(PN_code_plt)
plt.title('PN code')
plt.subplot(413)
plt.plot(mod_code_plt)
plt.subplot(414)
plt.plot(t,carrier_Tx)
plt.show()

##接收及解调信号
t = np.linspace(0,len(data),1000*len(data))
carrier_Rx = np.sin(4*np.pi*t)
for i in range(len(PN_code)):
    for j in range(1000):
        carrier_Rx[i*1000+j] = carrier_Rx[i*1000+j]*np.cos(np.pi*PN_code[i])

#signal_IF = np.multiply(carrier_Rx,carrier_Tx)
signal_IF = carrier_Rx*carrier_Tx
plt.subplot(211)
plt.plot(t,carrier_Rx)
plt.title('received')
plt.subplot(212)
plt.plot(t,signal_IF)
plt.title('IF')
plt.show()




