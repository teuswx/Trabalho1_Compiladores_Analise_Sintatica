# Dicionário de tokens conforme seu PDF
TOKENS = {
    "OPERADORES_ARITMETICOS": {
        "+": "ADICAO",
        "-": "SUBTRACAO",
        "*": "MULTIPLICACAO",
        "/": "DIVISAO_REAL",
        "mod": "MODULO",
        "div": "DIVISAO_INTEIRA"
    },
    "OPERADORES_LOGICOS_RELACIONAIS_ATRIBUICAO": {
        "or": "OU_LOGICO",
        "and": "E_LOGICO",
        "not": "NAO_LOGICO",
        "==": "IGUALDADE",
        "<>": "DIFERENCA",
        ">=": "MAIOR_IGUAL",
        "<=": "MENOR_IGUAL",
        ">": "MAIOR",
        "<": "MENOR",
        ":=": "ATRIBUICAO"
    },
    "PALAVRAS_RESERVADAS": {
        "program": "PROGRAM",
        "var": "VAR",
        "integer": "INTEGER",
        "real": "REAL",
        "string": "STRING",
        "begin": "BEGIN",
        "end": "END",
        "for": "FOR",
        "to": "TO",
        "while": "WHILE",
        "do": "DO",
        "break": "BREAK",
        "continue": "CONTINUE",
        "if": "IF",
        "else": "ELSE",
        "then": "THEN",
        "write": "WRITE",
        "writeln": "WRITELN",
        "read": "READ",
        "readln": "READLN"
    },
    "SIMBOLOS": {
        ";": "PONTO_VIRGULA",
        ",": "VIRGULA",
        ".": "PONTO",
        ":": "DOIS_PONTOS",
        "(": "ABRE_PARENTESES",
        ")": "FECHA_PARENTESES"
    }
}

# Expressões regulares
REGEXES = {
    "STRING": r"(\"[^\"]*\"|'[^']*')",
    "OCTAL": r'\b0[0-7]+\b',
    "HEXA": r'\b0x[0-9A-Fa-f]+\b',
    "FLUTUANTE": r'\b\d+\.\d*0\b',
    "DECIMAL": r'\b[1-9]\d*\b',
    "IDENTIFICADOR": r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
    "COMENTARIO_LINHA": r'//.*',
    "COMENTARIO_BLOCO": r'{[^}]*}'
}