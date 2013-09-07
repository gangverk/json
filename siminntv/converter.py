import json
import sys

if len(sys.argv) == 1:
	print "You need to at least provide a source file and optional height of source screen"
	exit()

source = sys.argv[1]

origin_height = 544
if len(sys.argv) > 2:
	print "setting height to ", sys.argv[2]
	origin_height = int(sys.argv[2])



params = set(["width","height","x","y","horizontal-spacing","vertical-spacing"])

def loop(itemlist):
	for v in itemlist:
		if isinstance(v,dict):
			traverse(v)
		elif isinstance(v,list):
			loop(v)

def traverse(node):
	for k,v in node.iteritems():
		if k in params:
			node[k] = round(float(v)/float(origin_height),3)
		elif isinstance(v,dict):
			traverse(v)
		elif isinstance(v,list):
			loop(v)


d = json.loads(open(source).read())
if isinstance(d,dict):
	traverse(d)
elif isinstance(d,list):
	loop(d)
else:
	print "What the hell is this:",type(d)


print json.dumps(d, sort_keys=True,indent=4, separators=(',', ': '))
