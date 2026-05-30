# Librerías para que lea caractreres en español
import os
import sys

os.system("chcp 65001")
sys.stdout.reconfigure(encoding='utf-8')
#----------------------------------------------------------------------
#Impoetación de la carpeta Modulos de los archivos "..." la clase "..."
from Modulos.alumno import Alumno
from Modulos.calificacion import Calificacion
from Modulos.materia import Materia
from Modulos.profesor import Profesor

#Alumno 1 objeto |nombre| No.control|
alumno1 = Alumno("Linn", "2480")

#Profesor 1 objeto |nombre| 
profesor1 = Profesor("Jose")

#Materia 1 objeto |nombre| profesor 1 objeto |
materia1 = Materia("POO", profesor1)

#Calificacion 1           |nombre 1 | materia 1 | promedio|
calificacion1 = Calificacion(alumno1, materia1, 90)

#---------------------IMPRIMIR INFORMACIÓN EN TERMINAL--------------------
print("––––––––––––––––––––––––––––––––––––––––––––––––––––")
print("Alumno:", alumno1.nombre)
print("Matrícula:", alumno1.Nocontrol)
print("––––––––––––––––––––––––––––––––––––––––––––––––––––")
print("Profesor:", profesor1.nombre)
print("Materia asignada:",materia1.nombre)
print("––––––––––––––––––––––––––––––––––––––––––––––––––––")
print("––––––––––––––––––––––––––––––––––––––––––––––––––––")
print("Calificación:", calificacion1.calificacion)
print("––––––––––––––––––––––––––––––––––––––––––––––––––––")