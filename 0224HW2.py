from vpython import*	

size = 0.1    #螞蟻的大小
v_0 = 2    #螞蟻的速率

scene = canvas(center = vector(0,sqrt(3),0), background=vec(0.6,0.8,0.8))
ant1 = sphere(radius=size, color=color.yellow, pos=vec(2,0,0), v=vec(0,0,0), make_trail = True)
ant2 = sphere(radius=size, color=color.red, pos=vec(-2,0,0), v=vec(0,0,0), make_trail = True)
ant3 = sphere(radius=size, color=color.blue, pos=vec(0,2*sqrt(3),0), v=vec(0,0,0), make_trail = True)    
#用球來模擬螞蟻的運動

dt = 0.001	
t = 0.0		

while (mag(ant1.pos-ant2.pos)>0.01) :    #這邊請填入如何判斷螞蟻相聚 
    rate(1/dt)      
    t = t+dt
    
    # hat_va=(ant2.pos-ant1.pos)/mag(ant2.pos-ant1.pos)
    # hat_vb=(ant3.pos-ant2.pos)/mag(ant3.pos-ant2.pos)
    # hat_vc=(ant1.pos-ant3.pos)/mag(ant1.pos-ant3.pos)

    # ant1.v = hat_va*2   #該如何指定螞蟻們的速度向量？
    # ant2.v = hat_vb*2
    # ant3.v = hat_vc*2

    ant1.v = (ant2.pos-ant1.pos).hat*2    #該如何指定螞蟻們的速度向量？
    ant2.v = (ant3.pos-ant2.pos).hat*2
    ant3.v = (ant1.pos-ant3.pos).hat*2
    
    ant1.pos = ant1.pos + ant1.v*dt    #一小段時間的等速度運動
    ant2.pos = ant2.pos + ant2.v*dt  
    ant3.pos = ant3.pos + ant3.v*dt

print ("相聚時間：" , t)