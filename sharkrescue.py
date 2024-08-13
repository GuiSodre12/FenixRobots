import main.py
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

#Declarando o tipo de hub
hub = PrimeHub()
#Declarando os motores
motorGarra = Motor(Port.F, positive_direction=Direction.CLOCKWISE)
motorEsquerda = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
motorDireita = Motor(Port.D, positive_direction=Direction.CLOCKWISE)
#Declarando quais motores compõem o par dos motores de movimento
motoresDeMovimento = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=96)

#---MISSÃO---
andar(50, 3)
curva(-45, 20)
garra(-25, 20)
garra(0, 20) #Voltar a garra
curva(90, 20) #Virar
andar(50, 3)  # Voltar pra base
