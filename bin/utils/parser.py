from bin.utils.binop import NumberNode, BinaryOperationNode
from bin.utils.tokens import TT_INT, TT_FLOAT, TT_MUL, TT_DIV, TT_PLUS, TT_MINUS


class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.token_idx = -1
        self.current_token = None
        self.advance()

    def advance(self):
        self.token_idx += 1
        if self.token_idx < len(self.tokens):
            self.current_token = self.tokens[self.token_idx]
        return self.current_token

    def factor(self):
        token = self.current_token
        if token.token_type in (TT_INT, TT_FLOAT):
            self.advance()
            return NumberNode(token)

    def binary_operation(self, func, operation_tokens):
        left = func()

        while self.current_token.token_type in operation_tokens:
            operation_token = self.current_token
            self.advance()
            right = func()
            left = BinaryOperationNode(left, operation_token, right)

        return left

    def term(self):
        return self.binary_operation(self.factor, (TT_MUL, TT_DIV))

    def expression(self):
        return self.binary_operation(self.term, (TT_PLUS, TT_MINUS))

    def parse(self):
        return self.expression()
