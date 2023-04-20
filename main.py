
import random
allText = []
cartelasS = []
c1 = []
c1t = []
c2 = []
c2t = []
c3 = []
c3t = []
c4 = []
c4t = []
sair = False
seta = '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
sorteados = []
num_disponivel = [i for i in range(1, 51)]
DONO = 1
C1_VENCEU = 1
C2_VENCEU = 2
C3_VENCEU = 3
C4_VENCEU = 4
cont = 0

#Função que sorteia as cartelas
def cartelas():
  with open("cartelas.txt", "r") as file:
    for linha in file:
      allText.append(file.readline().rstrip().split(','))
    for i in range(1, 5):
      cartelasS.append(allText[random.randint(1, 19)])
      if i == 1:
        c1.append(cartelasS[0])
      elif i == 2:
        c2.append(cartelasS[1])
      elif i == 3:
        c3.append(cartelasS[2])
      elif i == 4:
        c4.append(cartelasS[3])
cartelas()
#Função que sorteia um número
def sortear():
    indicie = random.randint(0, len(num_disponivel)-1)
    x = num_disponivel[indicie]
    sorteados.append(x)
    num_disponivel.remove(x)
#Função que transforma a string em inteiro
def trans(x, y):
    for i in range(5):
        x.append(y[0][i].rjust(2))
    return (x)
trans(c1t, c1)
trans(c2t, c2)
trans(c3t, c3)
trans(c4t, c4)
#Função que verifica se alguma cartela foi completada
def GANHOU(a):
  if int(a[0]) in sorteados and int(a[1]) in sorteados and int(a[2]) in sorteados and int(a[3]) in sorteados and int(a[4]) in sorteados:
    return True
  return False

def verificar_ganhador(c1t,c2t,c3t,c4t):
  if GANHOU(c1t) == True:
    return C1_VENCEU
  elif GANHOU(c2t) == True:
    return C2_VENCEU
  elif GANHOU(c3t) == True:
    return C3_VENCEU
  elif GANHOU(c4t) == True:
    return C4_VENCEU
  else:
    return 0
  
#Função que destaca se o número foi encontrado
def destaque(a):
        
        destaque_cartela = "          " if False else '           '
        destaque_0 = "    "
        destaque_1 = "    "
        destaque_2 = "    "
        destaque_3 = "    "
        destaque_4 = "    "
        if int(a[0]) in sorteados:
            destaque_0 = "----"
        if int(a[1]) in sorteados:
            destaque_1 = "----"
        if int(a[2]) in sorteados:
            destaque_2 = "----"
        if int(a[3]) in sorteados:
            destaque_3 = "----"
        if int(a[4]) in sorteados:
            destaque_4 = "----"
        if GANHOU(a)==True:
            destaque_cartela = "********** " if False else '********** '
            destaque_0 = "****"
            destaque_1 = "****"
            destaque_2 = "****"
            destaque_3 = "****"
            destaque_4 = "****"
        print(destaque_cartela, destaque_0, destaque_1, destaque_2, destaque_3, destaque_4,sep=' ')
def cart1():
    destaque(c1t)
    print(
        f'Cartela 1: | {c1t[0]} | {c1t[1]} | {c1t[2]} | {c1t[3]} | {c1t[4]} | ')
    destaque(c1t)
def cart2():
    destaque(c2t)
    print(
        f'Cartela 2: | {c2t[0]} | {c2t[1]} | {c2t[2]} | {c2t[3]} | {c2t[4]} |  ')
    destaque(c2t)
def cart3():
    destaque(c3t)
    print(
        f'Cartela 3: | {c3t[0]} | {c3t[1]} | {c3t[2]} | {c3t[3]} | {c3t[4]} | ')
    destaque(c3t)
def cart4():
    destaque(c4t)
    print(
        f'Cartela 4: | {c4t[0]} | {c4t[1]} | {c4t[2]} | {c4t[3]} | {c4t[4]} |  ')
    destaque(c4t)
def escolha1():
    print('\n')
    cart1()
    print(seta)
    print("\n")
    cart2()
    print("\n")
    cart3()
    print("\n")
    cart4()
    print("\n")
    return ''
def escolha2():
    print('\n')
    cart1()
    print("\n")
    cart2()
    print(seta)
    print("\n")
    cart3()
    print("\n")
    cart4()
    print("\n")
def escolha3():
    print('\n')
    cart1()
    print("\n")
    cart2()
    print("\n")
    cart3()
    print(seta)
    print("\n")
    cart4()
    print("\n")
def escolha4():
    print('\n')
    cart1()
    print("\n")
    cart2()
    print("\n")
    cart3()
    print("\n")
    cart4()
    print(seta)
    print("\n")
