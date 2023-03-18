from vpython import *  #引用套件Vpython

G = 6.67*10**(-11)  #萬有引力常數
M = 6*10**24    #地球質量
m = 1000    #衛星質量
Re = 6.4*10**6  #地球半徑
r = 5*Re  #衛星軌道半徑
t = 0   
dt = 1
v0 = sqrt(G*M/r)   #衛星繞行速率   

def F_g(x):                                 #定義萬有引力公式
    return -G*M*m/(mag(x)**3)*x

scene = canvas(width=600, height=600, center=vec(1.6*Re,0,0), background=vec(0.6,0.8,0.8)) #設定視窗
earth = sphere(pos=vec(0,0,0), radius=Re, texture=textures.earth) #放置物件地球
mater = sphere(pos=vec(r,0,0), v = vec (0,0.7*v0,0), a = vec(0,0,0),radius=0.1*Re,color=color.red, make_trail=True) #放置物件衛星

def position():
    return vec(mater.pos.x, mater.pos.y, mater.pos.z)

up=vec(0,0,0)
down=vec(0,0,0)
left=vec(0,0,0)
right=vec(0,0,0)

while(1):  #執行無窮迴圈
    rate(5000)
    
    mater.a = F_g(mater.pos-earth.pos)/m
    mater.v += mater.a*dt   
    mater.pos += mater.v*dt  
    
    
    if(mater.v.y>0 and mater.v.y+mater.a.y*dt<0):
        up=position()

    if(mater.v.y<0 and mater.v.y+mater.a.y*dt>0): 
        down=position()

    if(mater.v.x<0 and mater.v.x+mater.a.x*dt>0): 
        left=position()
        
    if(mater.v.x>0 and mater.v.x+mater.a.x*dt<0): 
        right=position()
        break
    t += dt

print("上端點:", up)
print("左端點:", left) 
print("下端點:", down)
print("右端點:", right)

a=(right.x-left.x)/2
b=(up.y-down.y)/2
c=a*a-b*b
c=sqrt(c)

print("The semi-major axis is : ",a)
print("The semi-minor axis is : ",b)
print("The focal distance is : ", c)