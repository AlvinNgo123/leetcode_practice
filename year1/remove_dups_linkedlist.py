#Constructor class for LinkedList implementation used for this problem.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

#Runtime: O(n) | Space: O(1)
#         where n is the number of nodes in the linked list
def remove_dups_linkedlist(listHead):
    #Have a currentPtr that pts to the current val (intialize to the head)
	#Have a possibleNextPtr that pts to the next val (intialize to the head's next)
	#Repeat until currentPtr reaches None (end of linked list)
		#Iterate through until the posible val is different from currentPtr's val
		#From, there change currentPtr.next to ptr to the new val
		#And then move currenPtr to that new val's spot
    #Return the editted linked list
	currentPtr = listHead
	possibleNextPtr = currentPtr.next
	
	while (currentPtr is not None):
		if possibleNextPtr is None:
			currentPtr.next = None
			break
		if possibleNextPtr.value == currentPtr.value:
			possibleNextPtr = possibleNextPtr.next
		else:
			currentPtr.next = possibleNextPtr
			currentPtr = possibleNextPtr
	
	return listHead
