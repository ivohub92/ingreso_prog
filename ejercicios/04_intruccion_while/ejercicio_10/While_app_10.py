import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        contador_positivos=0
        contador_negativos=0
        contador_ceros=0
        bandera=True
        acumulado_pos=0
        acumulado_neg=0
        suma_pos=0
        suma_neg=0
        bandera= True
        numero=0

        while bandera == True:
            numero= prompt("UTN", "INGRESE NUMERO")

            if numero == None:
                break

            while (numero == None) or (numero.isdigit() == False):   #ojo que si pones al reves las condiciones, falla. importa el orden en este caso
                numero= prompt("UTN", "ERROR INGRESE NUMERO")
            
            numero= int(numero)
            if numero>0:
                acumulado_pos= numero + acumulado_pos
                contador_positivos= contador_positivos + 1
            elif numero==0:
                contador_ceros= contador_ceros + 1
            else:
                acumulado_neg= numero + acumulado_neg
                contador_negativos= contador_negativos+1
        
        diferencias_contadores= acumulado_pos - acumulado_neg 

        alert("UTN",f"La suma acumulada de positivos es {acumulado_pos} La de positivos es {acumulado_neg} Hubo {contador_positivos} numeros positivos, {contador_negativos} negativos Y {contador_ceros} ceros ingresados. La diferencia entre numeros positivos y negativos es {diferencias_contadores}")
        





    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
