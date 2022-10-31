from ast import Break
import string
import traceback


Artistas = [["Norah Jones", "Don't Know Why"],["Norah Jones", "Come Away with Me "],["Norah Jones", "I loved you"]],

#Lista de Letras

Letras = [["I waited till I saw the sun I don't know why I didn't come  I left you by the house of fun  I don't know why I didn't come  I don't know why I didn't come  When I saw the break of day  I wished that I could fly away"],["Instead of kneeling in the sand  Catching teardrops in my hand  My heart is drenched in wine  But your be on my mind  Forever"]],


#elegir canciones

def elecciones():
  eleccion = 1
  while eleccion != 0:
    try: 
        eleccion = int(input("Ingresa la opción deseada: ? \n 1- Ver la lista de canciones? \n 2- Ver la letra de las canciones? \n 3- Agregar canción: \n 4- Borrar  canción?\n 5- Volver a preguntar \n 6-Buscar por lista \n 0-Finalizar \n : "))
    
        if eleccion == 1:
          elegirCancion()
        if eleccion == 2:
          seleccionarletra()
        if eleccion == 3:
          agregarcancion()
        if eleccion == 4:
          borrarcancion()
        if eleccion == 5:
          elecciones()
        if eleccion == 6:
          buscarnombre()  
              
    except:
      traceback.print_exc()
      print("Error elegir una opción:")
      eleccion = int(input("1- ¿Nueva canción? \n 2- Cerrar el programa \n:"))
      if eleccion == 1:
        elecciones()
      if eleccion == 2:
        print("-----------------Fin-------------------")
              
#Lista de canciones

def elegirCancion():
    print("¿Qué canción querés elegir?\n")
    for i in Artistas:
        print(Artistas.index(i)+1, "-" , i[0], ", " , i[1] )
    elecciones() 

#Funcion para seleccionar la letra de la cancion

def seleccionarletra():
    letra = int(input("que letra querés leer?: "))
    print(Letras[letra-1])

#Función para agregar canción

def agregarcancion():
    eleccion = input("Agregar nombre de la banda y cancion: ")
    eleccion2 = ingresarletra()
    Artistas.append(eleccion)
    print("Cancion Agregada")
    elecciones()
    
#Función para borrar
    
def borrarcancion():
    eleccion = int(input("¿Que canción deseas eliminar?: "))
    del Artistas[eleccion - 1]
    print("\nCanción eliminada\n")
    elecciones()

#buscar por Nombre

def buscarnombre():
    eleccion = (input("Cuál queres buscar?: "))
    for i in Artistas:
      if eleccion in i:
        print("es la opcion número:", i)
      else:
        print("no se encuentra")

#Funcion para ingresar letra

def ingresarletra():
    eleccion = ""
    print("Ingresa la letra de la canción, s para terminar")
    letra = input()
    while eleccion != "s" and eleccion != "S":
        eleccion = eleccion + "\n" + letra
        eleccion = input("Ingrese nueva línea, s para terminar\n")
        Letras.append(letra)
    return eleccion

elecciones()
