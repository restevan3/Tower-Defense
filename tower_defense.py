import sys
from pathlib import Path

movimentos = {
    'N': (0, -1),
    'S': (0, 1),
    'O': (-1, 0),
    'L': (1, 0)
}

def calcular_dano(tabuleiro, x, y):
    dano = 0
    altura, largura = len(tabuleiro), len(tabuleiro[0])

    for var_x in [-1, 0, 1]:
        for var_y in [-1, 0, 1]:
            if var_x == 0 and var_y == 0:
                continue

            adj_x, adj_y = x + var_x, y + var_y

            if 0 <= adj_x < largura:
                if 0 <= adj_y < altura:
                    if tabuleiro[adj_y][adj_x] == 'T':
                        dano += 10
    return dano

def forca_bruta(tabuleiro):
    altura, largura = len(tabuleiro), len(tabuleiro[0])
    destino = (largura - 1, altura - 1)

    melhor_dano = [float('inf')]
    melhor_caminho = ['']

    visitados = set()

    def busca_profundidade (x, y, dano_acumulado, caminho):
        if (x, y) == destino:
            if dano_acumulado < melhor_dano[0]:
                melhor_dano[0] = dano_acumulado
                melhor_caminho[0] = caminho
            elif dano_acumulado == melhor_dano[0]:
                if len(caminho) < len(melhor_caminho[0]):
                    melhor_caminho[0] = caminho
            return
        
        for movimento, (movimento_x, movimento_y) in movimentos.items():
            novo_x, novo_y = x + movimento_x, y + movimento_y

            if 0 <= novo_x < largura and 0 <= novo_y < altura:
                if (novo_x, novo_y) not in visitados and tabuleiro[novo_y][novo_x] != 'T':
                    visitados.add((novo_x, novo_y))
                    novo_dano = dano_acumulado + calcular_dano(tabuleiro, novo_x, novo_y)
                    busca_profundidade (novo_x, novo_y, novo_dano, caminho + movimento)
                    visitados.remove((novo_x, novo_y)) 

    visitados.add((0, 0))
    busca_profundidade(0, 0, calcular_dano(tabuleiro, 0, 0), '') 

    return melhor_caminho[0], melhor_dano[0]

def ler_tabuleiro(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        linhas = f.read().splitlines()

    # a primeira linha é o tamanho; o tabuleiro pode ser retangular
    tabuleiro = [list(linha.strip()) for linha in linhas[1:] if linha.strip()]
    return tabuleiro

if __name__ == "__main__":
    nome_arquivo = sys.argv[1] if len(sys.argv) > 1 else "tabuleiro.in"
    tabuleiro = ler_tabuleiro(nome_arquivo)
    resultado, dano = forca_bruta(tabuleiro)
    print(f"Caminho ótimo: {resultado} - Dano: {dano}")

    with open(f"sol_{Path(nome_arquivo).stem}.out", 'w') as f:
        f.write(resultado)
