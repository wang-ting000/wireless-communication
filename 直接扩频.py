




# -*- encoding: utf-8 -*-
"""
@File   : 直接扩频.py
@Time   : 2021/5/15 16:19
@Author : Wang
"""
# -*- coding: utf-8 -*-
'''
根据P124，图4-1进行的仿真
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import Widget
from scipy import signal
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

##产生以及发送信号
data = list(np.zeros(12))
data=np.concatenate((data,np.ones_like(data)))
data = list(data)##original signal
axis=np.arange(len(data)+1)

PN_code = [1,0,1,0,1,1,1,0,0,1,0,1,0,0,0,1,1,0,0,1,1,1,1,0]##Psudo Code


def mod_2_plus(a,b):
    '''

    :param a: input 1
    :param b: input 2
    :return: (a+b)mod2
    '''
    c=list(np.zeros_like(a))
    if len(a) == len(b):
        for i in range(len(a)):
            c[i] = np.mod((a[i]+b[i]),2)
    else:
        print('two inputs must be the same length')
    return c

mod_code = mod_2_plus(data,PN_code)##复合码

fs=1000
T0=len(data)
dt=1/fs
N=int(T0/dt)
t=np.linspace(0,T0,N)
f=t/T0*fs
#t=np.linspace(0,len(data),1000*len(data))

f0=15/4
fr=f0 ##因为滤波器不理想，导致混频时候得到的低频跳变点不明显，所以直接得到一个频率
carrier_Tx = np.cos(2*np.pi*f0*t) ##载波

data_plt = data.copy()##这一步对于调制没有影响，只是为了画图更加直观，让每一个step展示出对应的code
data_plt.insert(0,0)
PN_code_plt = PN_code.copy()
PN_code_plt.insert(0,0)
mod_code_plt = mod_code.copy()
mod_code_plt.insert(0,0)

for i in range(len(PN_code)):
    for j in range(1000):
        carrier_Tx[i*1000+j] = carrier_Tx[i*1000+j]*(1-2*mod_code[i])
        ##BPSK

##画出信息数据、扩频码xu列、复合码序列、发射信号
plt.figure()
plt.subplot(411)
plt.step(axis,data_plt)
plt.title('signal data')
plt.subplot(412)
plt.step(axis,PN_code_plt)
plt.title('PN code')
plt.subplot(413)
plt.step(axis,mod_code_plt)
plt.title('复合码')
plt.subplot(414)
plt.plot(t,carrier_Tx)
plt.title('发射信号')
plt.savefig('code.svg')

##接收及解调信号

carrier_Rx = np.cos(2*np.pi*fr*t)##收信本振，需要经过扩频码发生器调相
for i in range(len(PN_code)):##调相
    for j in range(1000):
        carrier_Rx[i*1000+j] = carrier_Rx[i*1000+j]*(1-2*PN_code[i])

#signal_IF = np.multiply(carrier_Rx,carrier_Tx)
signal_IF = carrier_Rx*carrier_Tx##中频信号

'''两种滤波方法'''
'''sos = signal.butter(128, f0-fr, 'lp', fs=1000, output='sos')
signal_IF = signal.sosfiltfilt(sos, signal_IF)'''
'''y = np.fft.fft(signal_IF)
end = np.asarray(np.where(f<=f0-fr))
end = end[0,-1]
for i in range(len(y)):
    if i>end:
        y[i]=0
signal_IF = np.fft.ifft(y)
plt.figure()
plt.subplot(211)
plt.plot(f[0:500],abs(y[0:500]))
plt.subplot(212)
plt.plot(t,(signal_IF))'''
plt.figure()
plt.subplot(211)
plt.plot(t,carrier_Rx)
plt.title('收信本振')
plt.subplot(212)
theo=np.sin((f0-fr)*2*np.pi*t)
for i in range(len(t)):
    if t[i]<=11:
        theo[i]=theo[i]
    else:
        theo[i] = theo[i]*(-1)

the = np.cos(2*np.pi*f0*t)*np.cos(2*np.pi*fr*t)
for i in range(len(PN_code)):##调相
    for j in range(1000):
        the[i*1000+j] = the[i*1000+j]*(1-2*data[i])
plt.plot(t,signal_IF)
plt.title('中频信号')
plt.savefig('IF.svg')
plt.show()
##采样判决
re = np.zeros_like(data)
for i in range(len(data)):
    if signal_IF[i*1000+500]>=0:
        re[i] = 0   #判决，1对应0，-1对应1
    else:
        re[i] = 1

res = list(re.copy())
res.insert(0,0)
plt.scatter(axis,data_plt,marker='o',label = '原始数据')
plt.scatter(axis,res,marker='^',label = '判决的数据')
plt.legend()
plt.savefig('res.svg')
plt.show()



