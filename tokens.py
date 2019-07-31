# encoding: utf-8

from enum import Enum


class TokenType(Enum):
    """
    token types
    COMMA, DOT, MINUS, PLUS, SEMICOLON, SLASH, STAR, 
    BANG, BANG_EQUAL,                                
    EQUAL, EQUAL_EQUAL,                              
    GREATER, GREATER_EQUAL,                          
    LESS, LESS_EQUAL, 
    IDENTIFIER, STRING, NUMBER, 

    AND, CLASS, ELSE, FALSE, FUN, FOR, IF, NIL, OR,  
    PRINT, RETURN, SUPER, THIS, TRUE, VAR, WHILE,    

    EOF 
    """

    LEFT_PAREN = 1  # (
    RIGHT_PAREN = 2  # )

    LEFT_BRACE = 3  # {
    RIGHT_BRACE = 4  # }

    COMMA = 5  # ,
    DOT = 6  # .
    MINUS = 7  # -
    PLUS = 8  # +
    SEMICOLON = 9  # ;
    SLASH = 10  # /
    STAR = 11  # *

    BANG = 12  # !
    BANG_EQUAL = 13 # !=
    EQUAL = 14  # =
    EQUAL_EQUAL = 15  # ==
    GREATER = 16  # >
    GREATER_EQUAL = 17 # >=
    LESS = 18  # <
    LESS_EQUAL = 19 # <=

    IDENTIFIER = 20  ## 标识符
    STRING = 21  # 字符串
    NUMBER = 22  # 数字

    AND = 23  # &&
    OR = 24  # ||
    IF = 25  # if
    ELSE = 26  # else
    FOR = 27  # for
    WHILE = 28  # while
    TRUE = 29  # true
    FALSE = 30  # false

    VAR = 31  # var
    


class Token(object):
    def __init__(self, token_type, lexeme, literal, line_num):
        self.token_type = token_type
        self.lexeme = lexeme
        self.literal = literal
        self.line_num = line_num

    def __repr__(self):
        return '<{token_type}, {lexeme}, {literal}, {line_num}>'.format(
            token_type=self.token_type,
            lexeme=self.lexeme,
            literal=self.literal,
            line_num=self.line_num
        )


if __name__ == "__main__":
    for tokenType in TokenType:
        print(tokenType)

    t = Token(TokenType.LEFT_BRACE, '(', '(', 1)
    print(t)
