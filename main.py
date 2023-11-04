import re

# Define token types
TOKEN_TYPES = [
    ('KEYWORD', r'(Main|func|let|var|static|for|while|if|else if|elif|else|concat|pow|sqrt|class|init|deinit|public|protected|private|super|abstract|this|is_int|is_char|is_float|is_bool|is_str|replace|find|len)'),
    ('DATATYPE', r'(int|float|char|str|bool)'),
    ('CHAR', r'"[^"]{1}"|\'[^\']{1}\''),
    ('STRING', r'"[^"]"|\'[^\']\''),
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('FLOAT', r'\b[0-9]+\.[0-9]+\b'),
    ('INT', r'\b[0-9]+\b'),
    ('NULL', r'null'),
    ('BOOLEAN', r'(true|false)'),
    ('COMMENT', r'(//.|/\(.|\n)\/)'),
    ('OPERATOR',
     r',|=>|;|\(|\)|\{|\}|\:|\.|\+=|-=|\=|\+\+|--|&&|\|\||===|==|!==|!=|<=|>=|\\|\+|-|\|/|>|<|=')
]


def tokenize(source_code):
    tokens = []
    line_no = 1
    while source_code:

        for token_type, pattern in TOKEN_TYPES:
            match = re.match(pattern, source_code, re.IGNORECASE)
            if match:
                value = match.group(0)
                if token_type == 'OPERATOR':
                    tokens.append((value, value, line_no))
                else:
                    tokens.append((token_type, value, line_no))
                source_code = source_code[len(value):].lstrip()

                break
        else:
            raise SyntaxError(f"Unexpected character: {source_code[0]}")

    return tokens


if _name_ == '_main_':

    with open("mySourceCode", "r") as file:
        source_code = file.read()

    tokens = tokenize(source_code)
    for token_type, value, line_no in tokens:
        print([token_type, value, line_no])