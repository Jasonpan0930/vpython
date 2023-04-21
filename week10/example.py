import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

Q1 = 1  #Q1的電荷量
Q2 = -1/2  #Q2的電荷量
k = 1   #庫倫常數
x1 = 30  #Q1的x座標
y1 = 0  #Q1的y座標
x2 = -30  #Q2的x座標
y2 = 0  #Q2的y座標

def V(x,y): #電位
    return k*(Q1)/np.sqrt((x-x1)**2+(y-y1)**2)+k*(Q2)/np.sqrt((x-x2)**2+(y-y2)**2)

#利用linspace語法產生1D-array(陣列)
x = np.linspace(-50,50,51) 
y = np.linspace(-50,50,51)

#利用meshgrid語法產生2D-array，可簡單想成x-y平面上的網格
X,Y = np.meshgrid(x,y)
Z = V(X,Y)

equal_V = ax.plot_surface(X, Y, Z, cmap=plt.cm.jet)
fig.colorbar(equal_V)  #於圖表顯示色塊數值

plt.show()