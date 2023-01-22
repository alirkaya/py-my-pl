import tokenize

from bin.utils.binop import NumberNode, BinaryOperationNode
from bin.utils.tokens import TT_INT, TT_FLOAT, TT_MUL, TT_DIV, TT_PLUS, TT_MINUS, TT_EOF
from bin.errors.errors import InvalidSyntaxError


class ParseResult:

    def __init__(self):
        self.error = None
        self.node = None

    def register(self, other):
        if isinstance(other, ParseResult):
            if other.error: self.error = other.error
            return other.node
        return other

    def success(self, node):
        self.node = node
        return self

    def failure(self, error):
        self.error = error
        return self


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
        result = ParseResult()
        token = self.current_token
        if token.token_type in (TT_INT, TT_FLOAT):
            result.register(self.advance())
            return result.success(NumberNode(token))

        return result.failure(InvalidSyntaxError(token.pos_start, token.pos_end, 'Expected int or float'))

    def binary_operation(self, func, operation_tokens):
        result = ParseResult()
        left = result.register(func())
        if result.error:  return result

        while self.current_token.token_type in operation_tokens:
            operation_token = self.current_token
            result.register(self.advance())
            right = result.register(func())
            if result.error: return result
            left = BinaryOperationNode(left, operation_token, right)

        return result.success(left)

    def term(self):
        return self.binary_operation(self.factor, (TT_MUL, TT_DIV))

    def expression(self):
        return self.binary_operation(self.term, (TT_PLUS, TT_MINUS))

    def parse(self):
        result = self.expression()
        if not result.error and self.current_token.token_type != TT_EOF:
            return result.failure(InvalidSyntaxError(
                self.current_token.pos_start, self.current_token.pos_end, "Expected '+', '-', '*', or '/'")
            )
        return result

