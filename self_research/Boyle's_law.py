from vpython import *
import random

size = 0.05    #球的大小         
side = 3.0    #箱子牆壁所在位置  
thk = 0.01    #牆壁厚度
s2 = 2*side - thk    #牆壁大小
s3 = 2*side + thk
n=1000  #number of balls
abs_speed=50
m=1

scene = canvas(width=800, height=800, center = vec(0,0,0), background=vec(0.6,0.8,0.8)) #設定畫面
#畫牆壁
wall_R = box (pos=vector( side, 0, 0), size=vector(thk, s2, s3),  color = color.red, v=vec(0.5, 0, 0))
wall_L = box (pos=vector(-side, 0, 0), size=vector(thk, s2, s3),  color = color.red)
wall_B = box (pos=vector(0, -side, 0), size=vector(s3, thk, s3),  color = color.blue)
wall_T = box (pos=vector(0,  side, 0), size=vector(s3, thk, s3),  color = color.blue)
wall_BK = box(pos=vector(0, 0, -side), size=vector(s2, s2, thk), color = color.gray(0.7))

ball_list=[]

for i in range(n):
    x=0
    y=0
    z=0
    position_is_set=0
    while(position_is_set==0):
        x=-side+side*2*random.random()
        y=-side+side*2*random.random()
        z=-side+side*2*random.random()
        if(i==0):
            position_is_set=1
        else:
            for j in range(i):
                if(mag(vec(x, y, z)-ball_list[j].pos)<=2*size):
                    break
                if(j==i-1):
                    position_is_set=1

    vx=random.random()
    vy=random.random()
    vz=random.random()
    vx-=0.5
    vy-=0.5
    vz-=0.5
    speed=vec(vx, vy, vz)
    speed=abs_speed*hat(speed)

    ball=sphere(radius = size, color=color.yellow , pos = vec(x,y,z) ,v = speed, make_trail = False, retain = 100) #畫球
    ball_list.append(ball)



    
t = 0
dt = 0.001         #時間間隔 0.001 秒

time=0
Fx=0
Fy=0
Fz=0

gd1=graph(title = "PV-t plot", width=600, height=400, xtitle="t", ytitle="PV")
fPV = gcurve(color=color.blue, graph=gd1)

gd2=graph(title = "V-t plot", width=600, height=400, xtitle="t", ytitle="V")
fV = gcurve(color=color.red, graph=gd2)

while True:             
    rate(10000)                          #每一秒跑 1000 次
    time+=1
    t+=dt
    wall_R.pos+=wall_R.v*dt
    if(abs(wall_R.pos.x-wall_L.pos.x)>15):
        break
    for i in range(n):
        ball_list[i].pos+=ball_list[i].v*dt
    
    wall_T.pos=vec((wall_R.pos.x+wall_L.pos.x)/2, side, 0)
    wall_T.size=vec(wall_R.pos.x-wall_L.pos.x, thk, s3)

    wall_B.pos=vec((wall_R.pos.x+wall_L.pos.x)/2, -side, 0)
    wall_B.size=vec(wall_R.pos.x-wall_L.pos.x, thk, s3)

    wall_BK.pos=vec((wall_R.pos.x+wall_L.pos.x)/2, 0, -side)
    wall_BK.size=vec(wall_R.pos.x-wall_L.pos.x, s2, thk)
   
    #球撞擊牆面時，使球反彈
    Redge=wall_R.pos.x
    Ledge=wall_L.pos.x
    Bedge=wall_B.pos.y
    Tedge=wall_T.pos.y
    BKedge=wall_BK.pos.z
    FRedge=side
    for i in range(n):
        if ball_list[i].pos.x>Redge and ball_list[i].v.x>0 :    #請思考如何判斷球1撞擊左右兩牆
            ball_list[i].v.x = -ball_list[i].v.x
        if ball_list[i].pos.x<Ledge :    #請思考如何判斷球1撞擊左右兩牆
            ball_list[i].v.x = -ball_list[i].v.x
            Fx+=m*2*abs(ball_list[i].v.x)
        if ball_list[i].pos.y>Tedge or ball_list[i].pos.y<Bedge :    #請思考如何判斷球1撞擊上下兩牆
            ball_list[i].v.y = -ball_list[i].v.y
            Fy+=m*2*abs(ball_list[i].v.y)
        if ball_list[i].pos.z>FRedge or ball_list[i].pos.z<BKedge :    #請思考如何判斷球1撞擊前後兩牆
            ball_list[i].v.z = -ball_list[i].v.z
            Fz+=m*2*abs(ball_list[i].v.z)


    delta_t=200
    if(time==delta_t):
        P=Fx/(delta_t*4*side**2)
        Fx=0
        time=0
        V=(wall_R.pos.x-wall_L.pos.x)*4*side**2
        fPV.plot(pos=(t, P*V))
        fV.plot(pos=(t, V))
        print(P*V)

    


