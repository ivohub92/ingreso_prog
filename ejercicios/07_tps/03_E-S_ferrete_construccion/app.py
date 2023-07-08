import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''

nombre: Iván
apellido: Ramunda

Enunciado:

2.	El departamento de Construcción Rural requiere una herramienta que facilite el calculo de materiales necesarios 
a la hora de realizar un alambrado permetral, se le solicita al usuario que ingrese el ancho y el largo del terreno.

    A. Informar los metros cuadrados del terreno y los metros lineales del perimetro
    B. Informar la cantidad de postes de quebracho Grueso de 2.4 mts (van cada 250 mts lineales y en las esquinas).
    C. Informar la cantidad de postes de quebracho Fino de 2.2 mts (van cada 12 mts lineales, si en es lugar no se encuentra el poste grueso).
    D. Informar la cantidad de varillas (van cada 2 mts lineales).
    E. Informar la cantidad de alambre alta resistencia 17/15 considerando 7 hilos.

    EJ 36 MTS X 24 MTS 
    (G)Poste Quebracho Grueso de 2.4 mts
    (F)Poste Quebracho Fino de 2.2 mts
    (v)Varillas
    
    G V V V V V F V V V V V F V V V V V G
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    F                                   F
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    G V V V V V F V V V V V F V V V V V G
    
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Largo")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_largo = customtkinter.CTkEntry(master=self)
        self.txt_largo.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Ancho")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)

        self.txt_ancho = customtkinter.CTkEntry(master=self)
        self.txt_ancho.grid(row=1, column=1)

        self.btn_calcular = customtkinter.CTkButton(
            master=self, text="CALCULAR", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=3, pady=10, columnspan=2, sticky="nsew")

    def btn_calcular_on_click(self):
        largo = self.txt_largo.get()
        ancho = self.txt_ancho.get()
        largo = float(largo)
        ancho = float(ancho)

        perimetro = largo*2 + ancho*2 
        metros_cuadrados = largo * ancho

        postes_gr_lar = (1 + largo//250 - 0**(249//largo)) * 2
        postes_gr_anch = (1 + ancho//250 - 0**(249//ancho)) * 2

        postes_gr= postes_gr_anch + postes_gr_lar

        postes_fin_lar = (largo//12 - 0**(largo%12) - (largo//1500 - 0**(largo%1500))) * 2
        postes_fin_anch = (ancho//12 - 0**(ancho%12) - (ancho//1500 - 0**(ancho%1500))) * 2

        postes_fin = postes_fin_lar + postes_fin_anch

       
        varillas = (largo // 2) * 2 + (ancho // 2) * 2 - postes_gr - postes_fin

        alambre = perimetro*7



        alert("Calculos de terreno",f"Los metros lineales del terreno son {perimetro:.2f} metros.\nLos metros cuadrados son {metros_cuadrados:.2f}.\nSe precisan {postes_gr:.0f} postes anchos y {postes_fin:.0f} postes finos.\nNecesito {varillas:.0f} varillas y {alambre:.0f} metros de alambre")
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
