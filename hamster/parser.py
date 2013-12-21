from rply import ParserGenerator

pg = ParserGenerator(('INT', 'LPAR', 'RPAR', 'COMMA', 'ID'))

@pg.production('main : expr')
def main(p):
	return p[0]

@pg.production('expr : INT')
def expr_int(p):
	return int(p[0].getstr())

@pg.production('expr : LPAR ID params RPAR')
def expr_call(p):
	id = p[1].getstr()
	args = p[2]
	if id == 'add':
		return sum(args)
	if id == 'sub':
		if len(args) == 1:
			return -args[0]
		else:
			return args[0] - sum(args[1:])

@pg.production('params : expr COMMA params')
def params_rec(p):
	return [p[0]] + p[2]

@pg.production('params : expr')
def params_expr(p):
	return [p[0]]

parser = pg.build()
