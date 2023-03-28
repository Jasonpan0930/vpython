from vpython import *

size = 1    #球的大小                  
m1 = 2    #球1質量                 
m2 = 2    #球2質量           
side = 4.0    #箱子牆壁所在位置  
thk = 0.3    #牆壁厚度
s2 = 2*side - thk    #牆壁大小
s3 = 2*side + thk

scene = canvas(width=800, height=800, center = vec(0,0,0), background=vec(0.6,0.8,0.8)) #設定畫面
#畫牆壁
wall_R = box (pos=vector( side, 0, 0), size=vector(thk, s2, s3),  color = color.red)
wall_L = box (pos=vector(-side, 0, 0), size=vector(thk, s2, s3),  color = color.red)
wall_B = box (pos=vector(0, -side, 0), size=vector(s3, thk, s3),  color = color.blue)
wall_T = box (pos=vector(0,  side, 0), size=vector(s3, thk, s3),  color = color.blue)
wall_BK = box(pos=vector(0, 0, -side), size=vector(s2, s2, thk), color = color.gray(0.7))

Redge=wall_R.pos.x-thk/2-size
Ledge=wall_L.pos.x+thk/2+size
Bedge=wall_B.pos.y+thk/2+size
Tedge=wall_T.pos.y-thk/2-size
BKedge=wall_BK.pos.z+thk/2+size
FRedge=side-thk/2-size


ball1 = sphere(radius = size, color=color.yellow , pos = vec(-2,0.5,0) ,v = vec(6,0,1), make_trail = True, retain = 100) #畫球1
ball2 = sphere(radius = size, color=color.green , pos = vec(2,0,2)  , v = vec(0,6,2), make_trail = True, retain = 100) #畫球2
 
# 定義3D碰撞公式
def collision(v1, v2, r1, r2):
    v1_f = v1-(2*m2/(m1+m2))*((dot(v1-v2, r1-r2)/mag2(r1-r2)))*(r1-r2)   #請嘗試將碰撞公式填入其中
    v2_f = v2-(2*m1/(m1+m2))*((dot(v2-v1, r2-r1)/mag2(r2-r1)))*(r2-r1)
    return (v1_f, v2_f)
    
t = 0
dt = 0.001         #時間間隔 0.001 秒

while True:             
    rate(1000)                          #每一秒跑 1000 次

    ball1.pos += ball1.v*dt
    ball2.pos += ball2.v*dt

    #若兩球球心距離小於兩倍球半徑，則代入碰撞公式改變速度
    if mag(ball1.pos-ball2.pos)<=2*size :    #請思考如何判斷兩球相撞
        ball1.v, ball2.v = collision(ball1.v, ball2.v, ball1.pos, ball2.pos)
   
    #球撞擊牆面時，使球反彈
    if ball1.pos.x>Redge or ball1.pos.x<Ledge :    #請思考如何判斷球1撞擊左右兩牆
        ball1.v.x = -ball1.v.x
    if ball2.pos.x>Redge or ball2.pos.x<Ledge :    #請思考如何判斷球2撞擊左右兩牆
        ball2.v.x = -ball2.v.x
    if ball1.pos.y>Tedge or ball1.pos.y<Bedge :    #請思考如何判斷球1撞擊上下兩牆
        ball1.v.y = -ball1.v.y
    if ball2.pos.y>Tedge or ball2.pos.y<Bedge :    #請思考如何判斷球2撞擊上下兩牆
        ball2.v.y = -ball2.v.y
    if ball1.pos.z>FRedge or ball1.pos.z<BKedge :    #請思考如何判斷球1撞擊前後兩牆
        ball1.v.z = -ball1.v.z
    if ball2.pos.z>FRedge or ball2.pos.z<BKedge :    #請思考如何判斷球2撞擊前後兩牆
        ball2.v.z = -ball2.v.z