from vpython import *
g = 9.8                 #重力加速度 9.8 m/s^2
size = 0.5              #球半徑 0.5 m
m = 1.0                 #球質量1kg

Fg = vector(0, -m*g, 0) #重力

scene = canvas(width=600, height=600,x=0, y=0, center = vector(0,0,0), background=vector(0.6,0.8,0.8)) #設定畫面
floor = box(length=20, height=0.01, width=10, color=color.green)  	#畫地板
blue_ball = sphere(radius = size, color=color.blue, make_trail= True, trail_type="points", interval=100) 	#畫球
green_ball = sphere(radius = size, color=color.green, make_trail= True, trail_type="points", interval=100) 	#畫球
blue_ball.pos = vector(0, 0, 0)    #球初始位置
blue_ball.v = 20*vector(cos(pi/6), sin(pi/6), 0)           #球初速 
green_ball.pos = vector(0, 0, 0)    #球初始位置
green_ball.v = 20*vector( cos(pi/3),sin(pi/3), 0)           #球初速 



dt = 0.001	#時間間隔 0.001 秒
t = 0.0		#模擬初始時間為0秒

blue=0

while green_ball.pos.y >= 0:    #模擬直到球落地 即y=0
    rate(1/dt)    #每一秒跑 1000 次
    t = t + dt    #計時器
    
    blue_ball.a = Fg/m            #球的加速度
    green_ball.a = Fg/m            #球的加速度
    if(blue):
        blue_ball.a=vector(0,0,0)
    blue_ball.v = blue_ball.v + blue_ball.a*dt          #球的末速度 = 前一刻速度 + 加速度*時間間隔
    green_ball.v = green_ball.v + green_ball.a*dt          #球的末速度 = 前一刻速度 + 加速度*時間間隔
    blue_ball.pos = blue_ball.pos + blue_ball.v * dt    #球的末位置 = 前一刻位置 + 速度*時間間隔
    green_ball.pos = green_ball.pos + green_ball.v * dt    #球的末位置 = 前一刻位置 + 速度*時間間隔
    if(blue_ball.pos.y<0):
        blue_ball.v=vector(0,0,0)
        blue=1


    t1=0
    t2=0
    y1=0
    y2=0
    d1=0
    d2=0
    if(blue_ball.pos.y-0<pow(10,-2) and t>0.5 and blue!=1):
        t1=t
        d1=blue_ball.pos.x
        blue_ball.pos.y=pow(10,-6)

    if(blue_ball.v.y-0<=pow(10,-2)and t>1):
        y1=blue_ball.pos.y

    if(green_ball.v.y-0<=pow(10,-5)):
        y2=green_ball.pos.y
t2=t
d2=green_ball.pos.x

print(f"30度的飛行時間= {t1}")
print(f"30度的最大高度= {y1}")
print(f"30度的水平射程= {d1}")
print(f"60度的飛行時間= {t2}")
print(f"60度的最大高度= {y2}")
print(f"60度的水平射程= {d2}")

