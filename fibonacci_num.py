#ITERATIVE
#Runtime: O(n) | Space: O(1)
#         where n is the input value
def fibonacci_num(n):
	#Create two variables to keep track of the prior two nums
	#Initialize the two base cases for fib seq (0, 1)
		#Return 0 or 1 if n is 0 or 1
	#Have a counter that counts from 2 until n
		#At each iteration, add the prior two nums to get new val
		#Shift the prior two nums to accomodate for this val
	#At the end, return the last sum
	prevPrev = 0
	prev = 1

	if n == 0:
		return prevPrev
	elif n == 1:
		return prev

	counter = 2
	while counter < n:
		currSum = prevPrev + prev
		prevPrev = prev
		prev = currSum

		counter += 1
	return prev


#Runtime: O(n) | Space: O(n)
#         where n is the input value
def fibonacci_num2(n):
	#Create an array of size n+1
	#Set the two base cases for fib seq (0, 1)
	#Iterate through array and fill out the rest of seq by summing the prior two values
	#Return the last value in the array 

	fibArr = [0 for x in range(n)]
	fibArr[1] = 1

	for i in range(2, len(fibArr)):
		fibArr[i] = fibArr[i-1] + fibArr[i-2]

	return fibArr[-1]


#RECURSIVE
#Runtime: O(n^2) | Space: O(n)
#         where n is the input value
def fibonacci_num3(n):
	#Return values for base cases
	#Call function recursively with prev two values sum
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return (fibonacci_num3(n-1) + fibonacci_num3(n-2))

n1 = 2
print(fibonacci_num(n1))
#1

n2 = 4
print(fibonacci_num(n2))
#2

n3 = 6
print(fibonacci_num(n3))
#5