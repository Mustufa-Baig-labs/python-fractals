import pygame
pygame.init()

try:
    zoom=int(input("Zoom->"))
    print("Program has begun...")
except:
    print("Switching to default...")
    zoom=1


width,height=1366,768
        
win=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
Clock=pygame.time.Clock()
run=True

def add(a,b):
    return (a[0]+b[0]),(a[1]+b[1])
    
def square(z):
    a,b=z
    return ((a*a)-(b*b)) , (2*a*b)
    
def f(z,c=[0,0]):
    return add(square(z),c)
    
    
def is_fractal(z,iterations,blacks=0):
    if iterations>3000:
        iterations=3000
        
    c=[0,0]
    for i in range(iterations):
        c=f(c,z)
        if c[0]>2 or c[1]>2:
            result=(i/600)
            
            return result
            
        if i>(iterations/5):
            if blacks>5:
                return -2
    return -1
    
    


while run:   
    win.fill((0,0,0))
    pygame.draw.rect(win,((50,50,50)),((width-1,0),(1,height)))
    calc=[(zoom*height),((1.75/zoom)-(0.15)),(zoom*50)]
    print("Zoom =",zoom)
    blacks=0
    for x in range(width):
        if not(run):
            break
        for y in range(height):
            a=((x/calc[0])-(calc[1]))
            b=((y/calc[0])-(0.64))
            
            if zoom>15:
                r=is_fractal([a,b],calc[2],blacks)
            else:
                r=is_fractal([a,b],750,blacks)
             
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
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                
        pygame.display.update()
        Clock.tick(60)
    zoom*=2

    
pygame.quit()

