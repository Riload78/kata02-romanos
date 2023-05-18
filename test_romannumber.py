from romannumber import entero_a_romano


def test_uno_es_palito():
    assert entero_a_romano(1) == 'I'

def test_dos_es_palito():
    assert entero_a_romano(2) == 'II'
    
def test_tres_espalito():
    assert entero_a_romano(3) == 'III'
    
def test_cuatro_es_palito_uve():
    assert entero_a_romano(4) == 'IV'
    
def test_cinco_es_uve():
    assert entero_a_romano(5) == 'V'

def test_seis_es_uve_palito():
    assert entero_a_romano(6) == 'VI'

def test_siete_es_uve_dos_palitos():
    assert entero_a_romano(7) == 'VII'

def test_ocho_es_uve_tres_palitos():
    assert entero_a_romano(8) == 'VIII'
    
def test_nueve_es_palito_uve():
    assert entero_a_romano(9) == 'IV'

def test_diez_es_x():
    assert entero_a_romano(10) == 'X'   
    
def test_once_es_x_palito():
    assert entero_a_romano(11) == 'XI'

def test_doce_x_palito_palito():
    assert entero_a_romano(12) == 'XII'
    
def test_trece_x_palito_palito():
    assert entero_a_romano(13) == 'XIII'

def test_catorce_x_uve_palito():
    assert entero_a_romano(14) == 'XIV'
    
def test_quince_v():
    assert entero_a_romano(15) == 'XV'