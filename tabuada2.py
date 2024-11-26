def exibir_tabuada(n):
    print(f"\nTabuada de {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Pergunta para o usuário qual tabuada ele quer ver
while True:
    try:
        num = int(input("Escolha um número para ver a tabuada (1-10) ou 0 para sair: "))
        if num == 0:
            print("Saindo...")
            break
        elif 1 <= num <= 10:
            exibir_tabuada(num)
        else:
            print("Escolha um número entre 1 e 10.")
    except ValueError:
        print("Por favor, insira um número válido.") #caso não selecionem um numero de 0 a 10
