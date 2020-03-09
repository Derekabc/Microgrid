import numpy as np
import math

pi = math.pi
# --------Parameter values--------------
Cf = 50e-6
Lf = 1.35e-3
rLf = .1
Lc = .35e-3
rLc = .03
wc = 31.41

rN = 1e4
F = .75
wb = 2 * pi * 60
wref = 2 * pi * 60
Vnom = 480

kp = 4
ki = 40

# mp and nq
mp1 = 9.4e-5
mp4 = mp1
mp5 = mp1
mp8 = mp1
mp9 = mp1
mp11 = mp1
mp14 = mp1
mp15 = mp1
mp18 = mp1
mp19 = mp1

mp2 = 12.5e-5
mp3 = mp2
mp6 = mp2
mp7 = mp2
mp10 = mp2
mp12 = mp2
mp13 = mp2
mp16 = mp2
mp17 = mp2
mp20 = mp2

nq1 = 1.3e-3
nq4 = nq1
nq5 = nq1
nq8 = nq1
nq9 = nq1
nq11 = nq1
nq14 = nq1
nq15 = nq1
nq18 = nq1
nq19 = nq1

nq2 = 1.5e-3
nq3 = nq2
nq6 = nq2
nq7 = nq2
nq10 = nq2
nq12 = nq2
nq13 = nq2
nq16 = nq2
nq17 = nq2
nq20 = nq2

# Kpv and Kiv
Kpv1 = 0.1
Kpv4 = Kpv1
Kpv5 = Kpv1
Kpv8 = Kpv1
Kpv9 = Kpv1
Kpv11 = Kpv1
Kpv14 = Kpv1
Kpv15 = Kpv1
Kpv18 = Kpv1
Kpv19 = Kpv1

Kpv2 = 0.05
Kpv3 = Kpv2
Kpv6 = Kpv2
Kpv7 = Kpv2
Kpv10 = Kpv2
Kpv12 = Kpv2
Kpv13 = Kpv2
Kpv16 = Kpv2
Kpv17 = Kpv2
Kpv20 = Kpv2

Kiv1 = 420
Kiv4 = Kiv1
Kiv5 = Kiv1
Kiv8 = Kiv1
Kiv9 = Kiv1
Kiv11 = Kiv1
Kiv14 = Kiv1
Kiv15 = Kiv1
Kiv18 = Kiv1
Kiv19 = Kiv1

Kiv2 = 390
Kiv3 = Kiv2
Kiv6 = Kiv2
Kiv7 = Kiv2
Kiv10 = Kiv2
Kiv12 = Kiv2
Kiv13 = Kiv2
Kiv16 = Kiv2
Kiv17 = Kiv2
Kiv20 = Kiv2

# kpc and kic
Kpc1 = 15
Kpc4 = Kpc1
Kpc5 = Kpc1
Kpc8 = Kpc1
Kpc9 = Kpc1
Kpc11 = Kpc1
Kpc14 = Kpc1
Kpc15 = Kpc1
Kpc18 = Kpc1
Kpc19 = Kpc1

Kpc2 = 10.5
Kpc3 = Kpc2
Kpc6 = Kpc2
Kpc7 = Kpc2
Kpc10 = Kpc2
Kpc12 = Kpc2
Kpc13 = Kpc2
Kpc16 = Kpc2
Kpc17 = Kpc2
Kpc20 = Kpc2

Kic1 = 20e3
Kic4 = Kic1
Kic5 = Kic1
Kic8 = Kic1
Kic9 = Kic1
Kic11 = Kic1
Kic14 = Kic1
Kic15 = Kic1
Kic18 = Kic1
Kic19 = Kic1

Kic2 = 16e3
Kic3 = Kic2
Kic6 = Kic2
Kic7 = Kic2
Kic10 = Kic2
Kic12 = Kic2
Kic13 = Kic2
Kic16 = Kic2
Kic17 = Kic2
Kic20 = Kic2

