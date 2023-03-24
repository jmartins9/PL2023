import ply.lex as lex


tokens = (
    "INITCOMMENT", # '/*' 
    "CLOSECOMMENT", # '*/' 
    "COMMENT", # '//'
    "INT",
    "ID",
    "PVIR",
    "FUNCTION",
    "PROGRAM",
    "OPERATOR",
    "ATRIB",
    "FOR",
    "WHILE",
    "APC",
    "FPC",
    "APR",
    "FPR",
    "ABREV",
    "VR",
    "ACH",
    "FCH",
    "NUM",
    "IN",
    "IF"
)

t_NUM = r'\d+'
t_ID = r'\w+'
t_OPERATOR = r'[*\-><]'
t_ABREV = r'\.\.'
t_ATRIB = r'='
t_PVIR = r';'
t_APC = r'\('
t_FPC = r'\)'
t_APR = r'\['
t_FPR = r']'
t_VR = r','
t_ACH = r'{'
t_FCH = r'}'

states = (
    ('commentml', 'exclusive'), # Comment multi line
    ('commentl', 'exclusive') # Comment single line
)

def t_INT(t):
    r'\bint\b'
    return t

def t_IN(t):
    r'\bin\b'
    return t

def t_IF(t):
    r'\bif\b'
    return t
    
def t_WHILE(t):
    r'\bwhile\b'
    return t

def t_FOR(t):
    r'\bfor\b'
    return t

def t_FUNCTION(t):
    r'\bfunction\b'
    return t

def t_PROGRAM(t):
    r'\bprogram\b'
    return t


# Init comment multi line state
def t_INITCOMMENT(t):
    r'/\*'
    t.lexer.begin('commentml')
    return t

# Close comment multi line, begin initial state
def t_commentml_CLOSECOMMENT(t):
    r'\*/'
    t.lexer.begin('INITIAL')
    return t

# Ignore all the caracteres in the multi line comment
def t_commentml_ANY(t):
    r'(.|\n)'
    pass

# Init comment single line state
def t_COMMENT(t):
    r'//'
    t.lexer.begin('commentl')
    return t

# Close comment single line with a new line caracter, begin initial state
def t_commentl_newline(t):
    r'\n'
    t.lexer.begin('INITIAL')

# Ignore all the caracteres in the single line comment
def t_commentl_ANY(t):
    r'.'
    pass

# Ignore caracteres for the initial state
t_ignore = ' \n\t'

# Ignore caracteres for the comment multi line state
t_commentml_ignore = ''

# Ignore caracteres for the comment state
t_commentl_ignore = ''

# Error rule for the initial state
def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

# Error rule for the comment multi line state
def t_commentml_error(t):
    pass

# Error rule for the comment state
def t_commentl_error(t):
    pass

# Build the lexer
lexer = lex.lex()


data = """
/* max.p: calcula o maior inteiro duma lista desordenada
-- 2023-03-20 
-- by jcr
*/

int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};

// Programa principal
program myMax{
  int max = a[0];
  for i in [1..9]{
    if max < a[i] {
      max = a[i];
    }
  }
  print(max);
}
"""

lexer.input(data)

for tok in lexer:
    print(tok)

