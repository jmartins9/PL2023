import re


on = False # True if phone is up
money = 0

def troco():
    global money

    coins = { 1: 0, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0, 200: 0 }

    for coin in [200, 100, 50, 20, 10, 5, 2, 1]:
        if money <= 0:
            break
        nc = money // coin
        coins[coin] += nc
        money -= nc * coin
    print(f"maq: \"troco= {coins[200]}x2e, {coins[100]}x1e, {coins[50]}x50c, {coins[20]}x20c, {coins[10]}x10c, {coins[5]}x5c, {coins[2]}x2c, {coins[1]}x1c;\"")


def levantar(line):
    global on

    if on:
        print("maq: \"Telefone já levantado.\"")
    else:
        on = True
        print("maq: \"Introduza moedas.\"")

def pousar(line):
    global on, money

    if not on:
        print("maq: \"Telefone já pousado.\"")
    else:
        troco()
        print("maq: \"Volte Sempre!\"")
        on = False
        money = 0


def moeda(line):
    global on, money

    if not on:
        print("maq: \"Telefone não levantado.\"")
    else:
        coins = re.findall(r"\d+[ce]", line)

        v = 0
        for coin in coins:
            if coin[-1] == "e":
                m = int(coin[:-1]) * 100
            else:
                m = int(coin[:-1])

            if m not in [1,2,5,10,20,50,100,200]:
                print(f"maq: \"{coin} - moeda inválida.\"")
            else:
                v += m
        money += v
        print(f"maq: \"saldo = {money // 100}e{money - (money // 100) * 100}c\"")


def numero(line):
    global on, money 

    if not on:
        print("maq: \"Telefone não levantado.\"")
    else:
        phone_number = line[2:]

        if not re.fullmatch(r"(00\d{9}|\d{9})", phone_number):
            print("maq: \"Número de telefone inválido.\"")
        elif phone_number.startswith("601") or phone_number.startswith("604"):
            print("maq: \"Esse número não é permitido neste telefone. Queira discar novo número!\"")
        elif phone_number.startswith("00"):
            if money < 150:
                print("maq: \"Saldo insuficiente.\"")
            else:
                money -= 150
                print(f"maq: \"saldo = {money // 100}e{money - (money // 100) * 100}c\"")
        elif phone_number.startswith("2"):
            if money < 25:
                print("maq: \"Saldo insuficiente.\"")
            else:
                money -= 25
                print(f"maq: \"saldo = {money // 100}e{money - (money // 100) * 100}c\"")
        elif phone_number.startswith("808"):
            if money < 10:
                print("maq: \"Saldo insuficiente.\"")
            else:
                money -= 10
                print(f"maq: \"saldo = {money // 100}e{money - (money // 100) * 100}c\"")
        else:
            print(f"maq: \"saldo = {money // 100}e{money - (money // 100) * 100}c\"")


def abortar(line):
    global on, money

    if not on:
        print("maq: \"Telefone não levantado.\"")
    else:
        troco()
        money = 0  


def main():
    commands = {
        "LEVANTAR": levantar,
        "POUSAR" : pousar,
        "MOEDA": moeda,
        "T" : numero,
        "ABORTAR" : abortar
    }

    while True:
        line = input()
        for k,v in commands.items():
            if line.startswith(k):
                v(line)

if __name__ == '__main__':
    main()