from vpython import*  

G = 6.67 
M = 6*10**2
Re = 10 

def g(r):   #定義重力場公式
    return -G*M/(mag(r)**2)*norm(r)

scene = canvas(width=1000, height=800, center=vec(0,0,0), background=vec(0.6,0.8,0.8), range = 6*Re)
earth = sphere(pos=vec(0,0,0), radius=Re, texture=textures.earth)

arrowlist = []  #定義箭頭放置的List
for N1 in range(-5,6,1): #X軸
    for N2 in range(-5,6,1):#Y軸
        for N3 in range(-5,6,1):
            arrowlist.append(arrow(pos = vector(N1*Re,N2*Re,N3*Re), axis = vec(5,0,0), shaftwidth = 1, color = color.red))

for i in arrowlist:
    if(mag(i.pos)<=Re):
        i.axis=vector(0,0,0)
    else:
        i.axis = g(i.pos) #這邊自己想要填什麼東西
    