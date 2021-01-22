#Runtime: O(nlogn) | Space: O(n)
#         where n is the length of queries list
def min_wait_time(queries):
    #First sort the list of queries in ascending order
	#Then create a new list of the same length that represents the wait time to get to that point
	#Base
		#Initialize first element of new list to be 0
			#if length of queries is 1, then return 0
		#Initialize second element of new list to be val of first query
			#If length of queries is 2, return this second element
	#Fill rest of new list w/ following formula
	    # newList[i] = newList[i-1] + queries[i-1]
	#At the end, iterate through new list and sum up the values to return the min wait time
    
	queries.sort()
	minWaitList = [0 for x in range(len(queries))]
	
	if len(queries) == 1:
		return 0
	minWaitList[1] = queries[0]
	if len(queries) == 2:
		return minWaitList[1]
	
	for i in range(2, len(queries)):
		minWaitList[i] = minWaitList[i-1] + queries[i-1]
	
	minWait = 0
	for j in range(len(minWaitList)):
		minWait += minWaitList[j]
	
	return minWait

query1 = [6, 2, 2, 3, 1]
print(min_wait_time(query1))
#17

query2 = [6]
print(min_wait_time(query2))
#0

query3 = [6, 2]
print(min_wait_time(query3))
#2

query4 = [1, 4, 2, 3, 4]
print(min_wait_time(query4))
#20