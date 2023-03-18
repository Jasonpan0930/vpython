from vpython import *	#引用套件Vpython

size = 0.05	#設定球的大小為0.05公尺

x = arrow(pos=vec(0,0,0), axis=vec(1,0,0), shaftwidth=0.02, color=color.green)
y = arrow(pos=vec(0,0,0), axis=vec(0,1,0), shaftwidth=0.02, color=color.red)
z = arrow(pos=vec(0,0,0), axis=vec(0,0,1), shaftwidth=0.02, color=color.blue)
#畫出3D直角座標沿x,y,z方向的單位向量


vy=vec(-0.4, 1, -0.4)
py=vec(0,-1,1)
vg=vec(-1.5,-0.5,-0.7)
pg=vec(1,1,1)

yball = sphere(radius = size, pos=py, color=color.yellow)
gball = sphere(radius = size, pos=pg, color=color.green)

dt=0.001
t=0.0

while(t<=1.5):
    rate(1/dt)
    t+=dt
    yball.pos+=vy*dt
    gball.pos+=vg*dt
    
print(yball.pos, gball.pos)