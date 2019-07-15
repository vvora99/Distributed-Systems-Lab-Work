import time
import random

n=int(input("Enter number of processes :"))

processes=[]
for i in range(n+1):
	processes.append(i)
coordinator=processes[len(processes)-1]
#coordinator=random.choice(processes)
print("Here, Coordinator is "+str(coordinator))

time.sleep(3)
print("Coordinator is crashed!!! Need for election.")

proc_t=int(input("Which process has noticed the coordinator failure ? "))

active=[proc_t]
count=0
def election(leader,coordinator,count):
	if count==n:
		coordinator=max(active)
		print("New coordinator is "+str(coordinator))
	else:
		proc=(leader+1)%n
		print("Elect msg forwarded to "+str(proc))
		count=count+1
		if proc==coordinator or proc==leader:
			election(proc,coordinator,count)
		else:
			choice=int(input("Process "+str(proc)+" : Are you alive ? (0/1) : "))
			if choice==1:
				active.append(proc)
				election(proc,coordinator,count)
			else:
				election(proc,coordinator,count)

election(proc_t,coordinator,count)

