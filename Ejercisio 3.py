class Procesador:
    def __init__(self,modelo,frecuencia):
        self.modelo = modelo
        self.frecuencia = frecuencia


class RAM:
    def __init__(self,capacidad,tipo):
        self.capacidad = capacidad
        self.tipo = tipo


class DiscoDuro:
    def __init__(self,capacidad,tipo):
        self.capacidad = capacidad
        self.tipo = tipo


class Ordenador:
    def __init__(self,procesador,ram,disco_duro):
        self.procesador = procesador
        self.ram = ram
        self.disco_duro = disco_duro

    def mostrar_infor(self):
        info = (f"Procesador: {self.procesador.modelo}, {self.procesador.frecuencia} GHz\n"
            f"RAM: {self.ram.capacidad} GB, {self.ram.tipo}\n"
            f"Disco Duro: {self.disco_duro.capacidad} GB, {self.disco_duro.tipo}")




