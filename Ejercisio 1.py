class Paciente:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
        self.doctor = None

    def asignar_doctor(self, doctor):
        self.doctor = doctor
        doctor.agregar_paciente(self)

    def mostrar_info(self):
        if self.doctor:
            return f"Paciente(nombre={self.nombre}, id={self.id}, doctor={self.doctor.nombre})"
        else:
            return f"Paciente(nombre={self.nombre}, id={self.id}, doctor=N/A)"


class Doctor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
        self.pacientes = []

    def agregar_paciente(self, paciente):
        if paciente not in self.pacientes:
            self.pacientes.append(paciente)

    def eliminar_paciente(self, paciente):
        if paciente in self.pacientes:
            self.pacientes.remove(paciente)

    def mostrar_info(self):
        lista_pacientes = [p.nombre for p in self.pacientes]
        return f"Doctor(nombre={self.nombre}, especialidad={self.especialidad}, pacientes={lista_pacientes})"



if __name__ == "__main__":
    doctor = Doctor("Dr. Maristany", "Traumatologia")
    paciente1 = Paciente("Emanuel Gomez", 1)
    paciente2 = Paciente("Ana Guevara", 2)

    paciente1.asignar_doctor(doctor)
    paciente2.asignar_doctor(doctor)

    print(doctor.mostrar_info())
    print(paciente1.mostrar_info())
    print(paciente2.mostrar_info())










