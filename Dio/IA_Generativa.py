def gerar_resultado(tempo_treino):
    tempo = tempo_treino.lower()

    if "3 meses" in tempo:
        return "🔹 Realidade: pequenas mudanças na resistência e no condicionamento físico."
    
    elif "6 meses" in tempo:
        return "🔹 Realidade: início do ganho de massa magra e leve definição corporal."
    
    elif "1 ano" in tempo:
        return "🔹 Realidade: corpo mais definido, ganho muscular consistente e melhor postura."
    
    elif "3 anos" in tempo:
        return "🔹 Realidade: físico atlético bem desenvolvido, resultado de disciplina e constância."
    
    else:
        return "⚠️ Informe um tempo válido (ex: 3 meses, 6 meses, 1 ano, 3 anos)."


print("🏋️ Expectativa vs Realidade - IA Generativa")
tempo = input("Informe seu tempo de treino: ")
resultado = gerar_resultado(tempo)

print("\nResultado gerado pela IA:")
print(resultado)
