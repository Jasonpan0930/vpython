from vpython import *

size = 0.1

scene = canvas(width=600, height=400, center=vector(2.5,0,0), background=vector(0,0,0))
#設定物件視窗的顯示畫面與背景，寬為600畫素、高為400畫素
#center為畫面中心，background為背景顏色

x = arrow(pos=vector(0,0,0), axis=vector(1,0,0), shaftwidth=0.02, color=color.green)
y = arrow(pos=vector(0,0,0), axis=vector(0,1,0), shaftwidth=0.02, color=color.red)
z = arrow(pos=vector(0,0,0), axis=vector(0,0,1), shaftwidth=0.02, color=color.blue)
ball = sphere(radius=size, color=color.yellow, pos=vector(0,0,0), v=vector(-2.0,0,0), a=vector(3.0,0,0))

gd1 = graph(title = "x-t plot", width=600, height=400, xtitle="t", ytitle="x")
gd2 = graph(title = "v-t plot", width=600, height=400, xtitle="t", ytitle="v")
gd3 = graph(title = "a-t plot", width=600, height=400, xtitle="t", ytitle="a")
#設定函數圖的畫面
xt = gcurve(graph=gd1, color=color.blue)  	#設定函數圖中線條的特性，這裡只設定顏色
vt = gcurve(graph=gd2, color=color.green)
at = gcurve(graph=gd3, color=color.red)

dt = 0.001
t = 0.0

while t<5:
    rate(1/dt)
    t = t+dt
    ball.pos +=ball.v*dt
    ball.v+=ball.a*dt

    xt.plot(pos=(t,ball.pos.x))	#每一個迴圈畫一個點描出線條，x軸為時間，y軸為位置
    vt.plot(pos=(t,ball.v.x))
    at.plot(pos=(t,ball.a.x))

    if( ball.v.x + ball.a.x*dt>=0 and ball.v.x<0):
        print("折返囉")
        print("t = ", round(t, 2))
        print("x = ", round(ball.pos.x, 2))
        print("v = ", round(ball.v.x, 2))

    if(t+dt>=3 and t<3):
        print("t = ", round(t, 2), "s, position = ", round(ball.pos.x, 2))