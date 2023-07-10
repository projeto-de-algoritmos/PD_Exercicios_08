# ===================================================================================================================
# Beecrowd - 2026 - Arvore de Natal - Nivel 5
# ===================================================================================================================
# Teoria: Programacao Dinamica
# Algoritmo utilizado: Algoritmo de Programacao Dinamica - Memoization
# ===================================================================================================================
# Para facilitar a correcao, foram incluidos no codigo comentarios detalhados, mesmo se desnecessarios :)
# ===================================================================================================================

# Para enfeitar a arvore estavam disponiveis no mercado onde Rolien foi procurar enfeites natalinos, varios pacotes 
# com uma quantidade X de enfeites e em cada pacote o seu respectivo peso em gramas. Baseando-se nessas informaçoes 
# Rolien estipulou que cada galho pudesse suporta uma quantidade K em gramas.
# Com isso ele precisava encontrar qual a melhor opcao entre os pacotes, ou seja, quais pacotes ele deve levar que 
# combinados possuam o maior numero de enfeites e que o galho ao qual ele vai enfeitar consiga suportar suportar 
# o peso dos enfeites.
# ===================================================================================================================

def escolher_enfeites(qtde_galhos, qtde_pacotes, capacidade, pacotes):
    # Inicializa a matriz de memoizacao
    memo = [[0] * (capacidade + 1) for _ in range(qtde_pacotes + 1)]
    # Preenche a matriz de memoizacao
    for i in range(1, qtde_pacotes + 1):
        enfeites, peso = pacotes[i - 1]
        for j in range(1, capacidade + 1):
            if peso > j:
                memo[i][j] = memo[i - 1][j]
            else:
                memo[i][j] = max(memo[i - 1][j], enfeites + memo[i - 1][j - peso])
    # Obtem o numero total de enfeites para cada galho
    num_enfeites = [memo[qtde_pacotes][capacidade]] * qtde_galhos
    return num_enfeites

# ===========================================================================================================
# Entrada
# ===========================================================================================================
# A primeira linha de entrada possui um inteiro G para os galhos da árvore, e também representando o numero 
# de casos de teste
G_num_galhos = int(input())  # Numero de galhos da arvore
for galho in range(1, G_num_galhos + 1):
    # A segunda linha de entrada possui um inteiro P (1 < P < 100) que indica o número de pacotes,
    # A próxima linha possui um inteiro W (1 < W < 1000) que indica a capacidade de peso que o galho suporta.
    P_num_pacotes = int(input())  # Numero de pacotes
    W_capacidade = int(input())  # Capacidade de peso do galho
    pacotes = []
    # As próximas P linhas indicam o número de enfeites em cadas pacote E(1 < E ≤ 300) e o 
    # peso de cada pacote PC (1 ≤ PC ≤ W).
    for _ in range(P_num_pacotes):
        num_enfeites, peso_pacote = map(int, input().split())
        pacotes.append((num_enfeites, peso_pacote))

    # ===========================================================================================================
    # Solucao
    # ===========================================================================================================
    # Chamada da funcao para escolher os pacotes
    # ===============================================================================================================
    num_enfeites = escolher_enfeites(G_num_galhos, P_num_pacotes, W_capacidade, pacotes)

    # ===============================================================================================================
    # Saida
    # ===============================================================================================================
    # A saída devera apresentar o número total de enfeites para cada galho.
    # ===============================================================================================================
    print(f'Galho {galho}:')
    print(f'Numero total de enfeites: {num_enfeites[galho - 1]}')
    print()
