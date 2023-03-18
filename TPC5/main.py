import re

state = {
    "on/off" : False,
    "money" : 0
}


def get_saldo_str():
    return str(state["money"]//100)+"e"+(str(state["money"]%100))+"c"

def troco():
    coins = {
        1: 0, 
        2: 0,
        5: 0,
        10: 0,
        20: 0,
        50: 0,
        100: 0,
        200: 0 
    }

    for coin in [200,100,50,20,10,5,2,1]:
        while state["money"] >= 0:
            if state["money"] // coin == 0:
                break
            else:
                div = state["money"] // coin
                state["money"] -= div * coin
                coins[coin] += 1
    
    print(f"maq: 'Troco = {coins[200]}x2e, {coins[100]}x1e, {coins[50]}x50c, {coins[20]}x20c, {coins[10]}x10c, {coins[5]}x5c, {coins[2]}x2c, {coins[1]}x1c'", end="")


def levantar():
    if state["on/off"] == True:
        print("maq: 'Já esta levantado!'")
    else:
        print("maq: 'Introduza moedas.'")
        state["on/off"] = True


def pousar():
    if state["on/off"] == False:
        print("maq: 'Telefone não foi levantado!'")
    else:
        troco()
        print(" Volte sempre!'")
        state["on/off"] = False
        state["money"] = 0


def moeda(line):
    invalid_coins = list()

    for coin in re.split(r"\s*,\s*", line[6:][:-1]):
        if match := re.match(r"(\d+)c", coin):
            value = int(match.group(1))
            if value in [1,2,5,10,20,50]:
                state["money"] += value
            else:
                invalid_coins.append(coin)
        elif match := re.match(r"(\d+)e", coin):
            value = int(match.group(1))
            if value in [1,2]:
                state["money"] += value*100
            else:
                invalid_coins.append(coin)
        else:
            invalid_coins.append(coin)

    string = "maq : "
    for coin in invalid_coins:
        string += coin + " - moeda inválida; "
    string += f"saldo = {get_saldo_str()}" 
    print(string)


def numero(line):
    if state["on/off"] == False:
        print("maq: 'Telefone não está levantado!'")
    else:
        number = line[2:]

        if not re.match(r"(\d{9}|00\d{9})$", number):
            print("maq: 'Número inválido!'")

        elif re.match(r"601|641", number):
            print("maq: 'Esse número não é permitido neste telefone. Queira discar novo número!'")

        elif re.match(r"00", number):
            saldo = state["money"]
            if saldo >= 150:
                state["money"] -= 150
                print(f"maq: 'saldo = {get_saldo_str()}'")
            else:
                print("maq: 'Saldo insuficiente!'")

        elif re.match(r"2", number):
            saldo = state["money"]
            if saldo >= 25:
                state["money"] -= 25
                print(f"maq: 'saldo = {get_saldo_str()}'")
            else:
                print("maq: 'Saldo insuficiente!'")

        elif re.match(r"808", number):
            saldo = state["money"]
            if saldo >= 10:
                state["money"] -= 10
                print(f"maq: 'saldo = {get_saldo_str()}'")
            else:
                print("maq: 'Saldo insuficiente!'")

        elif re.match(r"800", number):
            print(f"maq: 'saldo = {get_saldo_str()}'")




def abortar():
    if state["on/off"] == False:    
        print("maq: 'Telefone não está levantado!'")
    else:
        troco()
        print()
        state["money"] = 0


def main():
    while True:
        line = input()

        if re.match(r"LEVANTAR", line):
            levantar()
        elif re.match(r"POUSAR", line):
            pousar()
        elif re.match(r"MOEDA", line):
            moeda(line)
        elif re.match(r"T", line):
            numero(line)
        elif re.match(r"ABORTAR", line):
            abortar()



if __name__ == '__main__':
    main()

        
