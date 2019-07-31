# encoding: utf-8

from enum import Enum


class TokenType(Enum):
    """
    token types 
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

    IDENTIFIER = 20  ## 标识符(变量名，函数名, 类名)
    STRING = 21  # 字符串
    NUMBER = 22  # 数字

    # key words
    AND = 23  # &&
    OR = 24  # ||
    IF = 25  # if
    ELSE = 26  # else
    FOR = 27  # for
    WHILE = 28  # while
    TRUE = 29  # true
    FALSE = 30  # false

    VAR = 31  # var
    NIL = 32  # nil
    FUNC = 33  # func
    PRINT = 34  # print
    RETURN = 35  # return
    THIS = 36  # this
    SUPER = 37  # super

    EOF = 38  # eof


class Token(object):
    """
    A lexical token or simply token is a string with an assigned and thus identified meaning. 
    It is structured as a pair consisting of a token name and an optional token value. 
    The token name is a category of lexical unit.
    
    [2] Common token names are:
    identifier: names the programmer chooses;
    keyword: names already in the programming language;
    separator (also known as punctuators): punctuation characters and paired-delimiters;
    operator: symbols that operate on arguments and produce results;
    literal: numeric, logical, textual, reference literals;
    comment: line, block.
    """
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
