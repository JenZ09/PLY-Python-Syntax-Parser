import ply.lex as lex
import ply.yacc as yacc
import sys
tokens=(
            'DEF',          
            'IDENTIFIER',   
            'LPAREN',       
            'RPAREN',       
            'COMMA',      
            'COLON',       
        )
def t_DEF(t):
    r'def'
    return t
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_COLON = r':'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    sys.exit(1)  

lexer = lex.lex()

def p_function_declaration(p):
    'function_declaration : DEF IDENTIFIER LPAREN parameters RPAREN COLON'
    print("Function declaration parsed successfully!")

def p_parameters(p):
    '''parameters : IDENTIFIER
                  | IDENTIFIER COMMA parameters
                  | empty'''
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:	
        print("Syntax error at end of input")
    sys.exit(1)  

parser = yacc.yacc()
user_input = input("Enter a function declaration: ")
parser.parse(user_input)
