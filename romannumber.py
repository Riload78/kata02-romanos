
unidades = {
    1:'I',
    5:'V',
    10:'X'
}  

decenas = {
    1: 'X',
    5: 'L',
    10: 'C'
}

centenas = {
    1: 'C',
    5: 'D',
    10: 'M'
}

millares = {
    1: 'M'
}

class RomanNumberError(Exception):
    pass


def lista_numero(num):
    n_mil = num // 1000 * 1000
    n_cen = (num % 1000) // 100 * 100
    n_dec = (num % 100) // 10 * 10
    n_uni = (num % 10)
    
    digitos = [n_mil, n_cen, n_dec, n_uni]
    return digitos

def sacar_clave(num):
    if num >= 1000 :
        clave = millares
        num = num // 1000
            
    elif num >= 100 :
        clave = centenas
        num //= 100
    
    elif num >= 10:
        clave = decenas
        num = num // 10
    else:
        clave = unidades  
        
    return clave, num 

def set_number(digito,clave):
    resultado = ''
    if digito < 4:
        resultado += digito * clave[1] # 2 3
    elif digito == 4 :
        resultado += clave[1] + clave[5]
    elif digito < 9: 
        multiplicador = digito - 5
        resultado += clave[5] + multiplicador * clave[1]
    else :
        resultado += clave[1] + clave[10]
        
    return resultado
    

def entero_a_romano(n_int):
    if n_int > 4000:
        raise RomanNumberError('RomanErrror must be less of 4000')
    
    digitos = lista_numero(n_int);
    resultado = ''
    
    for digito in digitos :
        if digito == 0:
            continue
        
        clave, digito = sacar_clave(digito)
        resultado += set_number(digito, clave)
  
    return resultado
    


if __name__ == "__main__":
    print(entero_a_romano(2345))