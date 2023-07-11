// ===================================================================================================================
// Beecrowd - 2919 - Melhor Ordem - Nivel 7
// ===================================================================================================================
// Teoria: Programacao Dinamica
// Algoritmo utilizado: Algoritmo de Maior subsequencia crescente
// ===================================================================================================================
// Para facilitar a correcao, foram incluidos no codigo comentarios detalhados, mesmo se desnecessarios :)
// ===================================================================================================================
// Sera dado a voce uma lista com N numeros inteiros, você tera que escolher NI valores e inserir em uma nova lista. 
// Ha algumas restricoes, voce tera que percorrer da esquerda para a direita e cada vez que voce desejar inserir um 
// novo elemento na lista o elemento que voce esta inserindo tem que ser maior do que todos elementos que voce ja 
// inseriu ate o momento. O tamanho dessa lista deve ser maximizado. E permitido percorrer esta lista uma vez e ela 
// deve ficar em ordem crescente.

#include <stdio.h>
#include <stdlib.h>

int main() {
    // ===========================================================================================================
    // Entrada
    // ===========================================================================================================
    // A entrada possui varios casos de teste e termina com EOF.
    // A primeira linha de cada caso de teste possui um inteiro N representando respectivamente o número de 
    // elementos da lista, na proxima linha haverá N inteiros separados por espaço, representados por NI. 
    // N <= 5*10⁵, NI <= 10⁹.
    int qtde_elementos;
    while (scanf("%d", &qtde_elementos) == 1) {
        int* nums = (int*)malloc(qtde_elementos * sizeof(int));
        for (int i = 0; i < qtde_elementos; ++i)
            scanf("%d", &nums[i]);

        // ===========================================================================================================
        // Solucao - maior subsequencia crescente
        // encontrando a maior subsequência crescente - O(n^2)
        // ===========================================================================================================
        /*
        int* L = (int*)malloc(qtde_elementos * sizeof(int));
        int tam_maior_subseq = 0;
        for (int j = 0; j < qtde_elementos; j++) {
            L[j] = 1;
            for (int i = 0; i < j; i++) {
                if (nums[i] < nums[j] && (1 + L[i]) > L[j]) {
                    L[j] = 1 + L[i];
                    if (L[j] > tam_maior_subseq) {
                        tam_maior_subseq = L[j]; // guardando o maior valor
                    }
                }
            }
        }
        */

        // ===========================================================================================================
        // Solucao - maior subsequencia crescente
        // encontrando a maior subsequência crescente - O(nlgn)
        // ===========================================================================================================
        
        int* MSC = (int*)malloc(qtde_elementos * sizeof(int));
        int tam_maior_subseq = 0;
        for (int i = 0; i < qtde_elementos; ++i) {
            int num = nums[i];
            int esq = 0;
            int dir = tam_maior_subseq;
            while (esq < dir) {
                int meio = (esq + dir) / 2;
                if (MSC[meio] < num)
                    esq = meio + 1;
                else
                    dir = meio;
            }
            if (esq == tam_maior_subseq)
                MSC[tam_maior_subseq++] = num;
            else
                MSC[esq] = num;
        }
        free(MSC);
        
        // ===============================================================================================================
        // Saida
        // ===============================================================================================================
        printf("%d\n", tam_maior_subseq);
        free(nums);
        //free(L);
    }
    return 0;
}
