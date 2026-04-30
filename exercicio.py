 #voce quer escolher um numero aleatorio de 10-100 imprimir na tela um valor entre 10 a 100 
import random

print(random.randint(10, 100))

# voce quer fazer um sortei de 5 nomes em uma lista de nomes. Crie uma lista de 5 nomes e sortie um nome dessa lista

Nomes = ["Guilherme", "vinicius", "Thiago","Gustavo","tiago"]
print(random.choice(Nomes))

#voce quer simular a opção de uma koeda e resultado em cara ou coroa. 
# jogue as opç~es de uma lista e depois crie um programa que imprime "cara ou coroa " na tela

Moeda = ["Cara", "Coroa"]

print(random.choice(Moeda))