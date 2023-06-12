from random import randint
frequencia = [0] * 6
simulacao = []
for i in range(6000):
    jogada = randint(1,6)
    simulacao.append(jogada)
print(simulacao)

for i in range(6000): 
    frequencia[simulacao[i] - 1] += 1 
print(frequencia)
