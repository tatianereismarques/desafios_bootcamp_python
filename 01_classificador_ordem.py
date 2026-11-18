valores = input().split()
primeiro, segundo, terceiro = map(int, valores)

# Realiza a comparação dos valores em ordem de leitura, imprimindo classificação correspondente
if primeiro < segundo and segundo < terceiro:
    print("CRESCENTE")
elif primeiro > segundo and segundo > terceiro:
    print("DECRESCENTE")
else:
    print("DESORDENADO")