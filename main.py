from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
motorGarra = Motor(Port.F, positive_direction=Direction.CLOCKWISE)
motorEsquerda = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
motorDireita = Motor(Port.D, positive_direction=Direction.CLOCKWISE)
motoresDeMovimento = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=96)




def curva(anguloAlvo, velocidade):
    

def andar(velocidade, distancia):
 motoresDeMovimento.drive(velocidade, distancia)

def garra(anguloAlvoGarra, potencia):
    motorGarra.run(500)
    wait(1500)
    motorGarra.stop()

    

