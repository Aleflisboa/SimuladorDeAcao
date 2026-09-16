class Motor:
    def __init__(self, tipo, cilindrada):
        self.tipo = tipo
        self.cilindrada = cilindrada

    def ligar(self):
        print("Motor ligado.")

    def desligar(self):
        print("Motor desligado.")


class Carro:
    def __init__(self, modelo, cor, motor):
        self.modelo = modelo
        self.cor = cor
        self.motor = motor

    def dirigir(self):
        print(f"Dirigindo o carro {self.modelo} de cor {self.cor}.")
        self.motor.ligar()

    def parar(self):
        print(f"O carro {self.modelo} parou.")
        self.motor.desligar()


motor_do_carro = Motor(tipo="V8", cilindrada=5000)

meu_carro = Carro(modelo="Sedan", cor="Azul", motor=motor_do_carro)

meu_carro.dirigir()
meu_carro.parar()