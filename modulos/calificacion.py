class calificacion:
    #-------------------------------------------CLASE DE calificaciones----------------------------------------------------------------------------
    def __init__(self,valor,parcial,alumno, materia):
        self.valor = valor 
        self.parcial = parcial
        self.alumno= alumno
        self.materia = materia
        
    def mostrar_calificacion(self):
        print("-----------CALIFICACION--------------------")
        print ("Alumno: ", self.alumno)
        print("Materia: ", self.materia)
        print("Calificación", self.valor)
        print("Parcial:" , self.parcial)