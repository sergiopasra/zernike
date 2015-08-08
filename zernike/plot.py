import matplotlib.pyplot as plt
import numpy as np
import math

from zernike import eval_zernike, eval_zernike_R

ns = 200
x = np.linspace(0, 2*math.pi, ns)
y = np.linspace(0.0, 1.0, ns)
tgrid, rgrid = np.meshgrid(x, y)

nf = 5
nc = 5


fig = plt.figure()
ax = fig.add_subplot(5,5,1, polar=True)
zgrid = eval_zernike(0, 0,rgrid, tgrid)
ax.pcolormesh(tgrid, rgrid, zgrid)
ax.axis('off')
ax = fig.add_subplot(5,5,6, polar=True)
zgrid = eval_zernike(1, -1,rgrid, tgrid)
ax.pcolormesh(tgrid, rgrid, zgrid)
ax.axis('off')
ax = fig.add_subplot(5,5,7, polar=True)
zgrid = eval_zernike(1, 1,rgrid, tgrid)
ax.pcolormesh(tgrid, rgrid, zgrid)
ax.axis('off')
ax = fig.add_subplot(5,5,11, polar=True)
zgrid = eval_zernike(2, -2,rgrid, tgrid)
ax.pcolormesh(tgrid, rgrid, zgrid)
ax.axis('off')
ax = fig.add_subplot(5,5,12, polar=True)
zgrid = eval_zernike(2, 0,rgrid, tgrid)
ax.pcolormesh(tgrid, rgrid, zgrid)
ax.axis('off')
ax = fig.add_subplot(5,5,13, polar=True)
zgrid = eval_zernike(2, 2,rgrid, tgrid)
ax.pcolormesh(tgrid, rgrid, zgrid)
ax.axis('off')
ax = fig.add_subplot(5,5,16, polar=True)
zgrid = eval_zernike(3, -3,rgrid, tgrid)
ax.pcolormesh(tgrid, rgrid, zgrid)
ax.axis('off')
ax = fig.add_subplot(5,5,17, polar=True)
zgrid = eval_zernike(3, -1,rgrid, tgrid)
ax.pcolormesh(tgrid, rgrid, zgrid)
ax.axis('off')
ax = fig.add_subplot(5,5,18, polar=True)
zgrid = eval_zernike(3, 1,rgrid, tgrid)
ax.pcolormesh(tgrid, rgrid, zgrid)
ax.axis('off')
ax = fig.add_subplot(5,5,19, polar=True)
zgrid = eval_zernike(3, 3,rgrid, tgrid)
ax.pcolormesh(tgrid, rgrid, zgrid)
ax.axis('off')
ax = fig.add_subplot(5,5,21, polar=True)
zgrid = eval_zernike(4, -4,rgrid, tgrid)
ax.pcolormesh(tgrid, rgrid, zgrid)
ax.axis('off')
ax = fig.add_subplot(5,5,22, polar=True)
zgrid = eval_zernike(4, -2,rgrid, tgrid)
ax.pcolormesh(tgrid, rgrid, zgrid)
ax.axis('off')
ax = fig.add_subplot(5,5,23, polar=True)
zgrid = eval_zernike(4, 0,rgrid, tgrid)
ax.pcolormesh(tgrid, rgrid, zgrid)
ax.axis('off')
ax = fig.add_subplot(5,5,24, polar=True)
zgrid = eval_zernike(4, 2,rgrid, tgrid)
ax.pcolormesh(tgrid, rgrid, zgrid)
ax.axis('off')
ax = fig.add_subplot(5,5,25, polar=True)
zgrid = eval_zernike(4, 4,rgrid, tgrid)
ax.pcolormesh(tgrid, rgrid, zgrid)
ax.axis('off')
plt.show()