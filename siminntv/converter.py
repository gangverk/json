import json
import sys

if len(sys.argv) == 1:
	print "You need to at least provide a source file, optional width and height of source screen"
	exit()

source = sys.argv[1]

origin_height = 544
if len(sys.argv) > 2:
	origin_width = sys.argv[2]


xparams = set(["width","x","horizontal-spacing"])
yparams = set(["height","y","vertical-spacing"])

def loop(itemlist):
	for v in itemlist:
		if isinstance(v,dict):
			traverse(v)

def traverse(node):
	for k,v in node.iteritems():
		if k in yparams:
			node[k] = float(v)/float(origin_height)
		elif k in xparams:
			node[k] = float(v)/float(origin_height)
		elif isinstance(v,dict):
			traverse(v)
		elif isinstance(v,list):
			loop(v)


d = json.loads(open(source).read())
traverse(d)
print json.dumps(d, sort_keys=True,indent=4, separators=(',', ': '))
