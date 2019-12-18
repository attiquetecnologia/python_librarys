# -*- coding: utf-8 -*-

__author__ = "Rodrigo Attique Santana"
__email__ = "rodrigoattique@gmail.com"
__since__ = "2019/12/18"

# Example to order in tree structure a list sequence with father and son

# The dict represents a sql result query
arvore_sequence = {
    1: {"id":1, "name":'Paul', "father": None}
    ,2: {"id":2, "name":'Anna', "father": None}
    ,3: {"id":3, "name":'Kassie', "father": None}
    ,4: {"id":4, "name":'Jackie', "father": 1}
    ,5: {"id":5, "name":'Charlee', "father": 1}
    ,6: {"id":6, "name":'Charlee III', "father": 5}
    ,7: {"id":7, "name":'Klair', "father": 2}
    ,8: {"id":8, "name":'George', "father": 3}
}

# To transform a data sequence in tree structure
# The algorithm make many iteraction in list
# The first element it's the fathers in first iteraction.
# The others will get childreen of fathers until clean the list.

# Pre order algorithm
def pre_order(node):
    for k, v in arvore_sequence.items():
        if node['id'] == v['father']:
            if 'childreen' not in node:
                node['childreen'] = {}
            node['childreen'][k] = v
            del arvore_sequence[k]
            pre_order(v)

roots = {}

# Filter fathers
for k, v in arvore_sequence.items():
    if v['father']==None:
        del arvore_sequence[k]
        # Now search by son
        pre_order(v)
        roots[k] = v

import json
print(json.dumps(roots))
with open('tree_organize.json', 'w') as f:
    f.write(json.dumps(roots))