# ----Network Data-------
rline1 = .23
Lline1 = .1 / (2 * pi * 60)
rline2 = .35
Lline2 = .58 / (2 * pi * 60)
rline3 = .23
Lline3 = .1 / (2 * pi * 60)
rline4 = .23
Lline4 = .1 / (2 * pi * 60)
rline5 = .35
Lline5 = .58 / (2 * pi * 60)
rline6 = .23
Lline6 = .1 / (2 * pi * 60)
rline8 = .23
Lline8 = .1 / (2 * pi * 60)
rline9 = .35
Lline9 = .58 / (2 * pi * 60)
rline10 = .23
Lline10 = .1 / (2 * pi * 60)
rline7 = .23
Lline7 = .1 / (2 * pi * 60)
rline11 = .35
Lline11 = .58 / (2 * pi * 60)
rline12 = .23
Lline12 = .1 / (2 * pi * 60)
rline13 = .23
Lline13 = .1 / (2 * pi * 60)
rline14 = .35
Lline14 = .58 / (2 * pi * 60)
rline15 = .23
Lline15 = .1 / (2 * pi * 60)
rline16 = .23
Lline16 = .1 / (2 * pi * 60)
rline17 = .35
Lline17 = .58 / (2 * pi * 60)
rline18 = .23
Lline18 = .1 / (2 * pi * 60)
rline19 = .23
Lline19 = .1 / (2 * pi * 60)
rline20 = .35
Lline20 = .58 / (2 * pi * 60)

QF = 0.5
Rload1 = 2
Lload1 = QF * 2 / (2 * pi * 60)
Rload2 = 2
Lload2 = QF * 1 / (2 * pi * 60)
Rload3 = 2
Lload3 = QF * 2 / (2 * pi * 60)
Rload4 = 2
Lload4 = QF * 1 / (2 * pi * 60)
Rload5 = 2
Lload5 = QF * 2 / (2 * pi * 60)
Rload6 = 2
Lload6 = QF * 1 / (2 * pi * 60)
Rload7 = 2
Lload7 = QF * 2 / (2 * pi * 60)
Rload8 = 2
Lload8 = QF * 1 / (2 * pi * 60)
Rload9 = 2
Lload9 = QF * 2 / (2 * pi * 60)
Rload10 = 2
Lload10 = QF * 1 / (2 * pi * 60)

# ------------Controller Parameters------------------------

a_ctrl = 400
# Physical Graph
AP = 40 * np.array([[0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
                    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
                    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 3
                    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
                    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 6
                    [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # 7
                    [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 8
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 9
                    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # 10
                    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # 11
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 12
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],  # 13
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],  # 14
                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],  # 15
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],  # 16
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],  # 17
                    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],  # 18
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],  # 19
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]])  # 20

# Pinning gain to the reference frequency
G = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# matrix for bus and load connection
BUS_LOAD = [1, 0, 1, 0, 1,
            0, 1, 0, 1, 0,
            1, 0, 1, 0, 1,
            0, 1, 0, 1, 0]

# matrix for bus connection
BUSES = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
                  [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
                  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3
                  [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
                  [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
                  [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
                  [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 7
                  [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 8
                  [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 9
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 10
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 11
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 12
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # 13
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],  # 14
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],  # 15
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],  # 16
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],  # 17
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],  # 18
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],  # 19
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])  # 20

