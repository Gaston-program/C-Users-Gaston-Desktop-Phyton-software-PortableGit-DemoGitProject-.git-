class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.facultades = []

    def agregar_facultad(self, facultad):
        if isinstance(facultad, Facultad):
            self.facultades.append(facultad)


class Facultad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carreras = []

    def agregar_carrera(self, carrera):
        if isinstance(carrera, Carrera):
            self.carreras.append(carrera)




class Carrera:
    def __init__(self, nombre):
        self.nombre = nombre





if __name__ == "__main__":

    carrera1 = Carrera("Ingeniería en Sistemas")
    carrera2 = Carrera("Medicina")


    facultad1 = Facultad("Facultad de Ingeniería")
    facultad2 = Facultad("Facultad de Medicina")


    facultad1.agregar_carrera(carrera1)
    facultad2.agregar_carrera(carrera2)


    universidad = Universidad("Universidad Nacional")


    universidad.agregar_facultad(facultad1)
    universidad.agregar_facultad(facultad2)


    print(f"Universidad: {universidad.nombre}")
    for fac in universidad.facultades:
        print(f"  Facultad: {fac.nombre}")
        for car in fac.carreras:
            print(f"    Carrera: {car.nombre}")