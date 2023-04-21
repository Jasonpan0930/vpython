from vpython import *
k = 9*10**9  
size = 0.1  
N = 36  #電力線數量
Q1_charge = 10**(-5) #Q1電量
Q1_position = vec(0, 0, 0) #Q1位置
Q2_charge = -10**(-5)
Q2_position = vec(2,0,0)
t, dt = 0, 0.001

scene = canvas(title='line of electric force', height=600, width=1200, range=3.5,auto_scale=False, background=vec(0.3,0.4,0.4), center=vec(1,0,0))
Q1 = sphere(pos = Q1_position , radius = size , color = color.blue)
Q2 = sphere(pos = Q2_position , radius = size , color = color.red)

#畫出每個質點球, 每個球的名稱為field_ball[i]
field_ball=[]
for i in range(N):
    field_ball.append(sphere(pos=vec(size*cos(2*pi*i/N), size*sin(2*pi*i/N),0) + Q1_position, radius=0.01, color=color.yellow, make_trail=True, v=vec(0,0,0)))

field_ball2 = []
for i in range(N):
    field_ball2.append(sphere(pos=vec(size*cos(2*pi*i/N), size*sin(2*pi*i/N),0) + Q2_position, radius=0.01, color=color.yellow, make_trail=True, v=vec(0,0,0)))

def Force_E(p, q):  #定義靜電力，請將庫倫定律寫於此，r為與場源距離，q為電荷帶電量
    return (k * Q1_charge * q / mag(p-Q1_position)**2 * hat(p-Q1_position)) + (k * Q2_charge * q / mag(p-Q2_position)**2 * hat(p-Q2_position))

while True:
    rate(1500)
    for i, i2 in zip(field_ball, field_ball2):
        q = 1.6*10**(-3)
        m = 1
        if mag(i.pos-Q2_position) > size :
            i.v = Force_E(i.pos, q) * dt / m   #設定小球移動方向為單位正電荷的受力方向
            i.pos += i.v*dt
        if mag(i2.pos-Q1_position) > size :
            i2.v = Force_E(i2.pos, -q) * dt / m   #設定小球移動方向為單位正電荷的受力方向
            i2.pos += i2.v*dt