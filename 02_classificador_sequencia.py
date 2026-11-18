linha = input().strip()

if not linha:
    print("misto")
else:
    numeros = [int(valor) for valor in linha.split()]

    if len(numeros) < 2:
        print("misto")
    else:
        eh_crescente = True
        eh_decrescente = True

        for i in range(1, len(numeros)):
            atual = numeros[i]
            anterior = numeros[i - 1]

            if atual < anterior:
                eh_crescente = False
                eh_decrescente = True
              
            if atual >= anterior:
              eh_decrescente = False            

        if eh_crescente:
            print("crescente")
        elif eh_decrescente:
            print("decrescente")
        else:
            print("misto")