class Node:
    def __init__(self, key, leftChild=None, rightChild=None):
        self.key = key
        self.leftChild = leftChild
        self.rightChild = rightChild
    #Aus der Breitensuche ausgedacht
    def keys(self):
        """
        Listet alle Knotenschlüssel des Baums auf

        @return: List  die Liste der Knotenschlüssel des Baums
        """
        R = [self.key] #Die Liste aller erreichbaren Knotenschlüssel
        Q = [self]  #Die Liste der Knoten von denen ich nach neuen Knoten weitersuchen kann
        
        while not Q == []:
            v = Q[-1]
            #Die zwei adjazenten Knoten des Knoten v
            lc = v.leftChild
            rc = v.rightChild
            if lc != None:
                R.append(lc.key)
                Q.insert(0, lc)

            if rc != None:
                R.append(rc.key)
                Q.insert(0, rc)

            Q.pop() #Da ich keinen neuen Knoten gefunden habe
            

        return R
    #Aus der Breitensuche ausgedacht
    def height(self):
        """
        gib die Höhe des Knoten in seinem Baum zurück

        @return: int  die Höhe des Knoten in seinem Baum
        """
        R = [0] #Die Liste aller Länge zwischen der Wurzel und jedem einzelnen Knoten
        Q = [self]   #Die Liste der Knoten von denen ich nach neuen Knoten weitersuchen kann
        i = 0
        while not Q == []:
            v = Q[-1]
            #Die zwei adjazenten Knoten des Knoten v
            lc = v.leftChild
            rc = v.rightChild
            if lc != None:
                R.append(R[i]+1) #Jedes Mal, dass ein neuer Knoten gefunden wird, wird die Länge der vorherigen Knoten
                Q.insert(0, lc)  #der zu diesem neuen Knoten geführt hat, inkrementiert und zu R hinzugefügt

            if rc != None:
                R.append(R[i]+1)  #Jedes Mal, dass ein neuer Knoten gefunden wird, wird die Länge der vorherigen Knoten
                Q.insert(0, rc)   #der zu diesem neuen Knoten geführt hat, inkrementiert und zu R hinzugefügt

            Q.pop()
            i+=1
        return max(R)
            


    #Ausgedacht aus der Breitensuche    
    def leaves(self):
        """
        Listet die Schlüssel der Blätter des Baums auf

        @return: List  die Liste der Schlüssel der Blätter des Baums auf
        """
        R = []  #Die Liste aller  Schlüssel der Blätter des Baums
        Q = [self]   #Die Liste der Knoten von denen ich nach neuen Knoten weitersuchen kann
        if self.leftChild == None and self.rightChild == None: # wenn der Baum nur aus der Wurzel besteht
            R.append(self.key)
        else:
            while not Q == []:
                v = Q[-1]
                #Die zwei adjazenten Knoten des Knoten v
                lc = v.leftChild
                rc = v.rightChild
                if lc != None:
                    Q.insert(0, lc)
                    if lc.leftChild == None and lc.rightChild == None: #Prüfen ob dieser Adjazent Knoten keine Kinder hat
                        R.append(lc.key) #wenn True, ist er ein Blatt, und sein Schlüssel wird gespeichert
                        

                if rc != None:
                    Q.insert(0, rc)
                    if rc.leftChild == None and rc.rightChild == None:#Prüfen ob dieser Adjazent Knoten keine Kinder hat
                        R.append(rc.key) #wenn True, ist er ein Blatt, und sein Schlüssel wird gespeichert 

                Q.pop()
        return R
"""        
nodeRLR = Node(4,None,None)
nodeRL = Node(3,None,nodeRLR)
nodeRR = Node(7,None,None)
nodeL = Node(5,None,None)
nodeR = Node(2,nodeRL,nodeRR)
bin1 = Node(1,nodeL,nodeR)
#print(bin1.keys())
#print(bin1.leaves())
#print(bin1.height())
print(nodeRL.height())
#test2
nodeLL = Node(7,None,None)
nodeL = Node(5,nodeLL,None)
nodeRL = Node(3,None,None)
nodeR = Node(2,nodeRL,None)
bin2 = Node(0,nodeL,nodeR)
#print(bin2.keys())
#print(bin2.leaves())
#print(bin2.height())
print(nodeLL.height())
node1 = Node(1)
node2 = Node(2,node1,None)
node7 = Node(7)
node5 = Node(5,node2,node7)
print(node5.keys())
"""
