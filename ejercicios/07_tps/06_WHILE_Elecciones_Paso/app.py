'''
Alumno: Ramunda Ivan
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):

        continuar= True
        contador= 0
        bandera_primer_ingreso= False
        nombre= ""
        nombre_min= ""
        edad_min=0
        nombre_max=""
        votos_max=0
        votos_min=0
        acumulado_edad=0
        acumulado_votos=0

        
        while (continuar== True):
            nombre= prompt("UTN","Candidato")
            
            edad= prompt("UTN", "INGRESE EDAD")
            edad= int(edad)

            while (edad<25):

                edad= prompt("UTN", "ERROR INGRESE EDAD VALIDA")
                edad= int(edad)
            

            votos= prompt("UTN", "INGRESE VOTOS")
            votos= int(votos)
            while (votos<=0):
                votos= prompt("UTN", "ERROR INGRESE VOTOS VALIDOS")
                votos= int(votos)
            
            votos= int(votos)
            
            if votos<votos_min or bandera_primer_ingreso== False:
                votos_min= votos
                nombre_min= nombre
                edad_min= edad
                bandera_primer_ingreso= True

            if votos>votos_max :
                votos_max= votos
                nombre_max=nombre
                
                
            contador= contador+1
            acumulado_edad= acumulado_edad + edad
            acumulado_votos= acumulado_votos + votos 

            continuar= question("UTN","desea continuar?")
        
        
        promedio= acumulado_edad/contador
        
        alert("UTN", f"El candidato con mas votos es {nombre_max}\n El de menos votos es {nombre_min} con {edad_min} año.\n El promedio etario es de {promedio} años. El total de votos fue {acumulado_votos} ")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
