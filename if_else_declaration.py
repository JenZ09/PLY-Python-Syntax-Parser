import ply.lex as lex
import ply.yacc as yacc

tokens=[
            'IF', 'ELSE', 'TRUE', 'FALSE', 'FOR', 'IN', 'ID', 'COLON', 'LPAREN', 'RPAREN',
            'NUMBER', 'COMMA', 'GREATER', 'LESS', 'EQUALS', 'NOT', 'AND', 'OR'
        ]

reserved={
            'for': 'FOR',
            'in': 'IN',
            'if': 'IF',
            'else': 'ELSE',
            'true': 'TRUE',
            'false': 'FALSE'
        }

t_COLON = r':'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NUMBER = r'\d+'
t_COMMA = r','

t_GREATER = r'>'
t_LESS = r'<'
t_EQUALS = r'=='
t_NOT = r'!='
t_AND = r'&&'
t_OR = r'\|\|'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def p_if_statement(p):
    '''if_statement : IF LPAREN expression RPAREN COLON statement
                    | IF LPAREN expression RPAREN COLON statement ELSE COLON statement'''
    if len(p) == 8:
        print(f"Successfully parsed if-else statement")
    else:
        print(f"Successfully parsed if statement")

def p_expression_comparison(p):
    '''expression : ID GREATER ID
                  | ID LESS ID
                  | ID EQUALS ID
                  | ID NOT EQUALS ID'''
    p[0] = (p[1], p[2], p[3])

def p_expression_boolean(p):
    '''expression : TRUE
                  | FALSE'''
    p[0] = p[1]

def p_expression_id(p):
    '''expression : ID'''
    p[0] = p[1]

def p_statement(p):
    '''statement : ID'''
    pass

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at end of input")

parser = yacc.yacc()

data = input("Enter an if or if-else body: ")
parser.parse(data)
