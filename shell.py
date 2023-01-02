from lexer import Lexer


while True:
    text = input('basic >>> ')
    tokens, error = Lexer(text).make_tokens()

    if error: print('Invalid Syntax')
    else: print(tokens)
