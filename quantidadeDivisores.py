

def entradaValores():
    n = -1
    while n<=0:
        n = int(input("Digite um numero positivo maior que 0: "))

    return n


def contaDivisores(num):
    numDiv = 0
    for cont in range (1,num+1):
        resto = num%cont
        if(resto == 0):
            numDiv = numDiv+1
    
    return numDiv


def main():
    numero = entradaValores()
    numeroDivisores = contaDivisores(numero)
    print(numeroDivisores)

if __name__ == "__main__":
    main()