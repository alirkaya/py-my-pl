TT_INT      = 'TT_INT'
TT_FLOAT    = 'FLOAT'
TT_PLUS     = 'PLUS'
TT_MINUS    = 'MINUS'
TT_MUL      = 'MUL'
TT_DIV      = 'DIV'
TT_LPAREN   = 'LPAREN'
TT_RPAREN   = 'RPAREN'


class Token:

    def __init__(self, token_type, value = None):
        self.token_type = token_type
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.value}:{self.token_type}'
        return f'{self.token_type}'
