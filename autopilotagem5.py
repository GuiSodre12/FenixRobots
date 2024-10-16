from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
motorDireita = Motor(Port.A) #tacerto
motorEsquerda = Motor(Port.E, Direction.COUNTERCLOCKWISE) #tacerto


#distanciaEmCm = (distancia / 360) * 5.6
    #distancia = (distanciaEmCm * 360) / 17.5


def curva(angulo):  
 if hub.imu.ready():
    hub.imu.reset_heading(0)
    #print("COMEÇA AGORA")
    valorInicial = abs(hub.imu.heading())
    valorAlvo = valorInicial + (angulo)
    
    if angulo > 0:
        #iniciar movimentos direita
        motorEsquerda.run(150)
        motorDireita.run(-150)
        
        while abs(hub.imu.heading()) < valorAlvo or abs(hub.imu.heading()) == valorAlvo:

                if abs(hub.imu.heading()) > abs(valorAlvo - 30):
                        wait(10)
                        motorEsquerda.run(80)
                        motorDireita.run(-80)
    if angulo < 0:
        #iniciar movimentos esquerda

        motorDireita.reset_angle(0)
        motorEsquerda.reset_angle(0)
    
    
        motorDireitaAngulo =  ((motorDireita.angle() / 360) * 17.58)
        motorEsquerdaAngulo = ((motorEsquerda.angle() / 360) * 17.58)
        movimentacaoDoRobo =  (motorDireitaAngulo + motorEsquerdaAngulo) / 2
        percursoTotalDcc = 1
        velocidadeInicial = 500

        while (abs(hub.imu.heading()) * -1 ) > (valorAlvo) or (abs(hub.imu.heading()) * -1) == (valorAlvo):
                
            percursoTotal = valorAlvo
            percursoFeito = movimentacaoDoRobo

            velocidadeMinima = 100
            #Movimentação do robo
            motorDireitaAngulo =  ((motorDireita.angle() / 360) * 17.58)
            motorEsquerdaAngulo = ((motorEsquerda.angle() / 360) * 17.58)
            movimentacaoDoRobo =  (motorDireitaAngulo + motorEsquerdaAngulo) / 2
            
            percursoFeitoDcc = percursoFeito - (percursoTotal - percursoTotalDcc)


            velocidade = (velocidadeInicial - ((percursoFeitoDcc / percursoTotalDcc) * velocidadeInicial))

            if movimentacaoDoRobo < valorAlvo - percursoTotalDcc:
                velocidade = velocidadeInicial

            if velocidade < velocidadeMinima:
                velocidade = velocidadeMinima

            motorEsquerda.run(velocidade * -1)
            motorDireita.run(velocidade)
    motorDireita.brake()
    motorEsquerda.brake()   


def autopilotagem(setpoint, distanciaEmCm, velocidadeInicial):
    #resetar valores
    hub.imu.reset_heading(0)
    motorDireita.reset_angle(0)
    motorEsquerda.reset_angle(0)
    
    
    motorDireitaAngulo =  ((motorDireita.angle() / 360) * 17.58)
    motorEsquerdaAngulo = ((motorEsquerda.angle() / 360) * 17.58)
    movimentacaoDoRobo =  (motorDireitaAngulo + motorEsquerdaAngulo) / 2

    #percurso total e feito
    
    kp = 20
    kd = 4

    #eror
    ultimoerro = 0
    percursoTotalDcc = 1
    while movimentacaoDoRobo < distanciaEmCm:
        
        percursoTotal = distanciaEmCm
        percursoFeito = movimentacaoDoRobo

        velocidadeMinima = 20
        #Movimentação do robo
        motorDireitaAngulo =  ((motorDireita.angle() / 360) * 17.58)
        motorEsquerdaAngulo = ((motorEsquerda.angle() / 360) * 17.58)
        movimentacaoDoRobo =  (motorDireitaAngulo + motorEsquerdaAngulo) / 2
        
        percursoFeitoDcc = percursoFeito - (percursoTotal - percursoTotalDcc)

        #PID
        erro = setpoint - hub.imu.heading()
        proporcional = erro * kp
        deltaE = erro - ultimoerro
        derivada = deltaE * kd
        velocidade = (velocidadeInicial - ((percursoFeitoDcc / percursoTotalDcc) * velocidadeInicial))

        if movimentacaoDoRobo < distanciaEmCm - percursoTotalDcc:
            velocidade = velocidadeInicial

        if velocidade < velocidadeMinima:
            velocidade = velocidadeMinima
        motorDireita.run(velocidade - (proporcional + derivada))
        motorEsquerda.run(velocidade + (proporcional + derivada))
        #ultimo erro
        ultimoerro = erro

autopilotagem(0, 200, 1000)


