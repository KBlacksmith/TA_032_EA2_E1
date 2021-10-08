from tkinter import Frame, Entry, Label, Button, Tk
from automata import *
def iniciar(frame: Frame, e: Entry, b:Button, miAutomata: Automata): 
    x=20
    y=20
    Label(frame, text="Nombre: ", padx=x, pady=y, font=miAutomata.font).grid(row=0, column=0)
    Label(frame, text=miAutomata.nombre, padx=x, pady=y, font=miAutomata.font).grid(row=0, column=1)
    Label(frame, text="Matricula: ", padx=x, pady=y, font=miAutomata.font).grid(row=1, column=0)
    Label(frame, text=miAutomata.matricula, padx=x, pady=y, font=miAutomata.font).grid(row=1, column=1)
    Label(frame, text="Ingrese una cadena: ", pady=y/2, font=miAutomata.font).grid(columnspan=2)
    e.grid(pady=y, columnspan=2, padx=100)
    b.grid(columnspan=2)
def continuar(resultado: Label, si: Button, no: Button, pregunta: Label, b: Button): 
    b.configure(state="active")
    e.configure(state="normal")
    resultado.configure(text="\n\n\n\n\n\n\n")
    si.destroy()
    no.destroy()
    pregunta.destroy()

def click(e: Entry, resultado: Label, frame: Frame, b: Button, root: Tk):
    cadena=e.get()
    resultado.configure(text=miAutomata.validar0(cadena))
    resultado.grid(columnspan=2)
    e.configure(state='disabled')
    b.configure(state="disabled")
    si = Button(frame, text="Sí", padx=20, font=miAutomata.font)
    no = Button(frame, text="No", padx=20, font=miAutomata.font)
    pregunta = Label(frame, text="¿Desea continuar?", font=miAutomata.font)
    pregunta.grid(columnspan=2)
    si.grid(row= 16,column=0, pady=10)
    no.grid(row=16, column=1, pady=10)

    si.configure(command=lambda: continuar(resultado, si, no, pregunta, b))
    no.configure(command=lambda: root.destroy())

    pass
if __name__=="__main__": 
    miAutomata = Automata()
    root = Tk()
    root.title("TA_032_EA2_E1")
    Label(root, text="Indicaciones: Ingrese una cadena con la siguiente estructura", font=miAutomata.font, pady=10).pack()
    Label(root, text="i(w^n)i((w')^2n)j^2, tal que: ", font=miAutomata.font).pack()
    Label(root, text="w = las iniciales de los apellidos, i = todos los dígitos\nde la matrícula, w' = w inversa, j = el primer nombre,\nn>=1, n no debe leerse", font=miAutomata.font, pady=15).pack()
    Label(root, text='Nota: Todas las letras deben ser minúscula')
    frame = Frame(root)
    frame.pack()
    e=Entry(frame, font=miAutomata.font, width=50)
    resultado = Label(frame, font=miAutomata.font, text="\n\n\n\n\n\n\n")
    b=Button(frame, text="Ingresar cadena", font=miAutomata.font, command=lambda: click(e, resultado, frame, b, root), pady=10, padx=10)
    iniciar(frame, e, b, miAutomata)
    resultado.grid(columnspan=2)
    root.mainloop()