import sys
from AnalisadorLexico import AnalisadorLexico
if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    arquivo = sys.argv[1]

    analisador_lexico = AnalisadorLexico(arquivo)

    for token in analisador_lexico.fazer_analise_lexica():
        print(token)

