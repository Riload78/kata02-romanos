simbolos = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M",
    4000: "(IV)"
}

def entero_a_romano(n_ent):
    resultado = ""
    numeros = sorted(simbolos.keys(), reverse=True) 

    for num in numeros:
        while n_ent >= num:
            resultado += simbolos[num]
            n_ent -= num
            
    return resultado

def convert_num(n_ent):
    strNum = str(n_ent)
    miles_dig = []
    calc_miles = ''
    if n_ent > 4000:
        miles=[]
        for i in range(len(strNum)):  # calculo los miles que hay guardandoles en una lista y me guuardo el strin de las centenas 
            while len(strNum) - i >  3:
                dec = strNum[i]
                rest = strNum[i+1:]
                miles.append(dec)
                break
        for i in range(len(miles)):
            if len(miles) > 0:
                miles_dig = miles[-3:]
                miles = miles[:-3]
                delimiter = ''
                new_miles = delimiter.join(miles_dig)
                # calculo por separado los miles y las centenas llamando a la funcion mágica entero_a_romano
                
                calc_miles = '('* (i+1) + entero_a_romano(int(new_miles)) + ')' * (i+1) + calc_miles
            
        calc_centenas = entero_a_romano(int(rest))
        
            
        # concateno miles y centenas y lo devuelvo
        return calc_miles + calc_centenas
        
                
""" print (convert_num(53125))
print (convert_num(54125))
print (convert_num(125678)) """
print (convert_num(4000004040004000040000))

""" 
Ejemplo del enunciado:
Con esa regla 5125 sería (V)CXXV, sin embargo hay ambigüedad en algunos casos:
53125 podría ser
(LIII)CXXV ó
(L)MMMCXXV
54125 sólo puede ser 

Con esto se consigue la primera opción -> (LIII)CXXV 
(LIV)CXXV """

