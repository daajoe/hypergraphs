#!/usr/bin/env python
from optparse import OptionParser
import select
from sys import stderr, stdin, stdout
import networkx as nx

def iter_islast(iterable):
    it = iter(iterable)
    prev = it.next()
    for item in it:
        yield prev, False
    prev = item
    yield prev, True

    
fromfile=True
if select.select([stdin,],[],[],0.0)[0]:
    inp=stdin
    fromfile=False
else:
    parser = OptionParser()
    parser.add_option('-f', '--file', dest='filename',
                  help='Input file', metavar='FILE')
    (options, args) = parser.parse_args()
    if not options.filename:
        stderr.write('Missing filename')
        parser.print_help(stderr)
        stderr.write('\n')
        exit(1)
    inp = open(options.filename, 'r')
    fromfile=True

    
G = nx.Graph()
line_number=1
for line in inp.readlines():
    line=line.split()
    if line==[]:
        continue
    if line[0] == 'c':
        # stdout.write('%s\n' %' '.join(line))
        continue
    if line[0]=='p':
        continue
    if line[0]=='e':
        G.add_edge(int(line[1]), int(line[2]))

for i, (edge,last) in enumerate(iter_islast(G.edges())):
    edge = map(lambda x: 'v%s' %x, edge)
    eol_symbol = '.' if last else ','
    stdout.write('e%i(%s)%s\n'%(i,",".join(edge), eol_symbol))

    
if fromfile:
    inp.close()

try:
    stdout.close()
except:
    pass

try:
    stderr.close()
except:
    pass
