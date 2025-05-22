import ply.lex as lex
import ply.yacc as yacc

tokens=(
            'NAME',
            'NUMBER',
            'FLOAT',
            'LBRACKET',
            'RBRACKET',
            'COMMA',
            'EQUALS',
            'STRING',
            'SEMICOLON',
        )

t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_EQUALS = r'='
t_SEMICOLON = r';'

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)  
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  
    return t

def t_STRING(t):
    r'("([^\\"]|\\.)*")|(\'([^\\\']|\\.)*\')'  
    t.value = t.value[1:-1]  
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

syntax_correct = True  

def p_list_declaration(p):
    '''list_declaration : NAME EQUALS LBRACKET list_elements RBRACKET optional_semicolon'''

def p_list_elements(p):
    '''list_elements : list_element
                     | list_elements COMMA list_element'''
    if len(p) == 2:
        p[0] = [p[1]]  
    else:
        p[0] = p[1] + [p[3]]  

def p_list_element(p):
    '''list_element : NAME
                    | NUMBER
                    | FLOAT
                    | STRING'''
    p[0] = p[1]

def p_optional_semicolon(p):
    '''optional_semicolon : SEMICOLON
                          | empty'''
    pass  

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    global syntax_correct
    syntax_correct = False
    print("Syntax error at '%s'" % p.value if p else "Syntax error at EOF")

parser = yacc.yacc()

test_input = input("Enter a Python list declaration: ")

lexer.input(test_input)
parser.parse(test_input)

if syntax_correct:
    print("Correct syntax!")
else:
    print("Incorrect syntax!")
