from vpython import *
g = 9.8                 #重力加速度 9.8 m/s^2
size = 0.05             #球半徑 0.05 m            
L0 = 1                   #彈簧原長 0.5m
delta_L=0.1
delta_x=0.1             
k = 100000              #彈簧力常數 100000 N/m
m = 0.1                 #球質量 0.1 kg
theta = 10 * pi/180     #初始擺角
Fg = m*vector(0,-g,0)   #球所受重力向量
n=int(input("How many balls will be in the Pendulum wave?"))                 #複擺中單擺數量

def SpringForce(r,L):
    return -k*(mag(r)-L)*norm(r)



scene = canvas(width=600, height=600, center=vector(0,(L0+n*delta_L)*-0.5, 0), background=vector(0.6,0.8,0.8))#設定畫面
ceiling = box(pos=vector(0,0,-delta_x*n/2),length=0.4, height=0.05, width=0.4+n*delta_x,color=vector(0.68,0.68,0.68))#畫天花板

balls=[]
rods=[]
for i in range(n):
    L=L0+delta_L*i
    ball = sphere(pos=vector(L*sin(theta), -L*cos(theta), -delta_x*i), v=vector(0,0,0), a=vector(0,0,0), radius = size,  color=color.yellow, make_trail = False)
    rod = cylinder(pos=vector(0,0,-delta_x*i), radius=size/10, color=color.white)#畫繩子    
    balls.append(ball)
    rods.append(rod)


dt = 0.001    #時間間隔
t = 0.0       #初始時間
t_right = 0   #右端點時間 
X=0.2

while True:
    rate(50/dt)

    for i in range(n):
        L=L0+i*delta_L
        rods[i].axis = balls[i].pos - rods[i].pos
        balls[i].a = (Fg + SpringForce(rods[i].axis,L))/m    #牛頓第二定律：加速度＝合力/質量
        balls[i].v += balls[i].a*dt    
        balls[i].pos += balls[i].v*dt


        
    t += dt