import random

#gera um valor de 0.0 a 1.0
print (random.random()) 
#gera um valor decimal de valor mínimo ao valor máximo 
print(random.uniform(4, 10))
#gera um valor inteiro de valor minimo ao valor maximo 
print(random.randint(4, 111))

alunos = ["Ceci", "Lucas","Gui","toli","gustavo","tiago","luiz","andré"]
print(random.choices(alunos, k=2))

alunos = ["Ceci", "Lucas","Gui","toli","gustavo","tiago","luiz","andré"]
print(random.shuffle(alunos))