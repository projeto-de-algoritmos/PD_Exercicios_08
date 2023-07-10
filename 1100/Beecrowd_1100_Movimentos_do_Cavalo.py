# ===================================================================================================================
# Beecrowd - 1100 - Movimentos do Cavalo - Nivel 5
# ===================================================================================================================
# Teoria: Programacao Dinamica
# Algoritmo utilizado: Algoritmo do Menor Caminho - Bellman-Ford
# Este problema poderia ser resolvido com busca em largura, mas optamos por usar Bellman-Ford para fins didaticos
# utilizando peso 1 em todas as arestas
# ===================================================================================================================
# Para facilitar a correcao, foram incluidos no codigo comentarios detalhados, mesmo se desnecessarios :)
# ===================================================================================================================

# Mapeamento dos movimentos do cavalo
# ===============================================================================================================
movimentos = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    
# ===============================================================================================================
# Funcao auxiliar para verificar se uma posicao esta dentro do tabuleiro
# ===============================================================================================================
def esta_dentro_tabuleiro(x, y):
    return 0 <= x <= 7 and 0 <= y <= 7
# ===============================================================================================================
    
# ===============================================================================================================
# Funcao auxiliar para obter os movimentos possiveis a partir de uma posicao
# os movimentos possiveis representam as arestas do grafo
# verifica se o movimento possivel nao vai cair fora do tabuleiro
# ===============================================================================================================
def obter_vizinhos(x, y):
    vizinhos = []
    for incremento_xy in movimentos:
        dx, dy = incremento_xy
        novo_x = x + dx
        novo_y = y + dy
        if esta_dentro_tabuleiro(novo_x, novo_y):
            vizinhos.append((novo_x, novo_y))
    return vizinhos
# ===============================================================================================================

# ===============================================================================================================
# Funcao de para encontrar o menor numero de movimentos
# ===============================================================================================================
def encontrar_menor_caminho(inicio, fim):
    distancia = [[float('inf')] * 8 for _ in range(8)]
    distancia[inicio[0]][inicio[1]] = 0
    fila = [(inicio[0], inicio[1])] 
    # foi utilizada uma fila para nao ter que percorrer todas as 64 posicoes do tabuleiro
    # e parar assim que calculasse o valor da distancia do ponto final
    while fila:
        x, y = fila.pop(0)
        if (x, y) == fim:
            break
        for vizinho in obter_vizinhos(x, y):
            vizinho_x, vizinho_y = vizinho
            if distancia[vizinho_x][vizinho_y] > distancia[x][y] + 1:
                distancia[vizinho_x][vizinho_y] = distancia[x][y] + 1
                fila.append((vizinho_x, vizinho_y))
    return distancia[fim[0]][fim[1]]
# ===============================================================================================================

# ===================================================================================================================
# Seu trabalho entao sera escrever um programa que, pegando dois quadrados a e b 
# como entrada, determine o numero de movimentos para encontrar a rota mais curta de a ate b.
# ===================================================================================================================
while True:
    try:
        # ===========================================================================================================
        # Entrada
        # ===========================================================================================================
        # A entrada contem um ou mais casos de teste. Cada caso de teste consiste de uma linha contendo dois 
        # quadrados separados por um espaco. Um quadrado sera uma string consistindo de uma letra (a-h) representando
        # a coluna e um digito (1-8) representando a linha do tabuleiro de xadrez.
        # ===========================================================================================================
        entrada = input()
        a, b = entrada.split()

        # ===========================================================================================================
        # Solucao
        # ===========================================================================================================
        # Mapeamento das letras das colunas para numeros
        mapeamento_colunas = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        # Convertendo as strings dos quadrados em coordenadas numericas
        inicio_a = (mapeamento_colunas[a[0]], int(a[1])-1)
        fim_b = (mapeamento_colunas[b[0]], int(b[1])-1)
        # Chamando a funcao para encontrar o menor numero de movimentos
        menor_caminho = encontrar_menor_caminho(inicio_a, fim_b)

        # ===============================================================================================================
        # Saida
        # ===============================================================================================================
        # para cada caso de teste imprima uma linha dizendo "To get from xx to yy takes n knight moves."
        # No caso xx e a origem, yy e o destino e n e a quantidade de movimentos necessarios para ir de xx  ate yy.
        # ===============================================================================================================
        print(f"To get from {a} to {b} takes {menor_caminho} knight moves.")

    except EOFError:
        break
