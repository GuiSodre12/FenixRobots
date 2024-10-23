from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
motorDireita = Motor(Port.A) #tacerto
motorEsquerda = Motor(Port.E, Direction.COUNTERCLOCKWISE) #tacerto
motorAnexoDir = Motor(Port.B)
motorAnexoEsq = Motor(Port.F)

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
        motorEsquerda.run(250)
        motorDireita.run(-250)
        
        while abs(hub.imu.heading()) < valorAlvo or abs(hub.imu.heading()) == valorAlvo:

                if abs(hub.imu.heading()) > abs(valorAlvo - 30):
                        wait(10)
                        motorEsquerda.run(100)
                        motorDireita.run(-100)
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

            velocidadeMinima = 200
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
    
    kp = 15
    kd = 13.052884615384615


    verificacao = 1
    if distanciaEmCm < 0:
        verificacao = -1

        
    #eror
    ultimoerro = 0
    percursoTotalDcc = 10
    percursoTotal = abs(distanciaEmCm)
    while movimentacaoDoRobo < abs(distanciaEmCm):
        
        
        

        velocidadeMinima = 46
        #Movimentação do robo
        motorDireitaAngulo =  ((abs(motorDireita.angle()) / 360) * 17.58)
        motorEsquerdaAngulo = ((abs(motorEsquerda.angle()) / 360) * 17.58)
        movimentacaoDoRobo =  (motorDireitaAngulo + motorEsquerdaAngulo) / 2
        percursoFeito = movimentacaoDoRobo

        percursoFeitoDcc = percursoFeito - (percursoTotal - percursoTotalDcc)

        #PID
        erro = setpoint - hub.imu.heading()
        proporcional = erro * kp
        deltaE = erro - ultimoerro
        derivada = deltaE * kd
        correcao = (proporcional + derivada)


        velocidade = (abs(velocidadeInicial) - ((percursoFeitoDcc / percursoTotalDcc) * abs(velocidadeInicial)) )
        print(f"percursoFeitoDcc: {percursoFeitoDcc} percursoTotalDcc: {percursoTotal}")
        if movimentacaoDoRobo < abs(distanciaEmCm) - percursoTotalDcc:
            velocidade = abs(velocidadeInicial)
            

        if abs(velocidade) < velocidadeMinima:
            velocidade = velocidadeMinima

        motorDireita.run((velocidade * verificacao) - correcao )
        motorEsquerda.run((velocidade * verificacao) + correcao )
        print(f"velocidade: {velocidade}, percursoFeito: {percursoFeito}")
        #ultimo erro
        ultimoerro = erro


autopilotagem(0, -53, 900)
autopilotagem(0, -3, 800)
motorAnexoDir.run_time(9200, 500)
autopilotagem(0, 10000, 1000)