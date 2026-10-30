# Tower Defense: caminho de menor dano

Exercício de algoritmos: encontrar o caminho de um inimigo que sai do canto superior esquerdo do tabuleiro e chega ao canto inferior direito recebendo o **menor dano possível** das torres.

## Regras

- O inimigo anda uma casa por vez: `N` (cima), `S` (baixo), `O` (esquerda), `L` (direita).
- Casas com `T` são torres e não podem ser atravessadas.
- Em cada casa visitada, o inimigo leva **10 de dano por torre vizinha** (as 8 casas ao redor, diagonais incluídas).
- Entre caminhos com o mesmo dano, vence o mais curto.

## Como funciona

Busca em profundidade (DFS) com backtracking, que explora todos os caminhos simples e guarda o de menor dano. É força bruta, então serve para tabuleiros pequenos.

## Como rodar

```bash
python3 tower_defense.py              # usa tabuleiro.in
python3 tower_defense.py outro.in     # ou outro arquivo
```

O caminho sai no terminal e no arquivo `sol_<nome>.out`.

## Formato da entrada

A primeira linha é o tamanho e as seguintes são as linhas do tabuleiro (`0` = livre, `T` = torre):

```
6
00000T
00T000
000T00
```

Saída para esse exemplo:

```
Caminho ótimo: LLLLSSL - Dano: 70
```
