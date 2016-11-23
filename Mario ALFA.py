from tkinter import *

master = Tk()

    
master.geometry('1024x600')
master.title('Mario ALFA')

canvas = Canvas(master, width="1024", height="600")
canvas.pack()

Fondo = PhotoImage(file="MarioBros_Stage2.gif")
lblFondo = Label(master, image=Fondo).place(x=0,y=0)


#Estado normal
Mario = PhotoImage(file = "Mario-Sprite2.gif")  #Ubicacion i mario= posX-210/posY-450 ultimas plat 152
Mariolas = Label(master, image=Mario, bg = "black")
Mariolas.place(x=210,y=450)


#Enemigo

Koopa = PhotoImage (file= "Turtle2.gif")
Kupa = Label(master, image=Koopa, bg="black")
Kupa.place(x =850 ,y =130)

x1 = 850
y1 = 130

x = 210
y = 450
der = False
lef = False
Lim = 10
sal = False

def Move(event):
    global x,y,Mariolas,der,lef, Lim, sal
    tecla = repr (event.char)
##    print (tecla)
    #Mover derecha
    if (tecla == "'d'" or tecla == "'D'"):
        x+= 20
        Mariolas.destroy()
        Mariolas = Label(master, image=Mario)
        Mariolas.place(x= x,y = y)
        der = True
        lef = False
        
        if x >  1024:
            x = 50
            Mariolas.destroy()
            Mariolas = Label(master, image=Mario)
            Mariolas.place(x = x, y= y)
        
    #Mover Izquierda        
    elif (tecla== "'a'" or tecla == "'A'"):
        x-= 20
        Mariolas.destroy()
        Mariolas = Label(master, image = Mario)
        Mariolas.place(x = x,y= y)
        der = False
        lef = True
        
        if x < 0:
            x = 900
            Mariolas.destroy()
            Mariolas = Label(master, image=Mario)
            Mariolas.place(x = x,y= y)
    # Salto 1 plataf Derecha
    if (tecla == "'w'" or tecla == "'W'") and der == True and lef == False and sal==False:
            sal = True
            while Lim < 250:
                #Coalicion plataformas
                if ((y == 440 and not(y > 325 and x >390 and x < 610))or(y == 325 and not((x >150 and x < 250)or(x >750 and x < 850)))):
                    break
                x+=2
                y-=5
                Mariolas.destroy()
                Mariolas = Label(master, image=Mario)
                Mariolas.place(x=x, y=y)
                canvas.update()
                master.after(5)
##                print("Jump")
                Lim+=10
            Lim = 0
##            print(y)
            while Lim < 250:
                if (y == 450 or y == 360 or y == 250):
                    break
                x+=2
                y+=5
                Mariolas.destroy()
                Mariolas = Label(master, image=Mario)
                Mariolas.place(x=x, y=y)
                canvas.update()
                master.after(5)
##                print("Fall")
                Lim+=10
            sal = False
            Lim=0
    # Salto 1 plataf Izquierda
    elif (tecla == "'w'" or tecla == "'W'")and lef == True and der == False and sal==False:
        sal = True
        while Lim < 250:
            #Coalicion plataformas
            if ((y == 440 and not(y>325 and x >390 and x < 610))or(y == 325 and not((x >150 and x < 250)or(x >750 and x < 850)))):
                break
            x-=2
            y-=5
            Mariolas.destroy()
            Mariolas = Label(master, image=Mario)
            Mariolas.place(x=x, y=y)
            canvas.update()
            master.after(5)
##            print("Jump")
            Lim+= 10
        Lim=0
        while Lim < 250:
            #Coalicion plataformas
            if (y == 450 or y == 360 or y == 250):
                break
            x-=2
            y+=5
            Mariolas.destroy()
            Mariolas = Label(master, image=Mario)
            Mariolas.place(x=x, y=y)
            canvas.update()
            master.after(5)
##            print("Fall")
            Lim+=10
        sal = False
        Lim=0

def bajarplat():
    global x,y,Mariolas,der,lef,sal
##    print(x,y)
    #Coalicion plataformas
    if ((y == 360 and (x >390 and x < 610))or(y == 250 and ((x >150 and x < 250)or(x >750 and x < 850))))and sal==False:
##        print(x,y)
        sal=True
        Limt=0
        y+=5
        while Limt < 400:
            #Coalicion plataformas
            if (y == 450 or y == 360 or y == 250):
                break
            y+=5
            Mariolas.destroy()
            Mariolas = Label(master, image=Mario)
            Mariolas.place(x=x, y=y)
            canvas.update()
            master.after(5)
            Limt+=10
        sal=False
    master.after(50,bajarplat)

def MoveTurtle(): #Como su nombre lo indica, mover en este caso el enemigo(tortuga)
    global x1,Kupa,sal,y1
    x1-= 5
    y1+=0
    Kupa.destroy()
    Kupa = Label(master, image = Koopa)
    Kupa.place(x = x1,y= y1)
    
##    print(x1,y1)
    if x1 < 0:
            x1 = 900
            Kupa.destroy()
            Kupa = Label(master, image = Koopa)
            Kupa.place(x = x1,y= y1)
            canvas.update()
    master.after(90,MoveTurtle)
    if ((y1 == 130 and(x1 < 600 and x1 > 300))or((y1 == 335 and (x1 >390 and x1 < 610))or(y1 == 230 and ((x1 >150 and x1 < 250)or(x1 >750 and x1 < 850))))):
        Limt = 0
        y1+=5
        while Limt < 400:
            if (y1 == 450 or y1 == 335 or y1 == 230):
                break
            y1+=5
            Kupa.destroy()
            Kupa = Label(master, image = Koopa)
            Kupa.place(x = x1,y= y1)
            canvas.update()
            master.after(5)
            Limt+=10
            if y1 == 440 and x1 < 0:
                x1 = 850
                y1 = 130
                Kupa.destroy()
                Kupa = Label(master, image = Koopa)
                Kupa.place(x = x1,y= y1)
                canvas.update()
        master.after(90,MoveTurtle)
    


    


canvas.bind("<Key>",Move)
canvas.focus_set()

bajarplat()  
MoveTurtle()
iniciar()

master.mainloop()
