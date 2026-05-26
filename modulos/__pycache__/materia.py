class datos_materia:    
    def __init__(self, ID_materia, nombre_materia, Usuario_asignado): #el usuario asignado quiere decir quien imparte la materia o quien esta a cargo de ella.
        self.ID_materia= ID_materia
        self.nombre_materia = nombre_materia
        self.Usuario_asignado= Usuario_asignado 
    def mostrar_MATERIA(self):
        print ("ID_materia:", self.ID_materia)
        print("nombre_materia:", self.nombre_materia)
        print("Usuario_asignado: ", self.Usuario_asignado)