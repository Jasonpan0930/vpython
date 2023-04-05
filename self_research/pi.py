from vpython import *

m1=10000000000
m2=1

def collision(v1,v2):
    v11=(m1-m2)/(m1+m2)*v1+(2*m2)/(m1+m2)*v2
    v22=(2*m1)/(m1+m2)*v1+(m2-m1)/(m1+m2)*v2
    return(v11, v22)

box1=box(pos=vector(100,5,0), size=vec(10,10,10), v=vec(-50,0,0))
box2=box(pos=vector(20,5,0), size=vec(10,10,10), v=vec(0, 0, 0))
wall=box(pos=vector(0,200,0),size=vec(0.5,400,20) )
dt=0.0001
time=0
text = label(pos=vec(20,20,20),box = False, opacity = 0, height = 25, color=color.green, text = 0)
while(True):
    rate=1/dt
    box1.pos+=dt*box1.v
    box2.pos+=dt*box2.v
    if(box1.pos.x-box2.pos.x<10):
        box1.v, box2.v=collision(box1.v, box2.v)
        time+=1
    if(box2.pos.x<5):
        box2.v*=-1
        time+=1

    text.text=time