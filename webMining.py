# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from lxml.html import parse
from urllib2 import urlopen
import re
# web scraping modules

import matplotlib.pyplot as plt
import networkx as nx
# graph and plotting modules

G=nx.Graph()
# create graph

# <codecell>

root = 'http://www.the-adam.com/'
absolute_path = set([root])
stack = [root]

# <codecell>

def findLinks(parent):
    try:
        parsed = parse(urlopen(parent))
    except:
        print 'dead link @: '
        return

    newLinks = []
    
    doc = parsed.getroot()
    for i in doc.findall('.//a'):
        t = i.get('href')
        if type(t) == str:
            newLinks.append(t)
    
    s = parent
    
    cleanLinks = [i for i in newLinks if not re.match(r"http",i)]
    abs_path = [s+i for i in cleanLinks if re.match(r"\w", i)]
    abs_path.extend([s+j[3:] for j in cleanLinks if re.match(r"\W",j)])
    
    return set(abs_path)  

# <codecell>

stack

# <codecell>

t = findLinks(stack.pop())
stack.extend(t)
absolute_path = absolute_path.union(t)
stack

# <codecell>

t = findLinks(stack.pop())
if t:
    stack.extend(t)
    absolute_path = absolute_path.union(t)
    stack

# <codecell>

t = findLinks(stack.pop())
if t:
    stack.extend(t)
    absolute_path = absolute_path.union(t)
    stack

# <codecell>

t = findLinks(stack.pop())
if t:
    stack.extend(t)
    absolute_path = absolute_path.union(t)
    stack

# <codecell>

t = findLinks(stack.pop())
if t:
    stack.extend(t)
    absolute_path = absolute_path.union(t)
    stack, absolute_path

# <codecell>


