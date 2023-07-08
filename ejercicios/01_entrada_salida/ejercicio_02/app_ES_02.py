import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: entrada_salida_02
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un dato utilizando el Dialog Prompt
y luego mostrarlo utilizando el Dialog Alert
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
       #DEFINE EL BOTON
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        #SE EJECUTA ESTO
    def btn_mostrar_on_click(self):
        #DEFINO EL INPUT DEL USUARIO CON PROMPT
        nombre_alumno=  prompt("INGRESE","INGRESE NOMBRE ALUMNO: ") # Pido que en el alert, en vez de mostrarme un nombree me muestre la ventana que pide el dato
        #SE EJECUTA ESTA FUNCIÓN, CON LA VARIABLE nombre_alumno QUE AL SER UNA FUNCION, SE EJECUTA ESTA
        #E INGRESO POR PROMPT EL NOMBRE DEL ALUMNO
        #alert("Titulo","el nombre del alumno es" + nombre_alumno)-->Son alerts equivalentes
        #alert("Titulo","el nombre del alumno es{0}".format(nombre_alumno)-->Son alerts equivalentes
        alert("Titulo",f"el nombre del alumno es {nombre_alumno}")
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()