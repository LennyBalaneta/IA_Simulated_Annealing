"""
Algoritmo Simulated Annealing
CCT Udesc
IAR
Marcos Balatka
"""
import os, random, math


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
        
    return p, int(linhas[7].split()[2])

def decTemperatura(t):#decaimento da temperatura
    return t - 0.01
    
def energia(prob, resp):
    e = 0
    for clausula in prob:
        if clausula[0] < 0 and resp[-clausula[0] - 1] == 0 or clausula[0] >= 0 and resp[clausula[0] - 1] == 1:#prep 1
            p0 = 1
        else:
            p0 = 0
        
        if clausula[1] < 0 and resp[-clausula[1] - 1] == 0 or clausula[1] >= 0 and resp[clausula[1] - 1] == 1:#prep 2
            p1 = 1
        else:
            p1 = 0
            
        if clausula[2] < 0 and resp[-clausula[2] - 1] == 0 or clausula[2] >= 0 and resp[clausula[2] - 1] == 1:#prep 3
            p2 = 1
        else:
            p2 = 0         

        #print("p0=", p0, " p1=", p1, " p2=", p2)
        if p0 == 1 or p1 == 1 or p2 == 1:#or
            e += 1
    return (91 - e)*10

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
    entrada = "uf20-01.cnf"
    problema, tamanho = readFile(entrada)
    resposta = []
    for i in range(tamanho):
        resposta += [random.randint(0, 1)]

    t0 = 50#temperatura inicial
    tf = 0#temperatura final

    temperatura = t0
    candidato = resposta
    ener = energia(problema, candidato)

    #loop principal
    while temperatura > tf and  ener != 0:
        #print("Temperatura=", temperatura, "Energia=", 1/ener)
        novoCandidato = geraCandidato(candidato)
        nEner = energia(problema, novoCandidato)
        delta = nEner - ener
        print("Temperatura=", temperatura, "Energia=", ener)
        if delta <= 0:
            candidato = novoCandidato
            ener = nEner
        else:
            if random.random() < pow(math.e, -delta/temperatura):
                candidato = novoCandidato
                ener = nEner
        temperatura = decTemperatura(temperatura)
        
    print("Resposta=", candidato, " | Energia=", ener, " | Minimo global=", 0)











































