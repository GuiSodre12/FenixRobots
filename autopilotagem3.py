from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
motorDireita = Motor(Port.A) #tacerto
motorEsquerda = Motor(Port.E, Direction.COUNTERCLOCKWISE) #tacerto
motorAnexoDir = Motor(Port.C) #tacerto
motorAnexoEsq = Motor(Port.F) #tacerto

#distanciaEmCm = (distancia / 360) * 5.6
    #distancia = (distanciaEmCm * 360) / 17.5


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
                        #wait(10)
                        motorEsquerda.run(-50)
                        motorDireita.run(50)
    motorDireita.brake()
    motorEsquerda.brake()   


def autopilotagem(setpoint, distanciaEmCm, velocidade, kp, kd):
    #movimentacao do robo
    hub.imu.reset_heading(0)
    motorDireita.reset_angle(0)
    motorEsquerda.reset_angle(0)
    
    motorDireitaAngulo =  ((motorDireita.angle() / 360) * 17.58)
    motorEsquerdaAngulo = ((motorEsquerda.angle() / 360) * 17.58)
    movimentacaoDoRobo =  (motorDireitaAngulo + motorEsquerdaAngulo) / 2
    ultimoerro = 0

    while movimentacaoDoRobo < distanciaEmCm:
        print("ta dentro do while")
        motorDireitaAngulo =  ((motorDireita.angle() / 360) * 17.58)
        motorEsquerdaAngulo = ((motorEsquerda.angle() / 360) * 17.58)
        movimentacaoDoRobo =  (motorDireitaAngulo + motorEsquerdaAngulo) / 2
        print(movimentacaoDoRobo)
        #erro
        erro = setpoint - hub.imu.heading()
        proporcional = erro * kp
        print(f"O primeiro erro foi{erro}")
        deltaE = erro - ultimoerro
        derivada = deltaE * kd

        if movimentacaoDoRobo >= (distanciaEmCm * 0.8):
            print("lentinho")
            motorEsquerda.run((velocidade / 2) + (proporcional + derivada))
            motorDireita.run((velocidade / 2) - (proporcional + derivada))
        else:
            motorEsquerda.run(velocidade + (proporcional + derivada))
            motorDireita.run(velocidade - (proporcional + derivada))

        #ultimo erro
        ultimoerro = erro

    #print("acabou o while")
    motorDireita.brake()
    motorEsquerda.brake()
    #graus * cm *360 / circ
autopilotagem(0, 20, 500, 9, 8)
curva (-90)
autopilotagem(0, 20, 500, 9, 8)
