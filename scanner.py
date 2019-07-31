# encoding: utf-8

import logging

from tokens import Token, TokenType


class Scanner(object):
    """
    is used to read source code and produce tokens for parser.
    """

    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 0

    def is_end(self):
        return self.current >= len(self.source)

    def advance(self):
        self.current += 1
        return self.source[self.current-1]

    def add_token(self, token_type, literal=None):
        text = self.source[self.start:self.current]
        self.tokens.append(Token(token_type, text, literal, self.line))

    def match(self, expect):
        if self.is_end():
            return False
        
        if self.source[self.current] != expect:
            return False
        
        self.current += 1
        return True

    def scan_token(self):
        token_types = {
            '(': TokenType.LEFT_PAREN,
            ')': TokenType.RIGHT_PAREN,
            '{': TokenType.LEFT_BRACE,
            '}': TokenType.RIGHT_BRACE,
            ',': TokenType.COMMA,
            '.': TokenType.DOT,
            '-': TokenType.MINUS,
            '+': TokenType.PLUS,
            ';': TokenType.SEMICOLON,
            '*': TokenType.STAR
        }

        char = self.advance()
        token_type = token_types.get(char)
        if token_type is not None:
            self.add_token(token_type)
            return
        
        if char == '!':
            tk = TokenType.BANG_EQUAL if self.match('=') else TokenType.BANG
            self.add_token(tk)
        elif char == '=':
            tk = TokenType.EQUAL_EQUAL if self.match('=') else TokenType.EQUAL
            self.add_token(tk)
        elif char == '<':
            tk = TokenType.LESS_EQUAL if self.match('=') else TokenType.LESS
            self.add_token(tk)
        elif char == '>':
            tk = TokenType.GREATER_EQUAL if self.match('=') else TokenType.GREATER
            self.add_token(tk)
        else:
            msg = 'Unexpected character: {char} at line: {line_num}'.format(char=char, line_num=self.line)
            logging.error(msg)
            return

    def scan_tokens(self):
        while not self.is_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens


if __name__ == "__main__":
    print("Scanner")

    source = '.({+, -, *}).==,!=,>,>=,<,<='
    scanner = Scanner(source)
    for tk in scanner.scan_tokens():
        print(tk)

