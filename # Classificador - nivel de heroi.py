# Classificador - nivel de heroi
nome = "Yuichi"
xp = 3000  # exemplo de valor de XP
# Estrutura de decisão para determinar o nível do herói
if xp < 1000:
    nivel = "Ferro"
elif xp <= 2000:
    nivel = "Bronze"
elif xp <= 5000:
    nivel = "Prata"
elif xp <= 7000:
    nivel = "Ouro"
elif xp <= 8000:
    nivel = "Platina"
elif xp <= 9000:
    nivel = "Ascendente"
elif xp <= 10000:
    nivel = "Imortal"
else:
    nivel = "Radiante"

# Exibindo a mensagem final
print(f"O Herói de nome {nome} está no nível de {nivel}")
