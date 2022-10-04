def fatorial(numero, rondas):
    if numero == 1:
        return numero
    else:
        print(f'Ronda: {rondas} numero={numero}')
        rondas += 1
        return numero * fatorial(numero - 1, rondas)


if __name__ == '__main__':
    print(fatorial(5, 1))

