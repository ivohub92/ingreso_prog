import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera 
hasta que presione el botón Cancelar (en el prompt). 
Luego determinar el máximo y el mínimo 
e informarlos en los cuadros de textos txt_maximo y txt_minimo respectivamente

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.txt_minimo = customtkinter.CTkEntry(
            master=self, placeholder_text="Mínimo")
        self.txt_minimo.grid(row=0, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(
            master=self, placeholder_text="Máximo")
        self.txt_maximo.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")

    def btn_comenzar_ingreso_on_click(self):
    
        numero_max= None
        numero_min= None
        contador=0
        bandera= True
        
        while bandera == True:
            numero= prompt("UTN", "INGRESE NUMERO")

            if numero == None:  #si apreto cancelar, que salga el programa
                break

            while (numero == None) or (numero.isdigit() == False):   #ojo que si pones al reves las condiciones, falla. importa el orden en este caso
                numero= prompt("UTN", "ERROR INGRESE NUMERO")
                
            numero = int(numero)

            if  (numero_max == None) or (numero_max < numero):
                numero_max = numero

            if  (numero_min == None) or (numero_min > numero):
                numero_min = numero
        

        self.txt_minimo.delete(0,tkinter.END)
        self.txt_maximo.delete(0,tkinter.END)
        self.txt_maximo.insert(0,numero_max)
        self.txt_minimo.insert(0,numero_min)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
