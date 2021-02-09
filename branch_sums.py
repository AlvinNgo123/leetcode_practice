#This is how the BST is constructed
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Runtime: O(n) | Space: O(n)  
#         where n is the number of nodes in the tree
def branchSums(root):
	#We want to keep track of the current node, the current running sum, and the final return list
	currNode = root
	currRunningSum = 0
	finalList = []
	bsHelper(currNode, currRunningSum, finalList)
	
	return finalList

def bsHelper(currNode, currRunningSum, finalList):
	#If currentNode is none, just return
	#If the current node has no children (no left and no right), we add the sum of its val with currRunningSum to finalList and then return
	#Otherwise, recursively call bsHelper with currNodes' left children  and then after with its right children
	if currNode is None:
		return
	currRunningSum += currNode.value
	if currNode.right is None and currNode.left is None:
		finalList.append(currRunningSum)
		return
	bsHelper(currNode.left, currRunningSum, finalList)
	bsHelper(currNode.right, currRunningSum, finalList)


