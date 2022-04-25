# INPUTS
# ip = input('Inserta la IP: ')
# mascara = input('Inserta el número de bits de la máscara: ')
ip = '192.168.15.10'
mascara = 26

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

def que_clase_bits(separada):
    x = int(separada[0])
    if x >= 0 and x <= 127:
        return 8
        # print('Es clase A')
    if x >= 128 and x <= 191:
        return 16
        # print('Es clase B')
    if x >= 192 and x <= 223:
        return 24
        # print('Es clase C')
    if x >= 224 and x <= 239:
        return 32
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

# MÁSCARA DE LA SUBRED BINARIO
def a_binario_mascarasubred(mascara):
    total = 32 - int(mascara)
    cadena = ''
    for i in range(0, int(mascara)):
        cadena += '1'
    for i in range(int(mascara), 32):
        cadena += '0'
    
    o1 = cadena[0:8]
    o2 = cadena[8:16]
    o3 = cadena[16:24]
    o4 = cadena[24:32]
    
    octetos = [o1, o2, o3, o4]
    return octetos

# MÁSCARA DE LA SUBRED INT
def mascarasubreddef(mascara):
    o1 = int(mascara[0], 2)
    o2 = int(mascara[1], 2)
    o3 = int(mascara[2], 2)
    o4 = int(mascara[3], 2)

    return [o1, o2, o3, o4]


# print(a_binario_mascarasubred(mascara))

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

    andlist = [bin(and1), bin(and2), bin(and3), bin(and4)]
    return andlist

def compararor(listip, listmascara):
    oip1 = int(listip[0], 2)
    oma1 = int(listmascara[0], 2)
    and1 = oip1 | oma1

    oip2 = int(listip[1], 2)
    oma2 = int(listmascara[1], 2)
    and2 = oip2 | oma2

    oip3 = int(listip[2], 2)
    oma3 = int(listmascara[2], 2)
    and3 = oip3 | oma3

    oip4 = int(listip[3], 2)
    oma4 = int(listmascara[3], 2)
    and4 = oip4 | oma4

    andlist = [bin(and1), bin(and2), bin(and3), bin(and4)]
    return andlist

def contar_bits_host(mascara):
    dif = 32 - int(mascara)
    return str(dif)

def contar_bits_subred(mas1, mas2):
    dif = 32 - (int(mas1) + int(mas2))
    return int(dif)

def idsubredoctetos(mascara):
    string = ''
    contador = 0
    sol = []
    while contador < mascara:
        string += '1'
        contador += 1

    oct1 = string[0:8]
    oct2 = string[8:16]
    oct3 = string[16:24]
    oct4 = string[24:32]

    if len(oct1) >= 0 and len(oct1) < 8:
        sol = [oct1, '', '', '']
    elif len(oct2) >= 0 and len(oct2) < 8:
        sol = ['', oct2, '', '']
    elif len(oct3) >= 0 and len(oct3) < 8:
        sol = ['', '', oct3, '']
    elif len(oct4) >= 0 and len(oct4) <= 8:
        while len(oct4) < 8:
            oct4 += '0'
            sol = ['00000000', '00000000', '00000000', oct4]
            print(sol)
    # print(sol)
    # print(int(oct4, 2))
    return sol


# print(idsubredoctetos(mascara))
# print(idsubredoctetos())





# Ejecuciones
# Ejecuciones
# Ejecuciones

# AND entre la IP y la MÁSCARA
andipmascara = comparar(a_binario_ip(separada), a_binario_mascarasubred(mascara))
andone = [int(andipmascara[0], 2), int(andipmascara[1], 2), int(andipmascara[2], 2), int(andipmascara[3], 2)]
print(andone)

# Pasa la IP a binario
ipbinario = a_binario_ip(separada)

# Pasa la máscara de la clase a binario
masbin = a_binario_mascara(que_clase(separada))

# Máscara subred
mascarasubred = mascarasubreddef(a_binario_mascarasubred(mascara))

# Nº de bits en subred
contarsub = contar_bits_subred(que_clase_bits(separada), contar_bits_host(mascara))

# Sacar id de subred
# idsubred = comparar(ipbinario, a_binario_mascarasubred(mascara))

# Sacar id de subred
red = compararor(a_binario_ip(separada), idsubredoctetos(mascara))
idsubred = int(red[0], 2), int(red[1], 2), int(red[2], 2), int(red[3], 2)
print(idsubred)

# SOLUCIONES
# SOLUCIONES
# SOLUCIONES
print(f'1. Máscara de subred: {mascarasubred[0]}.{mascarasubred[1]}.{mascarasubred[2]}.{mascarasubred[3]}         ')
# print(f'2. Dirección IP de broadcast para la primera subred: {}')
print(f'3. Número de bits de red: {que_clase_bits(separada)}')
print(f'4. Número de bits de subred: {contarsub}')
print(f'5. Número de bits de host: {contar_bits_host(mascara)}')
print(f'6. ID de red: {str(andone[0])}.{str(andone[1])}.{str(andone[2])}.{str(andone[3])}')
print(f'7. ID de subred: {int(red[0], 2)}.{int(red[1], 2)}.{int(red[2], 2)}.{int(red[3], 2)}')
# print(f'8. Dirección IP de 2 PCs por subred: {}')






