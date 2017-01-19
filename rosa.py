import turtle
 
t = turtle.Turtle()
j = turtle.Screen()
 
def espiral(t, lineLen):
    if lineLen < 10000:      
        if(lineLen % 2 == 0):
            t.pencolor("pink")
        else:
            t.pencolor("#00BFFF")          
        t.forward(lineLen)      
        t.left(91)            #inclinação 91 graus à esquerda
        espiral(t,lineLen+3)
 
#inicio
t.screen.bgcolor("black")
t.width(1) #ponta caneta
t.speed(1000)
espiral(t,0)
 
#saida
j.exitonclick()
