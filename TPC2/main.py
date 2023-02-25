def print_soma(soma):
    string = "  Soma: " + str(soma)
    print('-' * (len(string) + 2))
    print(string)
    print('-' * (len(string) + 2))


def main():
    soma = 0
    estado = True
    num_string = ""
    estado_string = ""

    linha = input(">")
    while linha != "":
        for c in linha:
            c = c.upper()

            if estado:
                if '0' <= c <= '9':
                    num_string += c
                elif len(num_string) != 0:
                    soma += int(num_string)
                    num_string = ""   
            
            match c:
                case 'O':
                    estado_string = c
                case 'N':
                    if estado_string == "O":
                        estado = True
                        estado_string = ""
                case 'F':
                    if estado_string == "O":
                        estado_string += c
                    elif estado_string == "OF":
                        estado = False
                        estado_string = ""
                case '=':
                    print_soma(soma)
                    estado_string = ""
                case other:
                    estado_string = ""
        
        linha = input(">")


if __name__ == '__main__':
    main()