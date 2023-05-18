
simbolos = {
    1:'I',
    5:'V',
    10:'X',
}   

def entero_a_romano(n_int):
    if n_int in simbolos:  
        return simbolos[n_int]
    if n_int < 4:
        return n_int * simbolos[1]
    elif n_int == 4 :
         return simbolos[1] + simbolos[5]
    elif n_int > 4 and n_int < 9: 
        multiplicador = n_int - 5
        return simbolos[5] + multiplicador * simbolos[1]
    elif n_int == 9 :
        return simbolos[1] + simbolos[5]
    elif n_int == 10 :
        return simbolos[10]
    elif n_int > 10 :
        return simbolos[10] + (n_int - 10) * simbolos[1]
    elif n_int == 14:
        return simbolos[10] + simbolos[1] + simbolos[5]
    elif n_int > 14:
        return simbolos[10] + simbolos[5]
    

def convert_num(num):
    list_num = []
    str_num = str(num)
    for n in str_num :
       list_num.append(n)
    return list_num

if __name__ == "__main__":
    print(entero_a_romano(11))