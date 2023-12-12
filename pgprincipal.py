import funcoesip
arq=open('teste.txt','r')
reg=arq.readlines()
arq.close()
print(funcoesip.acharipv4(reg))
print(funcoesip.acharipv6(reg))
print(funcoesip.adaptador(reg))
print(funcoesip.mascara(reg))
print(funcoesip.gateway(reg))
