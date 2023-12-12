def acharipv4(lista):
    ip=[]
    for i in range(len(lista)):
        if ('IPv4' in lista[i]):
            dados = lista[i].split(': ')
            ip.append(dados[1])
    return ip

def acharipv6(lista):
    ip = []
    for i in range (len(lista)):
        if ('IPv6' in lista[i]):
            dados = lista[i].split(': ')
            ip.append(dados[1])
    return ip 

def adaptador(lista):
    adapt=[]
    for i in range (len(lista)):
        if ('Adaptador' in lista[i]):
            dados = lista[i].split(': ')
            adapt.append(dados[0].rstrip(': '))
    return adapt

def mascara(lista):
    masc=[]
    for i in range(len(lista)):
        if ('M scara de Sub-rede' in lista[i]):
            dados = lista[i].split(': ')
            masc.append(dados[1])
    return masc

def gateway(lista):
    gat = []
    for i in range(len(lista)):
        if ('Gateway PadrÆo' in lista[i]):
            dados = lista[i].split(': ')
            gat.append(dados[1])
    return gat
