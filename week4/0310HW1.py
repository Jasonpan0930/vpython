from vpython import *
g = 9.8                 #重力加速度 9.8 m/s^2
size = 0.05             #球半徑 0.05 m            
L = 0.5                 #彈簧原長 0.5m
k = 10                  #彈簧力常數 10 N/m
m = 0.1                 #球質量 0.1 kg
Fg = m*vector(0,-g,0)   #球所受重力向量
X=0.2

def SpringForce(r,L):
    return -k*(mag(r)-L)*norm(r)

def SpringU(r, L):
    return 0.5*k*(mag(r)-L)*(mag(r)-L)

scene = canvas(width=600, height=600, center=vector(0, -L*0.8, 0), range=1.2*L)#設定畫面
ceiling = box(length=0.4, height=0.005, width=0.4, opacity = 0.2)#畫天花板
ball = sphere(radius = size,  color=color.yellow)#畫球
spring = helix(radius=0.02, thickness =0.01)#畫彈簧
	
ball.pos = vector(0, -L, 0)     #球在t=0時的位置
ball.v = vector(0, 0, 0)        #球初速
spring.pos = vector(0, 0, 0)    #彈簧頭端的位置

Fg_arrow=arrow(shaftwidth = 0.02, color=color.yellow)
Fg_text=label(box = False, opacity = 0, height = 25, color=color.yellow, text = 'Fg')

v_arrow=arrow(shaftwidth = 0.02, color=color.green)
v_text=label(box = False, opacity = 0, height = 25, color=color.green, text = 'v')

Fs_arrow=arrow(shaftwidth = 0.02, color=color.white)
Fs_text=label(box = False, opacity = 0, height = 25, color=color.white, text = 'Fs')

Ft_arrow=arrow(shaftwidth = 0.02, color=color.red)
Ft_text=label(box = False, opacity = 0, height = 25, color=color.red, text = 'F_tot')

t = 0
dt = 0.001

gd1 = graph(title = "Energy check green for K, red for Us, blue for Ug, black for TOTAL", width=600, height=400, xtitle="t", ytitle="Energy")
fUg = gcurve(color=color.blue)
fK = gcurve(color=color.green)
fUs = gcurve(color=color.red)
fUt = gcurve(color=color.black)

while t < 5:
    rate(1/dt)
    spring.axis = ball.pos - spring.pos           #彈簧的軸方向，由頭端指向尾端的距離向量
    ball.a = (Fg + SpringForce(spring.axis,L))/m  #球的加速度由重力和彈力所造成
    ball.v += ball.a*dt      #球的速度
    ball.pos += ball.v*dt    #球的位

    Fg_arrow.pos=ball.pos
    v_arrow.pos=ball.pos+vector(2.5*size,0,0)
    Fs_arrow.pos=ball.pos
    Ft_arrow.pos=ball.pos+ vector(-2.5*size,0,0)

    Fg_text.pos=Fg_arrow.pos+Fg_arrow.axis*1.2
    v_text.pos=v_arrow.pos+v_arrow.axis*1.2
    Fs_text.pos=Fs_arrow.pos+Fs_arrow.axis*1.2
    Ft_text.pos=Ft_arrow.pos+Ft_arrow.axis*1.2

    Fg_arrow.axis=Fg*X
    v_arrow.axis=ball.v*X
    Fs_arrow.axis=SpringForce(spring.axis,L)*X
    Ft_arrow.axis=(Fg+SpringForce(spring.axis,L))*X

    Ug = m * g * (ball.pos.y)+m*g*L
    Us = 0.5 * k * ( mag(spring.axis) - L )**2
    K = 0.5 * m * mag(ball.v)**2

    fUg.plot(pos=(t, Ug))
    fK.plot(pos=(t, K))
    fUs.plot(pos=(t, Us))
    fUt.plot(pos=(t, Ug+Us+K))
    print(Ug+Us+K)

    t+=dt
    