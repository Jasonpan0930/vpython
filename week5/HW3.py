from vpython import *  #引用套件Vpython

G = 6.67*10**(-11)  #萬有引力常數
M = 2*10**30    #太陽質量
me = 6*10**24   #地球質量
mm = 6.4*10**23    #火星質量
Rs = 7*10**8  #太陽半徑
R=10**8
re = 5*Rs   #地球軌道半徑
rm = 7*Rs   #火星軌道半徑
v0_e = 0.7*sqrt(G*M/re)     #地球繞行速率
v0_m = 0.7*sqrt(G*M/rm)     #火星繞行速率  

t = 0   
dt = 1

def a_g(x):                                 #定義萬有引力公式
    return -G*M/(mag(x)**3)*x

scene = canvas(width=600, height=600, center=vec(1.6*Rs,0,0), background=vec(0.6,0.8,0.8)) #設定視窗
sun = sphere(pos=vec(0,0,0), radius=Rs, color = color.yellow) 
earth = sphere(pos=vec(re,0,0), v=vec(0, v0_e, 0), a=vec(0,0,0), radius=R, texture=textures.earth, make_trail=True) #放置物件地球
mars = sphere(pos=vec(rm,0,0), v=vec(0, v0_m, 0), a=vec(0,0,0), radius=R, color=color.red, make_trail=True) #放置物件衛星

te=0
tm=0
righte=0
rightm=0
lefte=0
leftm=0

print ("theoretical value for a^3/T^2 = ", G*M/(4*pi**2))

while True:  #執行無窮迴圈
    rate(5000)
    
    earth.a = a_g(earth.pos)
    mars.a = a_g(mars.pos)
    earth.v+=earth.a*dt
    mars.v+=mars.a*dt
    earth.pos+=earth.v*dt
    mars.pos+=mars.v*dt

    if(earth.v.x<0 and earth.v.x+earth.a.x*dt>0): 
        lefte=earth.pos.x

    if(mars.v.x<0 and mars.v.x+mars.a.x*dt>0): 
        leftm=mars.pos.x
        
    if(earth.v.x>0 and earth.v.x+earth.a.x*dt<0): 
        righte=earth.pos.x
        r=(righte-lefte)/2
        T=t-te
        te=t
        print("a^3/T^2 for Earth = ", r**3/T**2)

    if(mars.v.x>0 and mars.v.x+mars.a.x*dt<0): 
        rightm=mars.pos.x
        r=(rightm-leftm)/2
        T=t-tm
        tm=t
        print("a^3/T^2 for Mars = ", r**3/T**2)


    t += dt