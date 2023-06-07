from data_stark import *
from funciones import *
import os

flag_seguir = True

while flag_seguir:
    os.system("cls") #se limpia la consola
    print("-------------------------------------")
    y = stark_marvel_app_3(lista_personajes)
    if y == "s":
        flag_seguir = False
                
    os.system("Pause")
        
