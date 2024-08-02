from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from PIL import Image, ImageTk # importando Pillow
import random

# Cores usadas no programa --------------------------------------------------

co0 = "#111111"  # Preta
co1 = "#ffffff"  # Branca
co2 = "#afef6f"  # Verde Claro
co3 = "#437828"  # Verde Escuro
co4 = "#dfbdb1"  # Rosa
co5 = "#162a58"  # Azul Escuro
co6 = "#38576b"  # Azul
co9 = "#403d3d"  # Letra

# Criando a janela -----------------------------------------------------------

janela = Tk()
janela.title("Jogo das Lâmpadas")
janela.geometry('400x290')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

# Criando Frames -----------------------------------------------------------

frame_cima = Frame(janela, width=500, height=50, bg=co5)
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=500, height=235, bg=co6)
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Criando Frame cima ----------------------------------------------

l_app = Label(frame_cima, text="Jogo: Acenda todas as lâmpadas!", anchor=NE, font=("Ivy 15 bold"), bg=co5, fg=co1)
l_app.place(x=40, y=10)

# Criando Frame baixo ---------------------------------------------

img_lampada_off = Image.open("0.png")
img_lampada_off = img_lampada_off.resize((110, 100), Image.Resampling.NEAREST)
img_lampada_off = ImageTk.PhotoImage(img_lampada_off)

img_lampada_on = Image.open("1.png")
img_lampada_on = img_lampada_on.resize((110, 100), Image.Resampling.NEAREST)
img_lampada_on = ImageTk.PhotoImage(img_lampada_on)

img_2 = Image.open("2.png")
img_2 = img_2.resize((40, 40), Image.Resampling.NEAREST)
img_2 = ImageTk.PhotoImage(img_2)

img_3 = Image.open("3.png")
img_3 = img_3.resize((40, 40), Image.Resampling.NEAREST)
img_3 = ImageTk.PhotoImage(img_3)

img_4 = Image.open("4.png")
img_4 = img_4.resize((40, 40), Image.Resampling.NEAREST)
img_4 = ImageTk.PhotoImage(img_4)

img_5 = Image.open("5.png")
img_5 = img_5.resize((40, 40), Image.Resampling.NEAREST)
img_5 = ImageTk.PhotoImage(img_5)

l_img = Label(frame_baixo, image=img_2, bg=co6)
l_img.place(x=30, y=15)

l_estado = Label(frame_baixo, text="Estou com medo!", anchor=NW, font=("Ivy 15"), bg=co6, fg=co1)
l_estado.place(x=80, y=20)

global control


def ligarLampada(i):
    global control
    lista = i

    # Desabilitando o botão que for clicado.
    if lista[1] == "Interruptor 1":
        b_interruptor_1["state"] = "disable"
    elif lista[1] == "Interruptor 2":
        b_interruptor_2["state"] = "disable"    
    elif lista[1] == "Interruptor 3":
        b_interruptor_3["state"] = "disable"        
    elif lista[1] == "Interruptor 4":
        b_interruptor_4["state"] = "disable"
    else:
        b_interruptor_5["state"] = "disable"

    def substituirValor(i):
        global control
        nova_lista = []
        
        for string in control:
            novo_valor = string.replace(i[0], i[1])
            nova_lista.append(novo_valor)

        control = nova_lista

    # Selecionar valor aleatóriamente
    valor_selecionado = random.sample(lista[0], 1)[0]

    if int(valor_selecionado) == 1:
        if control[0] == "lampada_1":
            l_img_1["image"] = img_lampada_on
            l_img["image"] = img_3
            l_estado["text"] = "Acendeu uma, obrigado!"
            substituirValor(["lampada_1", str(1)])
        else:
            if control[1] == "lampada_2":
                l_img_2["image"] = img_lampada_on
                l_img["image"] = img_4
                l_estado["text"] = "Acendeu a segunda, falta uma!"
                substituirValor(["lampada_2", str(2)])
            else:
                if control[2] == "lampada_3":
                    l_img_3["image"] = img_lampada_on
                    l_img["image"] = img_5
                    l_estado["text"] = "MUUUUITO OBRIGADO!"
                    substituirValor(["lampada_3", str(3)])


control = ["lampada_1", "lampada_2", "lampada_3"]

l_img_1 = Label(frame_baixo, image=img_lampada_off, bg=co6)
l_img_1.place(x=2, y=80)

l_img_2 = Label(frame_baixo, image=img_lampada_off, bg=co6)
l_img_2.place(x=90, y=80)

l_img_3 = Label(frame_baixo, image=img_lampada_off, bg=co6)
l_img_3.place(x=180, y=80)

lista = [0, 1, 0, 1, 0]

b_interruptor_1 = Button(frame_baixo, command=lambda i=[lista, "Interruptor 1"]:ligarLampada(i), text="Interruptor 1", anchor=NW, font=("Ivy 12"), bg=co6, fg=co1)
b_interruptor_1.place(x=290, y=50)

b_interruptor_2 = Button(frame_baixo, command=lambda i=[lista, "Interruptor 2"]:ligarLampada(i), text="Interruptor 2", anchor=NW, font=("Ivy 12"), bg=co6, fg=co1)
b_interruptor_2.place(x=290, y=85)

b_interruptor_3 = Button(frame_baixo, command=lambda i=[lista, "Interruptor 3"]:ligarLampada(i), text="Interruptor 3", anchor=NW, font=("Ivy 12"), bg=co6, fg=co1)
b_interruptor_3.place(x=290, y=120)

b_interruptor_4 = Button(frame_baixo, command=lambda i=[lista, "Interruptor 4"]:ligarLampada(i), text="Interruptor 4", anchor=NW, font=("Ivy 12"), bg=co6, fg=co1)
b_interruptor_4.place(x=290, y=155)

b_interruptor_5 = Button(frame_baixo, command=lambda i=[lista, "Interruptor 5"]:ligarLampada(i), text="Interruptor 5", anchor=NW, font=("Ivy 12"), bg=co6, fg=co1)
b_interruptor_5.place(x=290, y=190)

janela.mainloop()