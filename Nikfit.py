import Conexao

def calcula_peso():
    peso_atual = float(input("Digite o seu peso atual: "))
    peso_desejado = float(input("Digite o peso que deseja alcançar: "))
    contador_semana = 0
    while peso_atual >= peso_desejado:
        peso_semana = peso_atual * 0.01 # Perda de 1% do peso atual por semana
        peso_atual -= peso_semana       
        contador_semana += 1 

    print(f"Você levará {contador_semana} semanas para chegar ao peso desejado")


while True:
    print("Bem vindo ao Nikfit - Plataforma de que monitora sua saude e perda de peso")
    op = input("A seguir você terá as opções de escolha para o que deseja fazer:\n 1 - Calcular quantidade de tempo para chegar ao peso desejado\n 2 - Calcular IMC\n 3 - Calcular quantidade de calorias \n 4 - Sair")

    match op:
        case "1":
            print("Você escolheu a opção 1")
            calcula_peso()
