#question1)
n=int(input())
marks=list(map(int, input().split()))

if min(marks)<40:
	print("Fail")
else:
	percentage=sum(marks)/n
	print(f"Aggregate Percentage:{percentage: .2f}")

	if percentage>75:
		print("Grade: Distinction")
	elif percentage >=60:
		print("Grade: First Division")
	elif percentage >=50:
		print("Grade: Second Division")
	else:
		print("Grade: Third Division")

#question2)
def fibonacci(n):

	if n==1:
		return 0
	elif n==2:
		return 1
	else:
		return fibonacci( n-1  ) + fibonacci(n-2)


n = int(input())
for i in range(1, n + 1):
	print(fibonacci(i), end=" ")

#question3)
n=int(input())
for i in range(1,n+1):
	print("* "*i)

#question4)
n=int(input())
for i in range(1, n+1):
	for j in range(1, i+1):
		print(j,end=" ")
	print()
