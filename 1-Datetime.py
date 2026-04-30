from datetime import datetime



#crie uma data 
lançamento_do_App = datetime (2026,12,29)
print(lançamento_do_App)

#receba um informação do uisuario, qual data será lançado o jogo do mesmo. 

Lançamendo_Fifa = datetime.strptime(input("Data de lançamento do jogo"), '%d/%m/%Y')
print(Lançamendo_Fifa)

#Calcular o intervelo entre datas
Data_atual = datetime.now()
Prazo = Lançamendo_Fifa - Data_atual 
print(Prazo.days)

#Calculo quantos dias faltam para o meu aniversario. 

Aniversario = datetime.strptime(input("Qual é o dia do seu aniversario ? "), '%d/%m/%Y')
Data_atual =datetime.now()
calculo = Aniversario - Data_atual
print(calculo.days) 