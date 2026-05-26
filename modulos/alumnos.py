class alumno:
    #-------------------------------------------CLASE DE ALUMNOS------------------------------------------------------------------------------
    def __init__(self,Id,nombre,No_control,grupo):
        self.Id= Id
        self.nombre = nombre
        self.No_control = No_control
        self.grupo = grupo
        
    def mostrar_datos(self):
        print ("Id asignado:", self.Id)
        print("nombre: ", self.nombre)
        print("No. control: ", self.No_control)
        print("Grupo:" , self.grupo)