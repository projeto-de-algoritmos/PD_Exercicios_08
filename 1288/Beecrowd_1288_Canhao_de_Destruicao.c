// ===============================================================================================================
// Beecrowd - 1288 - Canhao de Destruicao - Nivel 5
// ===============================================================================================================
// Teoria: Programacao Dinamica
// Algoritmo utilizado: Algoritmo da Mochila
// ===============================================================================================================
// Para facilitar a correcao, foram incluidos no codigo comentarios detalhados, mesmo se desnecessarios :)
// ===============================================================================================================
#include <stdio.h>

// Levando em consideracao que o canhao pode ser carregado uma unica vez, respeitando o seu limite de quilos, 
// a sua tarefa e carregar o canhao com projeteis que nao ultrapassem o seu limite de carga mas que façam o 
// maior estrago possivel, para saber se a missao foi completada ou nao.
// ===============================================================================================================
int main() {
    // ===========================================================================================================
    // Entrada
    // ===========================================================================================================
    // A primeira linha de entrada contem o numero de casos de teste. 
    int casos_testes;
    scanf("%d", &casos_testes); // Entrada do numero de casos de teste
    int cont = 0;
    while (cont < casos_testes) {

        // Cada caso de teste inicia com uma linha contendo um numero inteiro N (1 ≤ N ≤ 50), que representa o 
        // numero de projeteis de chumbo disponiveis. 
        int num_projeteis;
        scanf("%d", &num_projeteis); // Entrada do numero de projeteis disponiveis
        int lista[num_projeteis+1][2]; // Criacao da matriz lista para armazenar os poderes de destruicao e 
                                       // pesos dos projeteis
        lista[0][0] = 0;
        lista[0][1] = 0;

        // Seguem N linhas contendo dois inteiros X e Y, representando 
        // respectivamente o poder de destruicao do projetil e o peso do projetil. 
        for (int i = 1; i <= num_projeteis; i++) {
            int poder_destruicao, peso;
            scanf("%d %d", &poder_destruicao, &peso); // Entrada do poder de destruicao e peso de cada projetil
            lista[i][0] = poder_destruicao;
            lista[i][1] = peso;
        }

        // A proxima linha contem um inteiro K (1 ≤ K ≤ 100) que representa a capacidade de carga do canhao e 
        // a ultima linha do caso de teste contem um inteiro R que indica a resistencia total do castelo.
        int capacidade_carga_canhao;
        scanf("%d", &capacidade_carga_canhao); // Entrada da capacidade de carga do canhao
        int resistencia_castelo;
        scanf("%d", &resistencia_castelo); // Entrada da resistencia do castelo

        // ===============================================================================================================
        // Solucao
        // ===============================================================================================================
        int linhas = capacidade_carga_canhao + 1;
        int colunas = num_projeteis + 1;

        int matriz[colunas][linhas]; // Criacao da matriz para armazenar os valores de maior poder de destruicao possiveis

        // Inicializacao da matriz com valores zero
        for (int i = 0; i < colunas; i++) {
            for (int j = 0; j < linhas; j++) {
                matriz[i][j] = 0;
            }
        }

        // Preenchimento da matriz com os valores de maior poder de destruicao possiveis
        for (int i = 1; i < colunas; i++) {
            for (int j = 1; j < linhas; j++) {
                if (lista[i][1] > j) {
                    matriz[i][j] = matriz[i-1][j];
                } else {
                    int a = matriz[i-1][j];
                    int b = lista[i][0] + matriz[i-1][j-lista[i][1]];
                    int maior_valor = (a > b) ? a : b;
                    matriz[i][j] = maior_valor;
                }
            }
        }

        // ===============================================================================================================
        // Saida
        // ===============================================================================================================
        // Se o dano total das cargas carregadas for maior ou igual a resistência do castelo entao devera ser impressa
        // a mensagem “Missao completada com sucesso”, caso contrario, devera ser impressa a mensagem “Falha na missao”.
        // Verificacao se o poder de destruicao da matriz e suficiente para completar a missao
        // ===============================================================================================================
        if (matriz[colunas-1][linhas-1] >= resistencia_castelo) {
            printf("Missao completada com sucesso\n");
        } else {
            printf("Falha na missao\n");
        }

        cont++;
    }

    return 0;
}
