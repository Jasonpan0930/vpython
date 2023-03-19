from vpython import *

size = 0.1   # 木塊邊長
L = 1        # 地板長度
v = 0.03     # 木塊速度
t = 0        # 時間
dt = 0.01    # 時間間隔

scene = canvas(title="1D Motion", width=800, height=600, x=0, y=0, center=vec(0, 0, 0), background=vec(0, 0.6, 0.6))
floor = box(pos=vec(0, 0, 0), size=vec(L, 0.1*size, 0.5*L), color=color.blue)
cube = box(pos=vec(-0.5*L + 0.5*size, 0.55*size, 0), size=vec(size, size, size), color=color.red, v=vec(v, 0, 0))
 
gd = graph(title="x-t plot", width=600, height=450, x=0, y=600, xtitle="t(s)", ytitle="x(m)")
gd2 = graph(title="v-t plot", width=600, height=450, x=0, y=1050, xtitle="t(s)", ytitle="v(m/s)")

xt = gcurve(graph=gd, color=color.red)
vt = gcurve(graph=gd2, color=color.red)

while(cube.pos.x <= 0.5*L - 0.5*size):
    rate(1000)
    cube.pos.x += v*dt
    xt.plot(pos = (t, cube.pos.x))
    vt.plot(pos = (t, cube.v.x))
    t += dt

print("t = ", t)