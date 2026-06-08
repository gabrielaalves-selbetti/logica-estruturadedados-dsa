print("Jogo Pedra, Papel e Tesoura")
print("Regras: Escolham entre Pedra, Papel e Tesoura")

jogador_1 = input("Digite a sua jogada (pedra, papel ou tesoura): ")
jogador_2 = input("Digite a sua jogada (pedra, papel ou tesoura): ")

jogador_1 = jogador_1.strip()
jogador_1 = jogador_1.lower() 
jogador_2 = jogador_2.strip()
jogador_2 = jogador_2.lower()

print(f"""
Jogador 1 escolheu: {jogador_1}
Jogador 2 escolheu: {jogador_2}
""")

def jogo(jogada1, jogada2):
    resultado = ""

    if jogador_1 == jogador_2:
        resultado = "Empate!"
    elif (jogador_1 == "pedra" and jogador_2 == "tesoura") or (jogador_1 == "tesoura" and jogador_2 == "papel") or (jogador_1 == "papel" and jogador_2 == "pedra"):
        resultado = "Jogador 1 venceu."
    else:
        resultado = "Jogador 2 venceu" 

    return resultado


acoes = ["pedra", "papel", "tesoura"]
jogadas = [jogador_1, jogador_2]

if all(jogada in acoes for jogada in jogadas):
    saida = jogo(jogador_1, jogador_2)
    print(saida)
    print("Fim de jogo!")
else:
    print("Foi digitado um valor inválido.")

