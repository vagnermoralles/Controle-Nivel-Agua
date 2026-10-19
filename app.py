from colorama import Fore, Style

# Lista com os níveis e situações do reservatório
niveis = [
    "Nível 1: Muito baixo (crítico)",
    "Nível 2: Baixo",
    "Nível 3: Médio",
    "Nível 4: Alto",
    "Nível 5: Muito alto (alerta)"
]

# Função responsável por definir a cor conforme o nível informado
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE

# Exibição dos dados do reservatório
print("--- MONITORAMENTO DO RESERVATÓRIO ---\n")

posicao = 1
for mensagem in niveis:
    cor = definir_cor(posicao)
    print(cor + mensagem)
    posicao = posicao + 1

# Restaura o estilo padrão do terminal ao final
print(Style.RESET_ALL)
