from lexer import Lexer


while True:
    text = input('basic >>> ')
    file = '<stdin>'
    tokens, error = Lexer(file, text).make_tokens()

    if error: print(error.as_string())
    else: print(tokens)
