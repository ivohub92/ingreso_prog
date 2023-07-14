import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera, 
hasta que presione el botón Cancelar (en el prompt) o el usuario ingrese cero. 
Calcular la suma acumulada de los positivos y multiplicar los negativos. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_producto

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_producto = customtkinter.CTkEntry(master=self, placeholder_text="Producto")
        self.txt_producto.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        numero= 1
        acumulador=0
        multiplo=1
        bandera= True
        while bandera == True and numero != 0:
            numero= prompt("UTN", "INGRESE NUMERO")

            if numero == None:  #si apreto cancelar, que salga el programa
                break
            elif numero[0:1] == "-":
                if not numero[1:len(numero)].isdigit():
                    continue
            else:
                while (numero == None) or (numero.isnumeric() == False):   #ojo que si pones al reves las condiciones, falla. importa el orden en este caso
                    numero= prompt("UTN", "ERROR INGRESE NUMERO")
            
            numero= int(numero)
            if numero>0:
                acumulador= numero + acumulador
            else:
                multiplo= numero*multiplo
        
        self.txt_producto.insert(0,multiplo)
        self.txt_suma_acumulada.insert(0,acumulador)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
