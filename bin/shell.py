from bin.utils.lexer import Lexer
from bin.utils.parser import Parser


while True:
    text = input('basic >>> ')
    file = '<stdin>'
    tokens, error = Lexer(file, text).make_tokens()
    if error:
        print(error.as_string())
        break

    parser = Parser(tokens)
    ast = parser.parse()  # abstract-syntax-tree
    node, error = ast.node, ast.error
    if error:
        print(error.as_string())
    else:
        print(node)
    # if error: print(error.as_string())
    # else: print(tokens)
