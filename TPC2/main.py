def print_soma(soma):
    string = "  Soma: " + str(soma)
    print('-' * (len(string) + 2))
    print(string)
    print('-' * (len(string) + 2))


def main():
    soma = 0
    estado = True
    num_string = ""

    linha = input(">>> ")
    while linha != "":
        linha = linha.upper()

        for ind, char in enumerate(linha):
            if estado:
                if char.isdigit():
                    num_string += char
                else:
                    if char == 'O' and linha[ind : ind+3] == "OFF":
                        estado = False
                    
                    if len(num_string) != 0:
                        soma += int(num_string)
                        num_string = ""  
            else:
                if char == 'O' and linha[ind : ind+2] == "ON":
                    estado = True

            if char == '=':
                print_soma(soma)
        
        linha = input(">>> ")


if __name__ == '__main__':
    main()