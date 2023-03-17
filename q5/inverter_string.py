texto_teste = "texto de teste"


#usando string slice
def inverter_string_using_slice(string: str) -> str:
    return string[::-1]

#sem usar string slice

def inverter_string(string: str) -> str:
    string_invertida = ""
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

if __name__== '__main__':

    print(inverter_string(texto_teste))
    print(inverter_string_using_slice(texto_teste))