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
    return

def testUnstackOrder(stack):
    while(not stack.isEmpty()):
        print(stack.pop(),end=' ')
    #unstacks items from stack and prints in order
    return

#-----TESTING QUEUE-----#
print('Testing Queue Implementation')

#initializing queue with 0 1 2 3 4 5 6 7 8 9
testQ = q.queue()
for i in range(0,10):
    testQ.push(i)

print('Testing dequeue order')
#output should be 0 1 2 3 4 5 6 7 8 9
testDequeueOrder(testQ)
print('\n')

#queue should be empty after test
print('Testing queue empty...')
assert(testQ.isEmpty() is True)
print('Queue confirmed empty')
print('\n')

#-----TESTING STACK-----#
print('Testing Stack Implementation')

#initializing stack with 0 1 2 3 4 5 6 7 8 9
testStack = s.stack()
for i in range(0,10):
    testStack.push(i)

print('Testing unstack order')
#output should be 9 8 7 6 5 4 3 2 1 0
testUnstackOrder(testStack)
print('\n')

print('Testing stack empty')
assert(testQ.isEmpty() is True)
print('Stack confirmed empty')
#stack should now be empty
#tests push, pop, and empty
print('\n')

#-----TESTING TREE-----#
print('Testing Tree Implementation')
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

print('Testing printTree()')
#testing print tree
#feeding in above tree, output should be:
#42 2 13 11 21 12 5 7 10 16 6
testTree.printTree()
print('\n')

print('Testing add with non-existent parent')
#testing add with non existant parent
testTree.add(1337,2)
print('Test Success')

print('Testing add on parent with two existing children')
#testing add with full node
testTree.add(2,56)
print('Test Success')

#testing the delete function with same tree
#first trying to delete a node with children should result in 
#error messages being displayed

print('Testing delete with two children')
#node 2 has children 13 and 21, so will show an error
testTree.delete(2)

print('Testing delete with 1 child')
#node 16 has 1 child so will show an error
testTree.delete(16)

print('Testing delete on leaves')
#node 6 and 11 are leafs so will show no error
testTree.delete(11)
testTree.delete(6)

#confirming that those nodes are deleted using the
#find method (also confirms nodes are no longer pointed to)
assert(testTree.find(11) is None)
assert(testTree.find(6) is None)
print('Test Success')

#printing tree again, confirming delete
#output should be: 42 2 13 21 12 5 7 10 16
print('Re-printing tree to confirm deletes')
testTree.printTree()
print('\n')

#-----TESTING GRAPH-----#
print('Testing Graph Implementation')
testGraph = g.graph()

#initializing graph with 15 vertices
for i in range(1,16):
    testGraph.addVertex(i)

#testing adding an existing vertex:
print('Testing adding an existing vertex')
testGraph.addVertex(2)

#intializing edges
for i in range(1,15):
    testGraph.addEdge(i,i+1)
testGraph.addEdge(15,1)

#test adding existing edge
print('Testing adding existing edge')
testGraph.addEdge(5,4)

#test adding edge between 2 non-existing vertices
print('Testing adding an edge between non-existing vertices')
testGraph.addEdge(42,24)

#test adding edge between existing and non existing vertices
print('Testing adding an edge between existing and non-existing vertices')
testGraph.addEdge(5,1024)

#test find 5 vertices
print('Testing findVertex')
#output should be 2 and 4
testGraph.findVertex(3)
#output should be 7 and 9
testGraph.findVertex(8)
#output should be 14 and 1
testGraph.findVertex(15)
#output should be 5 and 7
testGraph.findVertex(6)
#output should be 11 and 13
testGraph.findVertex(12)

#test finding non-existent vertex
print('Testing findVertex on non-existing vertex')
testGraph.findVertex(1337)
