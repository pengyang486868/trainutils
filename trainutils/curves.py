import numpy as np
from trainutils.utils import math


def curve1():
    basex = np.arange(0, 2 * 3.14, 0.2)
    basey = np.sin(basex)

    # plt.plot(basex,basey)
    normalfront = 0.8 * np.tile(basey, 3)
    normalfront = normalfront + 0.6 * np.random.rand(len(normalfront))

    faultperiod = np.tile(basey, 2)
    faultperiod = 0.3 * faultperiod + 1.6 * np.random.rand(len(faultperiod)) + np.linspace(0, 2, len(faultperiod))

    repairperoid = np.ones(len(basex)) * faultperiod[-1] / 3
    repairperoid = repairperoid + 0.6 * np.random.rand(len(repairperoid))

    normalback = np.tile(basey, 2)
    normalback = normalback + 0.6 * np.random.rand(len(normalback))
    normalback = 0.6 * normalback[int(len(basex) / 3):]

    finalcurve = np.hstack((normalfront, faultperiod, repairperoid, normalback))
    return finalcurve
    # plt.plot(finalcurve)
    # plt.show()


def curve2():
    x = np.linspace(0, 1, 24)
    y = 3 * x ** 2 - 2 * x ** 3
    return math.add_one(y)
    # plt.plot(x, y)
    # plt.plot(x, x)
    # plt.show()


def rise_series(n, wave=1, rise=1):
    randpart = np.random.rand(n) * wave
    risepart = np.linspace(0, rise, n)
    return randpart + risepart


def hat_series(n, wave=1, top=1):
    randpart = np.random.rand(n) * wave
    x = np.linspace(0, 3.14, n)
    hatpart = np.sin(x) * top
    return randpart + hatpart


def bool_series(n, p=0.2):
    randpart = np.random.rand(n)
    return np.array(list(map(lambda x: 1 if x > p else 0, randpart)))
