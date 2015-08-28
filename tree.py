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

    def __init__(self, root=None):
        #tree object holds the 'root' of the tree
        if root is None:
            self.root = None
        else:
            self.root = root

    #utility functions
    def getLSubTree(self):
        #returns a tree object created from the left subtree
        #if there is no left subtree, then returns a tree rooted with None (i.e. an empty tree)
        if self.root.lchild is None:
            return tree(None)
        else:
            return tree(self.root.lchild)

    def getRSubTree(self):
        #returns a tree object created from the right subtree
        #if there is no right subtree, then returns a tree rooted with None (i.e. an empty tree)
        if self.root.rchild is None:
            return tree(None)
        else:
            return tree(self.root.rchild)
    def addRoot(self, root):
        #add a root if starting with an empty tree
        #first check if root alreayd exists

        if self.root is not None:
            print("Tree already has root")
        else:
            self.root = root
        return
    def find(self, val):
        #finds the node with the associated key value
        #if no node is found, returns None
        #otherwise returns the node
        
        if self.root is None:
            return None

        lSub = self.getLSubTree()
        rSub = self.getRSubTree()

        if self.root.key == val:
            return self.root

        lSubResult = lSub.find(val)
        if lSubResult is None:
            return rSub.find(val)
        else:
            return lSubResult


    def add(self, pval, chval):
        #add node, returns 0 if no add was made, returns 1 if add was succesful
        curVal = self.root.key

        target = self.find(pval)

        if target is None:
            print("Parent not found")
        elif target.lchild is None:
            newNode = node(chval)
            target.addLChild(newNode)
        elif target.rchild is None:
            newNode = node(chval)
            target.addRChild(newNode)
        else:
            print("Parent has two children. Node not added")

        return

    def delete(self, val):
        target = self.find(val)
        if target is None:
            print("Node not found")
            return
        if target.parent is not None:
            parent = target.parent
            plchild = target.parent.lchild
            prchild = target.parent.rchild

        if (target.lchild is None) and (target.rchild is None):
            if plchild is None:
                parent.rchild = None
                target.parent = None
            elif plchild.key == target.key:
                parent.lchild = None
                target.parent = None
            else:
                parent.rchild = None
                target.parent = None

        else:
            print("Node has children you monster, cannot delete node")

        return

    def printTree(self):
        if self.root is None:
            return
        print(self.root.key)
        lSub = self.getLSubTree()
        rSub = self.getRSubTree()

        lSub.printTree()
        rSub.printTree()
        return
