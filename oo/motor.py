class Motor:
    velocidade = 0

    def acelerar (self):
        self.velocidade += 1

    def frear (self):
        self.velocidade = self.velocidade - 2 if self.velocidade >= 2 else 0


if __name__ == '__main__':
    motor = Motor()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    motor.acelerar()
    motor.acelerar()
    motor.acelerar()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
