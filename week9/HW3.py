from vpython import *  #引用視覺畫套件Vpython

k = 9*10**9   
size = 0.1  
N = 36  #電力線數量
q = 10**(-2)
m = 1


Q1_charge = 10**(-5) #Q1電量 
Q1_position = vec(0, 0, 0) #Q1位置

Q2_charge = -10**(-5)
Q2_position = vec(2,0,0)
t = 0 
dt = 0.001

scene = canvas(title='line of electric force', height=600, width=1200, range=3.5,auto_scale=False, background=vec(0.3,0.4,0.4), center=vec(1,0,0))
Q1 = sphere(pos = Q1_position , radius = size , color = color.blue)
Q2 = sphere(pos = Q2_position , radius = size , color = color.red)

#畫出每個質點球, 每個球的名稱為field_ball[i] 
field_ball=[]
for i in range(N):
    field_ball.append(sphere(pos=vec(size*cos(2*pi*i/N), size*sin(2*pi*i/N),0) + Q1_position, radius=0.01, color=color.yellow, make_trail=True, v=vec(0,0,0)))

field_ball2=[]
for i in range(N):
    field_ball2.append(sphere(pos=vec(size*cos(2*pi*i/N), size*sin(2*pi*i/N),0) + Q2_position, radius=0.01, color=color.yellow, make_trail=True, v=vec(0,0,0)))

def Force_E(r, q):  #定義靜電力，請將庫倫定律寫於此，r為與場源距離，q為電荷帶電量
    return k*Q1_charge*q*norm(r-Q1_position)/(mag(r-Q1_position)**2) + k*Q2_charge*q*norm(r-Q2_position)/(mag(r-Q2_position)**2)

while True:
    rate(1500)
    for i in field_ball:
        if(mag(i.pos-Q2_position)>size):
            i.v = (Force_E(i.pos, q)) / m * dt   #設定小球移動方向為單位正電荷的受力方向
            i.pos += i.v * dt

    for i in field_ball2:
        if(mag(i.pos-Q1_position)>size):
            i.v = (Force_E(i.pos, -1*q)) / m * dt   #設定小球移動方向為單位正電荷的受力方向
            i.pos += i.v * dt