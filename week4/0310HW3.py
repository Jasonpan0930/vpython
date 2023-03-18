from vpython import *
g = 9.8                 #重力加速度 9.8 m/s^2
size = 0.05             #球半徑 0.05 m            
L = 0.5                 #彈簧原長 0.5m
k = 100000              #彈簧力常數 100000 N/m
m = 0.1                 #球質量 0.1 kg
theta = 30 * pi/180     #初始擺角
Fg = m*vector(0,-g,0)   #球所受重力向量
damp=0.1

def SpringForce(r,L):
    return -k*(mag(r)-L)*norm(r)

def SpringDamp(v, r):  #避震器
    if(mag(v)>0):
        cos_theta = dot(v,r)/(mag(v)*mag(r))                    #用向量內積找v和r夾角的餘弦函數
        r_unit_vector = norm(r)                                 #沿彈簧軸方向的單位向量
        projection_vector = mag(v) * cos_theta * r_unit_vector  #計算v在r方向的分量
        spring_damp = - damp * projection_vector                #沿彈簧軸方向的阻力
        return spring_damp
    return vector(0,0,0)

scene = canvas(width=600, height=600, center=vector(0, -L*0.8, 0), range=1.2*L)#設定畫面
ceiling = box(length=0.4, height=0.005, width=0.4, opacity = 0.2)#畫天花板
ball = sphere(radius = size,  color=color.yellow, make_trail = True, retain = 1000, interval=1)#畫球
rod = cylinder(radius=size/10)#畫繩子
	
ball.pos = vector(L*sin(theta), -L*cos(theta), 0)   #球的初始位置
ball.v = vector(0, 0, 0)                            #球初速
rod.pos = vector(0, 0, 0)                           #繩子頭端的位置

Fg_arrow=arrow(shaftwidth = 0.02, color=color.yellow)
Fg_text=label(box = False, opacity = 0, height = 25, color=color.yellow, text = 'Fg')

v_arrow=arrow(shaftwidth = 0.02, color=color.green)
v_text=label(box = False, opacity = 0, height = 25, color=color.green, text = 'v')

Fs_arrow=arrow(shaftwidth = 0.02, color=color.white)
Fs_text=label(box = False, opacity = 0, height = 25, color=color.white, text = 'Fs')

Ft_arrow=arrow(shaftwidth = 0.02, color=color.red)
Ft_text=label(box = False, opacity = 0, height = 25, color=color.red, text = 'F_tot')

dt = 0.001    #時間間隔
t = 0.0       #初始時間
t_right = 0   #右端點時間 
X=0.2

while True:
    rate(1/dt)
    rod.axis = ball.pos - rod.pos                #繩子的軸方向：由繩子頭端指向尾端的向量
    
    ball.a = (Fg + SpringForce(rod.axis,L)+SpringDamp(ball.v, rod.axis))/m    #牛頓第二定律：加速度＝合力/質量
    ball.v += ball.a*dt    
    ball.pos += ball.v*dt

    Fg_arrow.pos=ball.pos
    v_arrow.pos=ball.pos
    Fs_arrow.pos=ball.pos
    Ft_arrow.pos=ball.pos

    Fg_text.pos=Fg_arrow.pos+Fg_arrow.axis*1.2
    v_text.pos=v_arrow.pos+v_arrow.axis*1.2
    Fs_text.pos=Fs_arrow.pos+Fs_arrow.axis*1.2
    Ft_text.pos=Ft_arrow.pos+Ft_arrow.axis*1.2

    Fg_arrow.axis=Fg*X
    v_arrow.axis=ball.v*X
    Fs_arrow.axis=SpringForce(rod.axis,L)*X
    Ft_arrow.axis=(Fg+SpringForce(rod.axis,L))*X
    print(SpringDamp(ball.v, rod.axis))
        
    t += dt