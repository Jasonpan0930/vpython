from vpython import *
g = 9.8                 #重力加速度 9.8 m/s^2
size = 0.5              #球半徑 0.5 m
height = 40.0           #球初始高度 15 m
m = 1.0                 #球質量1kg
T=0.06
light=T*(7/8)
interval=0.02
balls=[]
gd1 = graph(title = "v-x plot", width=600, height=400, xtitle="x", ytitle="v")
f=gdots(color=color.blue)
position=[]
pre_position=[]
dt=0.001
t=0
tlight=0

Fg = vector(0, -m*g, 0) #重力

scene = canvas(width=600, height=600,x=0, y=0, center = vector(0,height/2,0), background=color.black) #設定畫面
floor = box(length=20, height=0.01, width=10, color=color.green)  	#畫地板


while(True):
    rate(1/dt)
    if(t//T!=(t-dt)//T):
        ball = sphere(radius = size, color=color.black, pos=vector(0, height, 0), v=vector(0,0,0)) 	#畫球
        balls.append(ball)
    for i in  range(len(balls)):
        balls[i].pos+=balls[i].v*dt
        balls[i].v+=vector(0,-g,0)*dt

    if(tlight>=light):
        tlight=0
        pre_position*=0
        for i in range(len(position)):
            pre_position.append(position[i])
        position*=0
        for i in range(len(balls)):
            balls[i].color=color.white
            position.append(balls[i].pos.y)
        for i in range(len(position)-1):
            minus=[]
            for j in range(len(pre_position)):
                minus.append(abs(pre_position[j]-position[i+1]))
            f.plot(position[i+1], min(minus)/light)
            print(position)
            print(pre_position)
            print()
            
    if(tlight>=interval):
        for i in range(len(balls)):
            balls[i].color=color.black
    
    n=len(balls)
    i=0
    while(i<n):
        if(balls[i].pos.y<1):
            balls[i].color=color.black
            del balls[i]
            n-=1
        i+=1
    t+=dt
    tlight+=dt