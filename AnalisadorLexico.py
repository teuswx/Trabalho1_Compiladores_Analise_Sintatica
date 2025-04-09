import sys
import re
from tokens import TOKENS, REGEXES

class AnalisadorLexico():
    def __init__(self, arquivo):
        self.__arquivo = arquivo
        self.__lista_token = []

    def fazer_analise_lexica(self):
        with open(self.__arquivo, 'r', encoding='utf-8') as f:
            aguardar = False
            comentario = ""
            for linha_num, linha in enumerate(f):
                if aguardar:
                    comentario += linha
                    if "}" in linha:
                        aguardar = False
                        # comentário completo — apenas ignora, não analisa
                    continue

                if "{" in linha and "}" not in linha:
                    aguardar = True
                    comentario += linha
                    continue

                # Se chegou aqui, é uma linha normal ou com comentário simples
                tokens = self.analise_linha(linha, linha_num)
                self.__lista_token += tokens

        return self.__lista_token
                

    def analise_linha(self, linha, linha_num):
        # Remover comentários
        coluna = 0
        linha = re.sub(REGEXES["COMENTARIO_LINHA"], "", linha)
        linha = re.sub(REGEXES["COMENTARIO_BLOCO"], "", linha)
        tokens = []

        # Verifica strings primeiro
        for match in re.finditer(REGEXES["STRING"], linha):  # verifica se acho uma srting "exemplo"
            tokens.append(("STRING", match.group(), linha_num, coluna)) # aqui vai retornar a parete que correspondeu ao regex, ou seja dentro de ('...') ou ("...")
            linha = linha.replace(match.group(), " ", 1)  #  remove a primeira ocorrência da string na linha para ir olhando uma por vez 

        # Quebra a linha em partes (palavras e símbolos)
        partes = re.findall(r'[\w]+|:=|==|>=|<=|<>|[^\s]', linha) # exmeplo ['if', 'a', '<=', 'b', 'then', 'c', ':=', 'a', '+', 'b', ';']

        for parte in partes:
            token = self.identificar_token(parte)
            tokens.append((token, parte, linha_num, coluna))
            coluna += 1

        return tokens

    def identificar_token(self, parte):
        for categoria, simbolos in TOKENS.items():  # aqui to lendo categoria por categoria dos TOKENS
            if isinstance(simbolos, dict):
                if parte in simbolos:
                    return simbolos[parte]

        # Verifica expressões regulares
        if re.match(REGEXES["HEXA"], parte):
            return "HEXADECIMAL"
        if re.match(REGEXES["OCTAL"], parte):
            return "OCTAL"
        if re.match(REGEXES["FLUTUANTE"], parte):
            return "FLUTUANTE"
        if re.match(REGEXES["DECIMAL"], parte):
            return "DECIMAL"
        if re.match(REGEXES["IDENTIFICADOR"], parte):
            return TOKENS["PALAVRAS_RESERVADAS"].get(parte, "IDENTIFICADOR")  #verica se tem parte em palavras reservadas, se n tive ele retorna identificador

        return "TOKEN_DESCONHECIDO"
