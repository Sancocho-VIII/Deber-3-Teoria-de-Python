import math

from tkinter import*


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
numero=60
while True:
    try:
        WORK_MIN = int(input("Cuantos minutos desea que dure una sesion? (pomodoro: 25) "))
        if isinstance(WORK_MIN, int):
            WORK_MIN=WORK_MIN*60
            break
        else:
            print("Ingrese un numero entero")
            continue
    except ValueError:
        print("Ingrese un numero entero")
        continue
while True:
    try:
        SHORT_BREAK_MIN = int(input("Cuantos minutos desea descansar entre sesiones? (pomodoro:5) "))
        if isinstance(SHORT_BREAK_MIN, int):
            SHORT_BREAK_MIN*=60
            break
        else:
            print("Ingrese un numero entero")
            continue
    except ValueError:
        print("Ingrese un numero entero")
        continue

def conteo_regresivo(numero):
    minutes= math.floor(numero/60)
    segundos=numero%60


    if numero>9:
        lienzo.itemconfig(crono,text=f"{minutes}:{segundos}")
    if numero<10:
        lienzo.itemconfig(crono,text=f"{minutes}:{segundos}")
    if numero>0:
        ventana.after(1000,conteo_regresivo,numero-1)
    if numero == 0:
        conteo_regresivo(SHORT_BREAK_MIN)


ventana = Tk()
ventana.config(bg=YELLOW, padx=25, pady=25)
ventana.title("Timer Pomodoro")

nombre = Label(text="Timer")
nombre.config(font=("Courier", 25), bg=YELLOW, fg=GREEN)
nombre.grid(column=1, row=0)

lienzo=Canvas(width=500, height=350, bg=YELLOW, highlightthickness=0)
imagen=PhotoImage(file="tomatones.png")
lienzo.create_image(250,140, image=imagen)
crono=lienzo.create_text(250,200, text="00:00", fill="peru", font=(FONT_NAME,50,"bold"))
lienzo.grid(column=1, row=1)
def button_start():
    ventana.after(0, conteo_regresivo, WORK_MIN)
start = Button(text="Start", command=button_start, font=(FONT_NAME,25,"bold"))
start.grid(column=0,row=2)
Reset = Button(text="Reset", command=button_start, font=(FONT_NAME,25,"bold"))
Reset.grid(column=2,row=2)


ventana.mainloop()