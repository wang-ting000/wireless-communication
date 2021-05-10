# -*- encoding: utf-8 -*-
"""
@File   : 注水法.py
@Time   : 2021/5/10 16:19
@Author : Wang
"""
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.ion()


def waterfilling(noise, P):
    N = len(noise)  # 信道数目
    axis = range(N)
    name = []
    for i in range(1, N + 1):
        name += [r'$\sigma_%s$' % (i)]
    #plt.figure(figsize=(8, 6))
    fig, ax = plt.subplots()

    plt.bar(axis, noise, width=1, color='rgb', tick_label=name)
    plt.pause(1)
    plt.cla()
    ori = sorted(noise)
    noise = sorted(noise)
    plt.bar(axis, noise, width=1, color='rgb', tick_label=name)
    plt.text(
        1,
        1.8,
        '给信道噪声功率排序',
        fontsize=15,
        verticalalignment="top",
        horizontalalignment="left")
    plt.pause(2)
    while len(noise) > 0:
        lam_rec = noise[-1]  # 1/lambda
        if lam_rec * len(noise) - sum(noise) <= P:
            lam_rec += (P - (lam_rec * len(noise) - sum(noise))) / len(noise)
            break
        else:
            noise.pop(-1)

    plt.title(r'$1/\lambda$'"=%s注水算法仿真" % (lam_rec))
    # plt.pause(1.2)
    axis = range(len(noise))  # 使用到的信道的数量
    axis1 = range(len(noise), N)  # 未使用的信道
    plt.bar(axis1, ori[len(noise):N], width=1, color='#1C201D')
    plt.text(
        1,
        1.2,
        '去掉不使用的信道',
        fontsize=15,
        verticalalignment="top",
        horizontalalignment="left")
    plt.pause(2)
    plt.bar(axis,
              np.ones_like(axis) * lam_rec - noise,
              bottom=noise,
              width=1,
              color='#22D352')

    plt.text(
        1,
        0.6,
        '按顺序注水',
        fontsize=15,
        verticalalignment="top",
        horizontalalignment="left")
    plt.pause(3)
    plt.xlabel('第i个信道')
    plt.ylabel('power/sigma')
    plt.show()


waterfilling([0.1, 0.4, 0.2, 0.3, 0.9, 1.8, 0.21], 1.2)
