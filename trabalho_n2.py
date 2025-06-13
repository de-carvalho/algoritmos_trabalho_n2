lista = []

while True:
    valor = int(input("Digite um valor (0 para sair): "))
    if valor == 0:
        break
    pos = 0
    while pos < len(lista) and lista[pos] < valor:
        pos += 1
    lista.insert(pos, valor)
    print("Lista atual:", lista)