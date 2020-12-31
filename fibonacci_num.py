#Runtime: O(n) | Space: O(n)
#         where n is the input value
def fibonacci_num(n):
	#Create an array of size n+1
	#Set the two base cases for fib seq (0, 1)
	#Iterate through array and fill out the rest of seq by summing the prior two values
	#Return the last value in the array 

	fibArr = [0 for x in range(n)]
	fibArr[1] = 1

	for i in range(2, len(fibArr)):
		fibArr[i] = fibArr[i-1] + fibArr[i-2]

	return fibArr[-1]

n1 = 2
print(fibonacci_num(n1))
#1

n2 = 4
print(fibonacci_num(n2))
#3

n3 = 6
print(fibonacci_num(n3))
#5