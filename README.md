# Compilador para Linguagem CI 
## Aluno: João Victor Martins Dantas (20220070761)

Este repositório contém o código-fonte de um compilador para a linguagem CI (Constantes Inteiras), desenvolvido para a Atividade 2 da disciplina de Compiladores com Profº Andrei.

O objetivo do compilador é traduzir um arquivo-fonte que contém apenas uma constante inteira para um arquivo de saída em linguagem Assembly (sintaxe GNU `as` para x86-64). O código gerado utiliza uma rotina externa (`runtime.s`) para imprimir o valor da constante na tela. 

## Requisitos:

  * Python 3.8 ou superior 

## Como Executar o Compilador:

O compilador é executado via linha de comando, passando o nome do arquivo de entrada como um argumento.

**Formato do Comando:**

```bash
python compilador.py <nome_do_arquivo_de_entrada>
```

Se a execução for bem-sucedida, uma mensagem de sucesso será exibida, e o arquivo de saída `.s` será gerado no mesmo diretório. Em caso de erro, uma mensagem informativa será mostrada. Optou-se pelo uso de um `sys.argv[]` ao invés de usar uma abordagem interativa via `input()`, visto que aquela mais se adequa ao fluxo de implementação de um compilador.

## Exemplos de Teste:

Conforme solicitado no documento da atividade, seguem dois exemplos de teste: um com um programa CI correto e outro com um erro de sintaxe.

### Teste 1: Como executar o compilador para algum arquivo de entrada:

Um programa correto na linguagem CI contém apenas uma constante inteira.
1.  **Caso de teste correto: `teste_correto.ci`**:

    ```
    2
    ```

2.  **Execute o compilador** passando o nome do arquivo como argumento:

    ```bash
    python compilador.py teste_correto.ci
    ```

3.  **Saída Esperada:** O compilador deve gerar a seguinte mensagem abaixo e o arquivo `teste_correto.s`.

    ```
    Compilação bem-sucedida! Arquivo assembly gerado em: 'teste_correto.s'
    ```

### Teste 2: Casos de erro:

Um erro de sintaxe na linguagem CI ocorre quando o arquivo de entrada não contém uma constante inteira válida (ex: contém letras).

1.  **Caso de teste com erro: `teste_erro.ci`**:

    ```
    2erro
    ```

2.  **Execute o compilador** passando o nome do arquivo de erro como argumento:

    ```bash
    python compilador.py teste_erro.ci
    ```

3.  **Saída Esperada:** O compilador deve identificar o erro e exibir a mensagem apropriada, sem gerar um arquivo de saída.

    ```
    Erro: O conteúdo do arquivo 'teste_erro.ci não está no fomato adequado.
    ```
    ou
    ```
    Erro: O arquivo 'teste_erro.ci' não foi encontrado.
    ```
