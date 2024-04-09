import ply.lex as lex
import re

# List of token names.   This is always required
tokens = (
   'SELECT',
   'FROM',
   'WHERE',
   'VARIABLE',
   'COMMA',
   'NUMBER',
   'OPERATOR'
)

# Regular expression rules for the tokens
t_SELECT = r'SELECT'
t_FROM = r'FROM'
t_WHERE = r'WHERE'
t_COMMA = r','
t_OPERATOR = r'(<|>|=)+'

def t_NUMBER(t):
    r'(\+|-)?\d+'
    t.value = int(t.value)    
    return t

t_VARIABLE  = r'\w+'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Test it out
data = 'SELECT id, nome, salario FROM empregados WHERE salario>=820'

def main():
    lexer = lex.lex()
    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)


if __name__ == '__main__':
    main()