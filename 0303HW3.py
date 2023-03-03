from vpython import*

scene = canvas(width = 600 , height = 600 , center=vector(10,0,0), background=vector(0.6,0.8,0.8))  #設定畫布

ball = sphere(radius=1, color=color.yellow, pos=vector(0,0,0), v=vector(0,6.0,0),a=vector(0,0,0),make_trail = True) #設定球的初始狀態
dt = 0.001
t = 0.0
m = 1.0
F = vector(4.0,0,0)             #設定力的初始狀態
right = 0                       #紀錄右端點
left = 0                        #紀錄左端點

while True:                     #無窮迴圈
    rate(1/dt)
    t = t+dt
    
    ball.a = F/m
    ball.v = ball.v + ball.a*dt
    ball.pos = ball.pos + ball.v*dt

    F_vec = rotate(ball.v, angle=-pi/2)    #請使用rotate的語法，找出F向量的方向
    F = 4.0*norm(F_vec)    #沿力的方向(F_vec)長出大小為4.0的力
    
    if(abs(ball.pos.y-0)<0.01 and ball.pos.x>0):    #右端點條件
        right = ball.pos.x
    if (abs(ball.pos.y-0)<0.01 and ball.pos.x<0):    #左端點條件
        left = ball.pos.x
        print ("theoretical radius = ", m*mag(ball.v)*mag(ball.v)/mag(F))    #請思考如何利用受力分析出理論上的半徑為何？
        print ("simulated radius = " , (right-left)/2)    #模擬的半徑值