## [![](https://img.shields.io/badge/-%E5%AF%B9%E8%B7%AF%E5%BE%84%E6%8D%9F%E8%80%97%E6%A8%A1%E5%9E%8B%E7%9A%84%E4%BB%BF%E7%9C%9F-lightgrey)](https://github.com/wang-ting000/wireless-communication/blob/main/pathloss.m)

## [![](https://img.shields.io/badge/-%E7%9B%B4%E6%8E%A5%E6%89%A9%E9%A2%91%E9%80%9A%E4%BF%A1%E7%B3%BB%E7%BB%9F%E7%9A%84%E4%BB%BF%E7%9C%9F-lightgrey)](https://github.com/wang-ting000/wireless-communication/blob/main/%E7%9B%B4%E6%8E%A5%E6%89%A9%E9%A2%91.py)

#本项目收集了无线通信基础的书本资源和本人笔记以及习题记录

# 一些关于通信方面的问题和回答

1. 什么是`等效基带信号`？其意义是？

    -  就是频带信号的复包络平移到了原点处
    -  包含了除f<sub>c</sub>处的所有信息
    - 带通信号通过带通系统，可以等效为等效基带信号通过等效低通系统。
    -  解析信号：只有正频率部分
            z<sub>x</sub>(t)=x(t)+j\overset{^}{x}
2. 星座图中点到原点的距离表示的是振幅
3. `IQ信号`：cos(ωt)+jsin(ωt);其解调和调制原理同傅里叶级数展开以及逆变换类似
4. 混叠问题的原因：
    · 采样频率过低
    · 恢复滤波器的低通特性不理想
5. `过采样`：意味着编码速率提高，会降低信道利用率
6. 以采样频率f<sub>s</sub>对频率为*kf<sub>s</sub>±f*的**余弦信号**进行采样，采样结果无法区分;

   以采样频率f<sub>s</sub>对频率为*kf<sub>s</sub>+f*的**复指数信号**进行采样，采样结果无法区分;
   
7. 模拟滤波器中利用电阻、电容、电感等对模拟信号进行处理，存在电压漂移、温度漂移和噪声等问题，而数字滤波器利用软件或逻辑对数字信号进行运算处理，不存在这方面的问题，有很高的稳定度和精度
8. 但是高频信号一般采用模拟滤波器因为采样频率高ADC处理不过来
9. 
