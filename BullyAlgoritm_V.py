import time

n=int(input("Enter number of processes :"))

processes=[]
for i in range(n+1):
	processes.append(i)
coordinator=processes[len(processes)-1]
print("Here, Coordinator is "+str(coordinator))

time.sleep(3)

def election():
	leader=int(input("Enter the process which has the knowledge of the crashed process : "))
	msg=[]
	accept=[]
	for i in range(leader+1,processes[-1]+1):
		if (i != processes[-1]):
			msg.append(i)
	print("Request message is forwarded to : ")
	print(msg)
	for i in msg:
		ans=int(input("Process " + str(i) + " : Alive? (0/1) : "))
		if (ans==1):
			accept.append(i)
	print("Processes which are ready to become coordinator : ")
	print(accept)
	if len(accept)==1:
		print("New Coordinator is : ")
		print(accept)
		coordinator=accept[0]
	elif len(accept)==0:
		print("New coordinator is : ")
		print(leader)
		coordinator=leader
	else:
		coordinator=max(accept)
		print("New coordinator is : ")
		print(coordinator)
		'''while accept:
			pr=accept[0]
			print(pr sends election msg to every process in accept)
			for p in accept:
				if p>pr:
					print(p wants to become coordinator)
					accept.remove(pr)
		'''
	print(str(coordinator)+" has declared itself as coordinator to all processes.")

print("Coordinator is crashed !!! Need for election !!!")
election()

