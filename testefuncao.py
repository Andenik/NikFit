
# Função que calcula o peso que a pessoa deve perder por semana para chegar ao peso desejado
def calcula_peso():
    peso_atual = float(input("Digite o seu peso atual: "))
    peso_desejado = float(input("Digite o peso que deseja alcançar: "))
    contador_semana = 0
    while peso_atual >= peso_desejado:
        peso_semana = peso_atual * 0.01 # Perda de 1% do peso atual por semana
        peso_atual -= peso_semana       
        contador_semana += 1 
        print(f"Seu peso na semana {contador_semana} deve ser {peso_atual} kg, seu peso perdido foi {peso_semana} kg")

    print(f"Você levará {contador_semana} semanas para chegar ao peso desejado")

calcula_peso()