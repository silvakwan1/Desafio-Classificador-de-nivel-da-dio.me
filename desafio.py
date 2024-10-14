
nome_heroi = input("Digite o nome do herói: ")
xp_heroi = int(input("Digite a quantidade de experiência (XP) do herói: "))
nivel_heroi = "" 

if xp_heroi < 1000:
    nivel_heroi = "Ferro"
elif 1001 <= xp_heroi <= 2000:
    nivel_heroi = "Bronze"
elif 2001 <= xp_heroi <= 5000:
    nivel_heroi = "Prata"
elif 5001 <= xp_heroi <= 7000:
    nivel_heroi = "Ouro"
elif 7001 <= xp_heroi <= 8000:
    nivel_heroi = "Platina"
elif 8001 <= xp_heroi <= 9000:
    nivel_heroi = "Ascendente"
elif 9001 <= xp_heroi <= 10000:
    nivel_heroi = "Imortal"
else:
    nivel_heroi = "Radiante"

print(f"O Herói de nome {nome_heroi} está no nível de {nivel_heroi}")
