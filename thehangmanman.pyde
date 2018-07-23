def setup():
    size(600,600)
    background(255)
                  #Hangman Platform (placed in setup since it will only be drawn once)
    line(250, 100, 250, 200) #first middle line
    line(300, 100, 250, 100) #right line ( where hangman head is placed)
    line(250, 300, 250, 200) #lengthens the  first middle line
    line(220, 300, 280, 300) #last line of the platform

    #head = createShape(ellipse(330, 120, 40, 40)) #hangman head
    #leftarm = createShape(line(330,170, 310, 190))  #left hand
    #rightarm = createShape(line(330,170, 350, 190 )) #right hand
    #leftleg = createShape(line(330, 235 ,310, 270)) #left leg
    #rightleg = createShape(line(330, 240, 350, 270)) #right leg
    #body = createShape(line(330, 140, 330, 240))  #hangman body
            #line(x1,y1, x2,y2)   #Hangman 
def draw(): 
    head = createShape(ellipse(330, 120, 40, 40)) #hangman head
    leftarm = createShape(line(330,170, 310, 190))  #left hand
    rightarm = createShape(line(330,170, 350, 190 )) #right hand
    leftleg = createShape(line(330, 235 ,310, 270)) #left leg
    rightleg = createShape(line(330, 240, 350, 270)) #right leg
    body = createShape(line(330, 140, 330, 240))  #hangman body
    s.beginShape(head)



        
                  
                  
                  
    #ellipse(330, 120, 40, 40) #hangman head
    #line(330, 140, 330, 240) #hangman body
    #line(330, 235 ,310, 270) #left leg
    #line(330, 240, 350, 270) #right leg
    #line(330,170, 310, 190) #left hand
    #line(330,170, 350, 190 ) #right hand
    
    
    
