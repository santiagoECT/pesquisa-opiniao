#Programa de Pesquisa de opinião
#Autor: Fernando José Santiago

#Verifica o sistema e limpa a tela
import os
os.system('cls' if os.name == 'nt' else 'clear')  


#Entrada

total_excelente = 0 #Contador de opiniões excelentes
total_ruim = 0

#Processamento

for i in range(1, 51): #
    nome = input("Digite o nome do entrevistado: ") # Nome do entrevistado
    idade = int(input("Digite a idade do entrevistado: ")) # Idade do entrevistado
    opiniao = input("Digite a opinião do entrevistado, 1 - Excelente  : 2 - Bom  : 3 - Ruim :   ") # Opinião do entrevistado
    
    print(f"Entrevistado {i}: {nome}, {idade} anos, opinião: {opiniao}") # Exibe os dados do entrevistado
    

    if opiniao == "1": # Condição para opinião excelente
        print("Opinião: Excelente") # Exibe a opinião do entrevistado
        total_excelente = total_excelente + 1 # Incrementa o contador de opiniões excelentes
    elif opiniao == "2":
        print("Opinião: Bom") # Exibe a opinião do entrevistado
    elif opiniao == "3":
        print("Opinião: Ruim") # Exibe a opinião do entrevistado
        total_ruim = total_ruim + 1 # Incrementa o contador de opiniões ruim
    else:
        print("Opinião inválida") # Exibe mensagem de opinião inválida caso o entrevistado digite uma opção diferente de 1, 2 ou 3
# Saída
print(f"Total de entrevistados que deram opinião excelente: {total_excelente}") # Exibe o total de entrevistados que deram opinião excelente
print(f"Total de entrevistados que deram opinião ruim: {total_ruim}") # Exibe o total de entrevistados que deram opinião ruim