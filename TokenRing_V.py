import time
n=int(input("Enter number of processes :"))

processes=[]
for i in range(n):
	processes.append(i)

token=0

p=0
while(1):
	print("Token is with process "+str(p))
	choice=int(input("You want to go to CS ? (0/1) "))
	if choice==1:
		print(str(p)+" is in CS.")
		token=1
		time.sleep(3)
		token=0
		print(str(p)+" exits CS.")
	p=(p+1)%n
