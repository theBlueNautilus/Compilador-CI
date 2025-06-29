import sys


def compilar_ci(nome_arquivo):

    # --- PASSO 1: ANÁLISE ---
    try:
        with open(nome_arquivo, 'r') as f:
            conteudo = f.read().strip()
            constante_inteira = int(conteudo)
    except ValueError:
        print(f"Erro: O conteúdo do arquivo '{nome_arquivo}' não está no fomato adequado.")
        return 0
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return 0

    # --- PASSO 2: SÍNTESE (GERAÇÃO DE CÓDIGO) ---
    codigo_gerado = f"""
    .section .text
    .globl _start

_start:
    mov ${constante_inteira}, %rax

    call imprime_num
    call sair

    .include "runtime.s"
"""
    
    nome_base = nome_arquivo.split('.')[0]
    nome_arquivo_saida = f"{nome_base}.s"

    try:
        with open(nome_arquivo_saida, 'w') as f:
            f.write(codigo_gerado)
        print(f"Arquivo de saída '{nome_arquivo_saida}' gerado com sucesso.")

    except:
        print(f"Erro ao escrever o arquivo de saída: {nome_arquivo_saida}")
        return 0
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso esperado: python compilador.py <nome_do_arquivo.ci>")
    else:
        compilar_ci(sys.argv[1])
