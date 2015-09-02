#implementation of a binary tree

class node(object):

    def __init__(self, key):
        #create node only specifying the key value
        #assignment of parent and children will be handled by methods
        if type(key) is not int:
            print("Error, key must be of type (int)")
            return
        self.key = key
        self.parent = None
        self.lchild = None
        self.rchild = None

    #utility functions to modify nodes
    #setting a child will automatically set the child's parent

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
    def isEmpty(self):
        if(self.root is None):
            return True
        else:
            return False

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
            self.root = node(root)
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
        #deletes the specified node if it is found
        #prints error if not or node is unable to be deleted

        target = self.find(val)
        if target is None:
            print("Node not found")
            return

        #only case where the target parent would be none is root
        #so this is an edge case
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
        #basic DF traverse and print
        if self.root is None:
            return
        print(self.root.key),
        lSub = self.getLSubTree()
        rSub = self.getRSubTree()

        lSub.printTree()
        rSub.printTree()
        return
