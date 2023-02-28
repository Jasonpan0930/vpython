from vpython import *	#引用套件Vpython
# import vpython as vp
size = 0.05	#設定球的大小為0.05公尺

x = arrow(pos=vec(0,0,0), axis=vec(1,0,0), shaftwidth=0.02, color=color.green)
y = arrow(pos=vec(0,0,0), axis=vec(0,1,0), shaftwidth=0.02, color=color.red)
z = arrow(pos=vec(0,0,0), axis=vec(0,0,1), shaftwidth=0.02, color=color.blue)
#畫出3D直角座標沿x,y,z方向的單位向量

ball = sphere(radius=size, color=color.yellow, pos=vec(0,0,0), v=vec(1.0,0,0))
#畫球，球的半徑為size，顏色為黃色，位置在(0,0,0)，速度為(1,0,0)

dt = 0.001	#模擬的時間間隔
t = 0.0		#設定模擬的初始時間

while t<2:          #條件判斷t<2成立時執行迴圈內容
    rate(1/dt)      #設定迴圈的執行速度，每秒執行1/dt次
    t = t+dt        #計時器
    ball.pos = ball.pos + ball.v*dt  #球的每一時刻位置，每次迴圈改變ball.v *dt的位移