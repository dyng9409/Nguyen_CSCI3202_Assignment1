#Dylan Nguyen
#University of Colorado - Boulder
#CSCI 3202 Fall 2015 Assignment 1
#Implementation of Various Data Structures

from __future__ import print_function
import sys
import q
import stack as s
import graph as g
import tree as t

#testing the implementations


def testDequeueOrder(queue):
    #dequeues items from queue and prints in order
    while(not queue.isEmpty()):
        print(queue.pop(),end=' ')
    print('\n')
    return

def testUnstackOrder(stack):
    while(not stack.isEmpty()):
        print(stack.pop(),end=' ')
    print('\n')
    #unstacks items from stack and prints in order
    return

#-----TESTING QUEUE-----#

#initializing queue with 0 1 2 3 4 5 6 7 8 9
testQ = q.queue()
for i in range(0,10):
    testQ.push(i)

#output should be 0 1 2 3 4 5 6 7 8 9
testDequeueOrder(testQ)
#queue should be empty after test
assert(testQ.isEmpty() is True)

#-----TESTING STACK-----#
testStack = s.stack()
for i in range(0,10):
    testStack.push(i)
#stack should now have 0 1 2 3 4 5 6 7 8 9 in it

#output should be 9 8 7 6 5 4 3 2 1 0
testUnstackOrder(testStack)

assert(testQ.isEmpty() is True)
#stack should now be empty
#tests push, pop, and empty

#-----TESTING TREE-----#
testTree = t.tree()
#initializing the tree
testTree.addRoot(42)
testTree.add(42,2)
testTree.add(42,5)
testTree.add(5,7)
testTree.add(5,10)
testTree.add(2,13)
testTree.add(2,21)
testTree.add(21,12)
testTree.add(13,11)
testTree.add(10,16)
testTree.add(16,6)

#testing print tree
#feeding in above tree, output should be:
#42 2 13 11 21 12 5 7 10 16 6
testTree.printTree()
print('\n')

#testing add with non existant parent
testTree.add(1337,2)

#testing add with full node
testTree.add(2,56)

#testing the delete function with same tree
#first trying to delete a node with children should result in 
#error messages being displayed:

#node 2 has children 13 and 21, so will show an error
testTree.delete(2)

#node 16 has 1 child so will show an error
testTree.delete(16)

#node 6 and 11 are leafs so will show no error
testTree.delete(11)
testTree.delete(6)

#confirming that those nodes are deleted using the
#find method (also confirms nodes are no longer pointed to)
assert(testTree.find(11) is None)
assert(testTree.find(6) is None)

#printing tree again, confirming delete
#output should be: 42 2 13 21 12 5 7 10 16
testTree.printTree()

#-----TESTING GRAPH-----#
testGraph = g.graph()

#initializing graph

