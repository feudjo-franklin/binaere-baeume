import pa01

nodeRLR = pa01.Node(4,None,None)
nodeRL = pa01.Node(3,None,nodeRLR)
nodeRR = pa01.Node(7,None,None)
nodeL = pa01.Node(5,None,None)
nodeR = pa01.Node(2,nodeRL,nodeRR)
bin1 = pa01.Node(1,nodeL,nodeR)

print(bin1.keys())
