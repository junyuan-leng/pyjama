#!/usr/bin/env python
#coding = utf-8

def parseImport(s):
	'''
	import aaa[.bbb] [as ddd]
	from aaa[.bbb] import ccc [as ddd]
	'''
	tokens = s.strip().replace(',', ' ').split()#TODO: handle 'import a, b, c'
	try:
		index_of_from = tokens.index('from')
	except ValueError:
		index_of_from = 0
	try:
		index_of_import = tokens.index('import')
	except ValueError:
		print "Not a legal import sentence"
	try:
		index_of_as = tokens.index('as')
	except ValueError:
		index_of_as = len(tokens)
	return ('.').join(list(tokens[index_of_from + 1 : index_of_import] + tokens[index_of_import + 1: index_of_as]))

if __name__ == '__main__':
	s1 = "import a"
	s2 = "import a.b as c"
	s3 = "from a import b"
	s4 = "from a.b import c as d"
	print parseImport(s1)
	print parseImport(s2)
	print parseImport(s3)
	print parseImport(s4)