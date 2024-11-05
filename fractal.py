import pygame
pygame.init()

width,height=2100,1080
win=pygame.display.set_mode((width,height))
Clock=pygame.time.Clock()
run=True

def add(a,b):
    return (a[0]+b[0]),(a[1]+b[1])
    
def square(z):
    a,b=z
    return ((a*a)-(b*b)) , (2*a*b)
    
def f(z,c=[0,0]):
    return add(square(z),c)
    
    
def is_fractal(z,iterations=100,blacks=0):
    if iterations>2500:
        iterations=2500
        
    c=[0,0]
    for i in range(iterations):
        c=f(c,z)
        if c[0]>2 or c[1]>2:
            return i/iterations
            
        if i>(iterations/4):
            if blacks>7:
                return -2
    return -1
    
    

zoom=8


while run:   
    win.fill((0,0,0))
    pygame.draw.rect(win,((50,50,50)),((width,0),(1,height)))
    calc=[(zoom*1000),((1.75/zoom)-(0.15)),(zoom*15)]
    blacks=0
    for x in range(width):
        for y in range(height):
            a=((x/(calc[0]))-(calc[1]))
            b=((y/(calc[0]))-(0.65))
            
            if zoom>15:
                r=is_fractal([a,b],calc[2],blacks)
            else:
                r=is_fractal([a,b],100,blacks)
             
            if r==0 or r==-1:
                blacks+=1   
            elif r==-2:
                #pygame.draw.rect(win,(255,0,0),((x,y),(1,1)))
                blacks=0
            
            if r>=0:
                c=255
                if r>0:
                    c*=r
                    
                c=int(c)
                if c>255:
                    c=255
                elif c<0:
                    c=0
                color=(c,c,c)
                pygame.draw.rect(win,(color),((x,y),(1,1)))
        
        pygame.display.update()
        Clock.tick(60)
    zoom*=2