DER_dic = {
    0: [Rload1, Lload1, Kpv1, Kiv1, Kpc1, Kic1, mp1, nq1],
    1: [0, 0, Kpv2, Kiv2, Kpc2, Kic2, mp2, nq2],
    2: [Rload2, Lload2, Kpv3, Kiv3, Kpc3, Kic3, mp3, nq3],
    3: [0, 0, Kpv4, Kiv4, Kpc4, Kic4, mp4, nq4],
    4: [Rload3, Lload3, Kpv5, Kiv5, Kpc5, Kic5, mp5, nq5],
    5: [0, 0, Kpv6, Kiv6, Kpc6, Kic6, mp6, nq6],
    6: [Rload4, Lload4, Kpv7, Kiv7, Kpc7, Kic7, mp7, nq7],
    7: [0, 0, Kpv8, Kiv8, Kpc8, Kic8, mp8, nq8],
    8: [Rload5, Lload5, Kpv9, Kiv9, Kpc9, Kic9, mp9, nq9],
    9: [0, 0, Kpv10, Kiv10, Kpc10, Kic10, mp10, nq10],
    10: [Rload6, Lload6, Kpv11, Kiv11, Kpc11, Kic11, mp11, nq11],
    11: [0, 0, Kpv12, Kiv12, Kpc12, Kic12, mp12, nq12],
    12: [Rload7, Lload7, Kpv13, Kiv13, Kpc13, Kic13, mp13, nq13],
    13: [0, 0, Kpv14, Kiv14, Kpc14, Kic14, mp14, nq14],
    14: [Rload8, Lload8, Kpv15, Kiv15, Kpc15, Kic15, mp15, nq15],
    15: [0, 0, Kpv16, Kiv16, Kpc16, Kic16, mp16, nq16],
    16: [Rload9, Lload9, Kpv17, Kiv17, Kpc17, Kic17, mp17, nq17],
    17: [0, 0, Kpv18, Kiv18, Kpc18, Kic18, mp18, nq18],
    18: [Rload10, Lload10, Kpv19, Kiv19, Kpc19, Kic19, mp19, nq19],
    19: [0, 0, Kpv20, Kiv20, Kpc20, Kic20, mp20, nq20],
}

rline = [rline1, rline2, rline3, rline4, rline5, rline6, rline7, rline8, rline9, rline10, rline11, rline12, rline13,
         rline14, rline15, rline16, rline17, rline18, rline19, rline20]
Lline = [Lline1, Lline2, Lline3, Lline4, Lline5, Lline6, Lline7, Lline8, Lline9, Lline10, Lline11, Lline12, Lline13,
         Lline14, Lline15, Lline16, Lline17, Lline18, Lline19, Lline20]

# add 0, to meet the difference between MATLAB and python, shape=(361,)
x0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      2 * pi * 60, 2 * pi * 60, 2 * pi * 60, 2 * pi * 60, 2 * pi * 60, 2 * pi * 60, 2 * pi * 60, 2 * pi * 60,
      2 * pi * 60, 2 * pi * 60, 2 * pi * 60, 2 * pi * 60, 2 * pi * 60, 2 * pi * 60, 2 * pi * 60, 2 * pi * 60,
      2 * pi * 60, 2 * pi * 60, 2 * pi * 60, 2 * pi * 60,
      Vnom, Vnom, Vnom, Vnom, Vnom, Vnom, Vnom, Vnom, Vnom, Vnom, Vnom, Vnom, Vnom, Vnom, Vnom, Vnom, Vnom, Vnom, Vnom,
      Vnom]

# add 0, to meet the difference between MATLAB and python, shape=(361,)
x_critic = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, Vnom, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            2 * pi * 60, 2 * pi * 60, 2 * pi * 60, 2 * pi * 60, 2 * pi * 60, 2 * pi * 60, 2 * pi * 60, 2 * pi * 60,
            2 * pi * 60, 2 * pi * 60, 2 * pi * 60, 2 * pi * 60, 2 * pi * 60, 2 * pi * 60, 2 * pi * 60, 2 * pi * 60,
            2 * pi * 60, 2 * pi * 60, 2 * pi * 60, 2 * pi * 60,
            Vnom, Vnom, Vnom, Vnom, Vnom, Vnom, Vnom, Vnom, Vnom, Vnom, Vnom, Vnom, Vnom, Vnom, Vnom, Vnom, Vnom, Vnom,
            Vnom,
            Vnom, 0]

mp = [mp1, mp2, mp3, mp4, mp5, mp6, mp7, mp8, mp9, mp10, mp11, mp12, mp13, mp14, mp15, mp16, mp17, mp18, mp19, mp20]
nq = [nq1, nq2, nq3, nq4, nq5, nq6, nq7, nq8, nq9, nq10, nq11, nq12, nq13, nq14, nq15, nq16, nq17, nq18, nq19, nq20]