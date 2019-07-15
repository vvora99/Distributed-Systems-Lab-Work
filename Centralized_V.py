import random
import time

n=int(input("Enter number of processes : "))

processes=[]
for i in range(n):
	processes.append(i)

coordinator=max(processes)
print("Coordinator is ",coordinator)
processes.remove(coordinator)

any_p=random.choices(processes)
cs=any_p
print("CS : ",cs)
queue=[]

def request(proc):
	if len(cs)==0:
		print("OK.. Access Granted !")
		cs.append(proc)
		queue.remove(proc)
		time.sleep(2)
		release(proc)
	else:
		print("wait!")
		queue.append(proc)
	print("CS : ",cs)
	print("Queue : ",queue)

def release(proc):
	cs.remove(proc)
	print("CS : ",cs)
	print("Queue : ",queue)
	if len(queue)!=0:
		request(queue[0])


while(1):
	choice=int(input("1 for resource request, 0 for lock release, 9 to exit process"))
	if choice==0:
		proc=int(input("Which process has completed CS ?"))
		release(proc)
	if choice==1:
		proc=int(input("Who wants to go to CS ? "))
		request(proc)
	if choice==9:
		break

