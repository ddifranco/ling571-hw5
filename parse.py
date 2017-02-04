#!/bin/python3.4

import nltk
import sys
import re
import pdb

grammar = nltk.data.load(sys.argv[1])
tests   = nltk.data.load(sys.argv[2])

p = nltk.parse.EarleyChartParser(grammar)
#f = open(sys.argv[3], 'w')

blank = re.compile('^[ ]?[\r]?[\n]?$')
skip = re.compile('^@')

for s in tests.split('\n'):
	if re.match(blank, s) or re.match(skip, s):
		continue
	#f.write(s+'\n')
	tkns = nltk.word_tokenize(s)
	sys.stdout.write(s+'\n')

	try:
		example = p.parse(tkns).next()
	except:
		sys.stdout.write('\tFAIL\n')
		continue

	sys.stdout.write('\tPASS\n')
