from tkinter import *
from PIL import ImageTk,Image
import random
root=Tk()
root.geometry("300x300")
root.configure(background="yellow")
root.title("Endless pokemon game")

img=ImageTk.PhotoImage(Image.open("button.jpg"))

abra=ImageTk.PhotoImage(Image.open("abra.jpg"))
bulbasour=ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
charmender=ImageTk.PhotoImage(Image.open("charmender.jpg"))
lyvasour=ImageTk.PhotoImage(Image.open("Iyvasour.jpg"))
jigglypuff=ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
kadabra=ImageTk.PhotoImage(Image.open("kadabra.jpg"))
meowth=ImageTk.PhotoImage(Image.open("meowth.jpg"))
nidoking=ImageTk.PhotoImage(Image.open("nidoking.jpg"))
paras=ImageTk.PhotoImage(Image.open("paras.jpg"))
persion=ImageTk.PhotoImage(Image.open("persion.jpg"))
pikachu=ImageTk.PhotoImage(Image.open("pikachu.jpg"))
ratata=ImageTk.PhotoImage(Image.open("ratata.jpg"))
squirtle=ImageTk.PhotoImage(Image.open("squirtle.jpg"))

name = [abra,bulbasour,charmender,lyvasour,jigglypuff,kadabra,meowth,nidoking,paras,persion,pikachu,ratata,squirtle]
power_list =[30,60,50,100,70,70,60,90,40,70,200,40,50]


labelplayer1= Label(root,text="Player1",bg="red",fg="white")
labelplayer1.place(relx=0.1,rely=0.3,anchor=CENTER)
labelplayer2= Label(root,text="Player2",bg="red",fg="white")
labelplayer2.place(relx=0.8,rely=0.3,anchor=CENTER)    

label1score= Label(root,bg="blue",fg="black")
label1score.place(relx=0.1,rely=0.10,anchor=CENTER)
label2score= Label(root,bg="blue",fg="black")
label2score.place(relx=0.8,rely=0.10,anchor=CENTER)

player2=0
player1=0

def btn1():
    global player1
    ranndom1= random.randint(0,12)
    random_pokemon = name[random1]
    labeldisplay["image"]= random_pokemon
    randompower=power_list[random1]
    player1=player1+randompower
    label1score["text"]=str(player1)
    
def btn2():
    global player2  
    random2 = random.randint(0,12)
    random2_pokemon = name[random2]
    labeldisplay["image"]=random2_pokemon
    random2power=power_list[random2]
    player2=player2+random2power
    label2score["text"]=str(player2)

labeldisplay= Label(root)
labeldisplay.place(relx=0.4,rely=0.5,anchor=CENTER)

btn1= Button(root,image=img,command=btn1)
btn1.place(relx=0.1,rely=0.5,anchor=CENTER)

btn2= Button(root,image=img,command=btn2)
btn2.place(relx=0.8,rely=0.5,anchor=CENTER)
root.mainloop()


