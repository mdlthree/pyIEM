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


# <codecell>

def findLinks(parent):
    s = parent.lower()
    try:
        parsed = parse(urlopen(parent))
    except:
        return None

    newLinks = []
    
    doc = parsed.getroot()
    for i in doc.findall('.//a'):
        t = i.get('href')
        if type(t) == str:
            newLinks.append(t)
    
    cleanLinks = [i for i in newLinks if not re.match(r"http",i) ]
    cleanLinks = [i for i in cleanLinks if not re.match(r"../",i) ]
    cleanLinks = [i for i in cleanLinks if not re.match(r"mailto",i) ]
    cleanLinks = [i for i in cleanLinks if not re.match(r"#",i) ]
    v = len(s) - len(re.split(r"/",s)[-1])
    abs_path = [ s[:v]+i for i in cleanLinks ] 
    return set(abs_path)  

# <codecell>

root = 'http://www.the-adam.com/'
absolute_path = set()
stack = [root]

G=nx.Graph()
# create graph

stack

# <codecell>

pop = stack.pop()

if pop not in absolute_path:
    absolute_path.add(pop)
    G.add_node(pop)
    t = findLinks(pop)
    if t is not None:
        stack.extend(t)
        
        for v in t:
            G.add_node(v)
            G.add_edge(pop, v)

#print len(stack), len(absolute_path)

nx.draw(G, with_labels=False)
plt.show() # display

# <codecell>

while len(stack) > 0:
    pop = stack.pop()
    
    if pop not in absolute_path:
        absolute_path.add(pop)
        G.add_node(pop)
        t = findLinks(pop)
        if t is not None:
            stack.extend(t)
            
            for v in t:
                G.add_node(v)
                G.add_edge(pop, v)
    
    print len(stack), len(absolute_path)

# <codecell>

len(absolute_path)

# <codecell>

nx.draw(G, with_labels=False, node_size=50)
plt.figure(figsize=(15,12))
plt.show() # display

# <codecell>


