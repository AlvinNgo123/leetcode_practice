#Time = O(V+E) | Space = O(V) 
#       where V is number of vertices and E is number of edges
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
		
    def depthFirstSearch(self, array):
		#First add the current node to the array
		#Then, iterate through the chlidren list and recursively call the dfs function on each child and pass in the array
		#At the end, return the final array.
        array.append(self.name)
		for children in self.children:
			children.depthFirstSearch(array)
		return array