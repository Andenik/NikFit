import Conexao
import calculos



while True:
    print("Bem vindo ao Nikfit - Plataforma de que monitora sua saude e perda de peso")
    op = input("A seguir você terá as opções de escolha para o que deseja fazer:\n 1 - Calcular quantidade de tempo para chegar ao peso desejado\n 2 - Calcular IMC\n 3 - Calcular quantidade de calorias \n 4 - Sair")

    match op:
        case "1":
            print("Você escolheu a opção 1")
            calculos.calcula_peso()
