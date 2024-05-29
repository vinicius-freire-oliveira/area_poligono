def Area():
    # Solicita os valores dos lados do retângulo
    l1 = float(input("Informe o valor do primeiro lado em m: "))
    l2 = float(input("Informe o valor do segundo lado em m: "))
    
    # Calcula a área do retângulo
    valor = l1 * l2

    # Imprime a área calculada
    print("O retângulo tem {} m²".format(valor))

# Chama a função para calcular e exibir a área do retângulo
Area()
