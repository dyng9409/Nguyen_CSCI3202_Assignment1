#implementation of a binary tree

class node(object):

    def __init__(self, key):
        #create node only specifying the key value
        #assignment of parent and children will be handled by methods

        self.key = key
        self.parent = None
        self.lchild = None
        self.rchild = None

    #utility functions to modify nodes

    def addLChild(self, child):
        self.lchild = child
        child.parent = self

    def addRChild(self, child):
        self.rchild = child
        child.parent = self

class tree(object):

    def __init__(self, root):
        #tree object holds the 'root' of the tree
        self.root = root

    #utility functions
    def getLSubTree(self):
        #returns a tree object created from the left subtree
        if self.root.lchild is None:
            return tree(None)
        else:
            return tree(self.root.lchild)

    def getRSubTree(self):
        #returns a tree object created from the right subtree
        if self.root.rchild is None:
            return tree(None)
        else:
            return tree(self.root.rchild)
    def find(self, val):
        #finds the node with the associated key value
        #if no node is found, returns None

    def add(self, pval, chval):
        #add node, returns 0 if no add was made, returns 1 if add was succesful
        curVal = self.root.key
        lSub = self.getLSubTree()
        rSub = self.getRSubTree()

        if self.root is None:
            return 
        else if (curVal == pval):
            if self.root.lchild is None:
                newNode = node(chval)
                self.root.addLChild(newNode)
                return 
            else if self.root.rchild is None:
                newNode = node(chval)
                self.root.addRChild(newNode)
                return 
            else:
                print("Parent has two children, node not added")
                return 
        else:
            lSub.add(pval, chval)
    #def delete(self, val):
        #TODO

    #def print(self):
        #TODO
