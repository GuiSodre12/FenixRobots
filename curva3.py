from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.parameters import Port
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction
from pybricks.parameters import Axis

hub = PrimeHub()
motorEsquerda = Motor(Port.C, Direction.COUNTERCLOCKWISE)
motorDireita = Motor(Port.F, Direction.CLOCKWISE)




def curva(angulo):  
 if hub.imu.ready():
    print("COMEÇA AGORA")
    velocidade = 150  #eu vou usar isso quando funcionar eu acho
    valorInicial = abs(hub.imu.rotation(Axis.Z))
    valorAlvo = valorInicial + abs(angulo)
    #hub.imu.reset_heading(0)
    print(abs(hub.imu.rotation(Axis.Z)))
    
    if angulo > 0:
        #iniciar movimentos esquerda
        motorEsquerda.run(150)
        motorDireita.run(-150)
        print(abs(hub.imu.rotation(Axis.Z)))
        
        while abs(hub.imu.rotation(Axis.Z)) < valorAlvo or abs(hub.imu.rotation(Axis.Z)) == valorAlvo:
                wait(100)
                print(abs(hub.imu.rotation(Axis.Z)))
                wait(30)
                if abs(hub.imu.rotation(Axis.Z)) > abs(valorAlvo - 30):
                        wait(10)
                        motorEsquerda.run(50)
                        motorDireita.run(-50)
    if angulo < 0:
        #iniciar movimentos esquerda
        motorEsquerda.run(-150)
        motorDireita.run(150)
        print(abs(hub.imu.rotation(Axis.Z)))
        
        while (abs(hub.imu.rotation(Axis.Z)) * -1) > (valorAlvo * -1) or (abs(hub.imu.rotation(Axis.Z)) * -1) == (valorAlvo * -1):
                print(abs(hub.imu.rotation(Axis.Z)))
                if (abs(hub.imu.rotation(Axis.Z)) * -1) > (abs((valorAlvo) - 30) * -1):
                        wait(10)
                        motorEsquerda.run(-50)
                        motorDireita.run(50)
    motorDireita.brake()
    motorEsquerda.brake()   



curva(90)

    