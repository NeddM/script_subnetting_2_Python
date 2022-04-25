# INPUTS
# ip = input('Inserta la IP: ')
ip = '203.34.134.81'
mascara = input('Inserta el número de bits de la máscara: ')

# MASCARA SEPARADA
separada = ip.split('.')

def que_clase(separada):
    x = int(separada[0])
    if x >= 0 and x <= 127:
        return [255, 0, 0, 0]
        # print('Es clase A')
    if x >= 128 and x <= 191:
        return [255, 255, 0, 0]
        # print('Es clase B')
    if x >= 192 and x <= 223:
        return [255, 255, 255, 0]
        # print('Es clase C')
    if x >= 224 and x <= 239:
        return [255, 255, 255, 255]
        # print('Es clase D')
    if x >= 240 and x <= 247:
        print('Es clase E')


# Pasa la IP a binario
def a_binario_ip(lista):
    o1, o2, o3 ,o4 = lista

    bino1 = bin(int(o1))
    bino2 = bin(int(o2))
    bino3 = bin(int(o3))
    bino4 = bin(int(o4))

    binaria = [bino1, bino2, bino3, bino4]
    return binaria


# Pasa la MÁSCARA a binario
def a_binario_mascara(lista):
    o1, o2, o3 ,o4 = lista

    bino1 = bin(int(o1))
    bino2 = bin(int(o2))
    bino3 = bin(int(o3))
    bino4 = bin(int(o4))

    binaria = [bino1, bino2, bino3, bino4]
    return binaria


# Compara la IP con la MÁSCARA y realiza un AND
def comparar(listip, listmascara):
    oip1 = int(listip[0], 2)
    oma1 = int(listmascara[0], 2)
    and1 = oip1 & oma1

    oip2 = int(listip[1], 2)
    oma2 = int(listmascara[1], 2)
    and2 = oip2 & oma2

    oip3 = int(listip[2], 2)
    oma3 = int(listmascara[2], 2)
    and3 = oip3 & oma3

    oip4 = int(listip[3], 2)
    oma4 = int(listmascara[3], 2)
    and4 = oip4 & oma4

    andlist = [and1, and2, and3, and4]
    print(andlist)
    return andlist


# MÁSCARA DE LA SUBRED



hola = comparar(a_binario_ip(separada), a_binario_mascara(que_clase(separada)))
print(hola)


print(a_binario_ip(separada))
print(a_binario_mascara(que_clase(separada)))





