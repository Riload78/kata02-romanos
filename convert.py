def convertir_a_len_miles(numero):
    while len(numero)<4:
        numero= "0" + numero
    return numero

def sacar_simbolo_de_digito (digit, clave):
    romanos = {"unidades" : ["I", "V", "X"], "decenas" : ["X", "L", "C"], "centenas" : ["C", "D", "M"], "miles": ["M","",""]}
    #    romanos = {"unidades" : ["I", "V", "X"], "decenas" : ["X", "L", "C"], "centenas" : ["C", "D", "M"], "miles": ["M","?","?"]}

    digit = int(digit)
    if digit == 0:
        return ""
    
    nums = [1, 5, 10]
    puntero = 0
    for numero in nums:
        if digit > numero:
            puntero += 1
    if (nums[puntero] - digit) == 1:
        simboloU = romanos[clave][0] + romanos[clave][puntero]
    elif (nums[puntero] - digit) == 0:
        simboloU = romanos[clave][puntero]
    else:
        simboloU = romanos[clave][puntero-1] + romanos[clave][0]*(digit - nums[puntero-1])
    return simboloU

def devolver_romano(numero):
    numero = convertir_a_len_miles(numero)
    tipologia = ["miles", "centenas", "decenas", "unidades"]
    simbolo = ""
    numero_romano = ""
    poner_parentesis = False
    for i in range(len(numero)):
        clave = tipologia[i]
        if i == 0 and int(numero[0]) > 3:
            clave = "unidades"
            poner_parentesis = True
        n = numero[i]
        simbolo = sacar_simbolo_de_digito(n,clave)
        if i == 0 and poner_parentesis == True:
            simbolo = "(" + simbolo + ")"
        numero_romano = numero_romano + simbolo
    return numero_romano, poner_parentesis


print(devolver_romano("9999"))
    
    