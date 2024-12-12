

import re
def isValidPhoneNumber(phone):
    #Cada diagonal invertida significa "literal"
    #El pattern se descompone en "literal (", "literal digito entero de 3 caracteres", "literal ) y un espacio", "Literal digito entero de 3 caracteres y un guión", "Literal digito entero de 4 caracteres"
    #Esto nos da como resultado "(***) ***-****" Donde cada asterisco es un numero de l0 al 9 y los demás caracteres son exactamente como aparecen.
    # La r antes de las comillas implica "raw", es decir, que el string pasa en crudo, esto evita que python lea escapes de linea erroneos.
    pattern = r"\(\d{3}\) \d{3}-\d{4}"
    return bool(re.match(pattern, phone))

print(isValidPhoneNumber("(123) 456-7890"))
print(isValidPhoneNumber("1111)555 2345"))
print(isValidPhoneNumber("098) 123 4567"))