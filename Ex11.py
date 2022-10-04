def lernumero(min='', max=''):
    try:
        min = int(min)
        minimo = True
    except ValueError:
        minimo = False

    try:
        max = int(max)
        maximo = True
    except ValueError:
        maximo = False


    while True:
        try:
            while True:
                numero = int(input('Insere um número? '))
                if minimo and numero < min:
                    print(f'O número mínimo é {min}. Tente de novo.')
                    continue
                if maximo and numero > max:
                    print(f'O número máximo é {max}. Tente de novo.')
                    continue
                break
            break
        except ValueError:
            print('Insere valores válidos!')
    return numero


if __name__ == '__main__':
    num = lernumero(12, 15)
    numstr = str(num)
    base = 1
    gerado = 0
    for x in range(len(numstr)):
        #print(len(numstr) - x - 1)
        if int(numstr[len(numstr) - x - 1]) % 2 != 0:
            print(numstr[len(numstr) - x - 1])
            gerado += int(numstr[len(numstr) - x - 1]) * base
            base *= 10
    print(gerado)

    ns = []
    for x in str(num):
        if int(x) % 2 != 0:
            ns.append(x)
    print(int(''.join(ns)))






