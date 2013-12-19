from rply import LexerGenerator

lg = LexerGenerator()
lg.add('INT', r'\d+')
lg.add('LPAR', r'\(')
lg.add('RPAR', r'\)')
lg.add('COLON', r':')
lg.add('COMMA', r',')
lg.add('ID', r'[a-zA-Z_][a-zA-Z0-9_]*')
lg.ignore(r'\s+')

lexer = lg.build()