def escolhaEnter():
  
  print(
        "\n##########################################################################"
    )
  print(
        f'#                          NÚMERO SORTEADO: {sorteados[cont]}                           #'
    )
  print(
        "##########################################################################"
    )
  if cartela_atual == 1:
    escolha1()
  elif cartela_atual == 2:
    escolha2()
  elif cartela_atual == 3:
    escolha3()
  elif cartela_atual == 4:
    escolha4()
  
cartela_atual = 1
print(escolha1())  #printar a cartela pela primeira vez
def cartela_dono(a):
  if a == 1:
    print(
        "\n##########################################################################"
    )
    print(
        '#                 VOCÊ AGORA É DONO DA CARTELA 1                         #'
    )
    print(
        "##########################################################################"
    )
  elif a == 2:
    print(
        "\n##########################################################################"
    )
    print(
        '#                 VOCÊ AGORA É DONO DA CARTELA 2                         #'
    )
    print(
        "##########################################################################"
    )
  elif a == 3:
    print( "\n##########################################################################"
    )
    print(
        '#                 VOCÊ AGORA É DONO DA CARTELA 3                         #'
    )
    print( "##########################################################################"
    )
  elif a == 4:
    print(
        "\n##########################################################################"
    )
    print(
        '#                 VOCÊ AGORA É DONO DA CARTELA 4                         #'
    )
    print(
        "##########################################################################"
    )

num=[1,2,3,4]
col=[-1,2,3,4]
davez=[]
while not sair:
    for i in range(len(col)):
      if col[i] != -1:
        davez.append(col[i])
    comando = input(f'\n# SELECIONE OUTRA CARTELA ({davez[0]}, {davez[1]} OU {davez[2]}) ou PRESSIONE ENTER PARA SORTEAR: __ ')
    davez = []
    if comando == '1':
      for i in range(len(col)):
        if col[i] == -1:
          col[i] = num[i]
        if col[i] == 1:
          col[i] = -1
      DONO = 1
      cartela_dono(DONO)
      escolha1()
      cartela_atual = 1
    elif comando == '2':
      for i in range(len(col)):
        if col[i] == -1:
          col[i] = num[i]
        if col[i] == 2:
          col[i] = -1
      DONO = 2
      cartela_dono(DONO)
      escolha2()
      cartela_atual = 2
    elif comando == '3':
      for i in range(len(col)):
        if col[i] == -1:
          col[i] = num[i]
        if col[i] == 3:
          col[i] = -1
      DONO = 3
      cartela_dono(DONO)
      escolha3()
      cartela_atual = 3
    elif comando == '4':
      for i in range(len(col)):
        if col[i] == -1:
          col[i] = num[i]
        if col[i] == 4:
          col[i] = -1
      DONO = 4
      cartela_dono(DONO)
      escolha4()
      cartela_atual = 4
    else:
      sortear()
      escolhaEnter()
      cont +=1
    if verificar_ganhador(c1t,c2t,c3t,c4t) == 1:
      if cartela_atual == 1:
        
        print ("# PARABÉNS! VOCÊ VENCEU!!!")
        nome = input("# Entre o seu nome para constar no rol de vencedores: ")
        with open("vencedores.txt","a") as arquivo:
          arquivo.write(nome)
        sair = True

      else:
        print("# OUTRA CARTELA FOI COMPLETADA \n# Melhor sorte na próxima vez!")
        sair = True
    if verificar_ganhador(c1t,c2t,c3t,c4t) == 2:
      if cartela_atual == 2:
        print ("# PARABÉNS! VOCÊ VENCEU!!!")
        nome = input("# Entre o seu nome para constar no rol de vencedores: ")
        with open("vencedores.txt","a") as arquivo:
          
          arquivo.write(nome)
        sair = True

      else:
        print("# OUTRA CARTELA FOI COMPLETADA \n# Melhor sorte na próxima vez!")
        sair = True
    if verificar_ganhador(c1t,c2t,c3t,c4t) == 3:
      if cartela_atual == 3:
        print ("# PARABÉNS! VOCÊ VENCEU!!!")
        nome = input("# Entre o seu nome para constar no rol de vencedores: ")
        with open("vencedores.txt","a") as arquivo:
  
          arquivo.write(nome)
        sair = True
      else:
        print("# OUTRA CARTELA FOI COMPLETADA \n# Melhor sorte na próxima vez!")
        sair = True
    if verificar_ganhador(c1t,c2t,c3t,c4t) == 4:
      if cartela_atual == 4:
        print ("# PARABÉNS! VOCÊ VENCEU!!!")
        nome = input("# Entre o seu nome para constar no rol de vencedores: ")
        with open("vencedores.txt","a") as arquivo:
          arquivo.write(nome)
        sair = True
      else:
        print("# OUTRA CARTELA FOI COMPLETADA \n# Melhor sorte na próxima vez!")
        sair = True
        


