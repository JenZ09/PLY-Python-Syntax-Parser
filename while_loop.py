import ply.lex as lex
import ply.yacc as yacc

tokens=(
            'LPAREN', 'RPAREN', 'COLON', 'NUMBER', 'IDENTIFIER', 'EQ',
            'GT', 'LT', 'GE', 'LE'
        )

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r':'
t_EQ = r'=='
t_GT = r'>'
t_LT = r'<'
t_GE = r'>='
t_LE = r'<='
t_ignore = ' \t'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def p_statement_while(p):
    '''statement : IDENTIFIER LPAREN expression RPAREN COLON single_statement'''
    
    if p[1] == 'while':
        p[0] = ('while', p[3], p[5])
    else:
        print("Syntax error: Expected 'while'")
        p[0] = None

def p_expression(p):
    '''expression : IDENTIFIER
                  | IDENTIFIER EQ IDENTIFIER
                  | IDENTIFIER EQ NUMBER
                  | IDENTIFIER GT IDENTIFIER
                  | IDENTIFIER GT NUMBER
                  | IDENTIFIER LT IDENTIFIER
                  | IDENTIFIER LT NUMBER
                  | IDENTIFIER GE IDENTIFIER
                  | IDENTIFIER GE NUMBER
                  | IDENTIFIER LE IDENTIFIER
                  | IDENTIFIER LE NUMBER'''
    if len(p) == 2:
        p[0] = ('id', p[1])
    else:
        p[0] = (p[2], p[1], p[3]) 

def p_single_statement(p):
    'single_statement : IDENTIFIER'
    p[0] = p[1]

def p_error(p):
    print("Syntax error at '%s'" % p.value if p else "Syntax error at EOF")

parser = yacc.yacc()

input_data = input("Enter a while loop statement: ")

result = parser.parse(input_data)

if result:
    print("Correct syntax!")
else:
    print("Incorrect syntax.")
