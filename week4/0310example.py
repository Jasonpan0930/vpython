from vpython import*

scene = canvas(width = 600 , height = 600 , center = vector(10,0,0), background = vec(0.6,0.8,0.8))  

ball = sphere(radius = 1, color = color.yellow, pos = vec(0,0,0), v = vec(0,6.0,0), a = vec(0,0,0), make_trail=True) 
dt = 0.001
t = 0.0
m = 1.0
F = vec(4.0,0,0)            

v_vector = arrow(shaftwidth = 0.3, headwidth = 0.8, headlength = 1.0, color=color.blue)  #畫描述v的箭頭
v_text = label(box = False, opacity = 0, height = 25, color=color.blue, text = 'v')  #產生文字標籤'v'                 
a_vector = arrow(shaftwidth = 0.3, headwidth = 0.8, headlength = 1.0, color=color.red)  #畫描述a的箭頭
a_text = label(box = False, opacity = 0, height = 25, color=color.red, text = 'a')  #產生文字標籤'a'    

while True:                    
    rate(2*1/dt)
    t += dt 
    
    ball.a = F/m
    ball.v += ball.a*dt
    ball.pos += ball.v*dt

    F_vec = ball.v.rotate(angle=-pi/2)   
    F = 4.0*norm(F_vec)   

    v_vector.pos = ball.pos        #將速度箭頭的位置放在球的位置
    v_vector.axis = ball.v         #將速度箭頭的軸方向指向速度方向，並將箭頭的長度設定為半徑的一半
    v_text.pos = v_vector.pos + v_vector.axis*1.2 #文字標籤'v'的位置
    
    a_vector.pos = ball.pos        #將加速度箭頭的位置放在球的位置
    a_vector.axis = ball.a         #將加速度箭頭的軸方向指向速度方向，並將箭頭的長度設定為半徑的一半    
    a_text.pos = a_vector.pos + a_vector.axis*1.2 #文字標籤'a'的位置