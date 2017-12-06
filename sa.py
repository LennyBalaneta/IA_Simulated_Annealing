"""
Algoritmo Simulated Annealing
CCT Udesc
IAR
Marcos Balatka
"""
import os, random, math

#parametros
entrada = "uf250-01.cnf"
t0 = 70#temperatura inicial
tf = 0.01#temperatura final

maxIt = 500000#quantidade maxima de iteracoes
txDecT = 0.0001

def clear():
    os.system("cls")

def readFile(entrada):#ler entrada
    f = open(entrada, "r+")
    linhas = f.readlines()
    inicioClausulas = 8#linha que começa as clausulas
    fimClausulas = inicioClausulas + int(linhas[7].split()[3])#linha que termina
    p = []#problema
    for i in range(inicioClausulas, fimClausulas):
        p += [linhas[i].split()[0:3]]
    
    for i in range(len(p)):
        for j in range(3):
            p[i][j] = int(p[i][j])
        
    return p, int(linhas[7].split()[2]), int(linhas[7].split()[3])

def decTemperatura(t):#decaimento da temperatura
    return t * (1 - txDecT)
    
def energia(prob, resp, qtdC):
    e = 0
    for clausula in prob:
        if clausula[0] < 0 and resp[(-clausula[0]) - 1] == 0 or clausula[0] >= 0 and resp[clausula[0] - 1] == 1:#prep 1
            p0 = 1
        else:
            p0 = 0
        
        if clausula[1] < 0 and resp[(-clausula[1]) - 1] == 0 or clausula[1] >= 0 and resp[clausula[1] - 1] == 1:#prep 2
            p1 = 1
        else:
            p1 = 0
            
        if clausula[2] < 0 and resp[(-clausula[2]) - 1] == 0 or clausula[2] >= 0 and resp[clausula[2] - 1] == 1:#prep 3
            p2 = 1
        else:
            p2 = 0         

        #print("p0=", p0, " p1=", p1, " p2=", p2)
        if p0 == 1 or p1 == 1 or p2 == 1:#or
            e += 1
    return (qtdC - e)

def geraCandidato(c):
    nC = []
    for i in c:
        nC += [i]
    for j in range(1):
        p = random.randint(0, len(c))
        if nC[p - 1] == 1:
            nC[p - 1] = 0
        else:
            nC[p - 1] = 1
            
    #print("novo Candidato:", nC)
    return nC

    
def sa():
    global problema, tamanho, qtdC
    
    problema, tamanho, qtdC = readFile(entrada)
    resposta = []
    for i in range(tamanho):
        resposta += [random.randint(0, 1)]

    temperatura = t0
    iteracoes = 0
    candidato = resposta
    ener = energia(problema, candidato, qtdC)
    print("Candidado inicial: ", candidato, " Energia inicial: ", ener)
    
    #loop principal
    while temperatura > tf and  ener != 0 and iteracoes < maxIt:
        novoCandidato = geraCandidato(candidato)
        nEner = energia(problema, novoCandidato, qtdC)
        delta = nEner - ener
        if delta <= 0:
            candidato = novoCandidato
            ener = nEner
        else:
            #print("chance=", pow(math.e, -delta/temperatura))
            if random.random() < math.exp(-delta / temperatura):
                candidato = novoCandidato
                ener = nEner
        temperatura = decTemperatura(temperatura)
        iteracoes += 1
        if(iteracoes % 100 == 0):
            print("Temperatura= %.5f" % temperatura, "\tEnergia= ", ener, "\tIteracao= ", iteracoes)
        
    print("Resposta=", candidato, " | Energia=", ener, " | Minimo global=", 0)











































