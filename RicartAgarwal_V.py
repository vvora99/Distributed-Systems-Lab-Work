import time
import random
n=int(input("Enter number of processes : "))

processes=[]
for i in range(n):
	processes.append(i)

while(1):
	choice=int(input("1 to request 0 to quit"))
	if choice==1:
		res=[]
		proc=int(input("Who want to request ? "))
		time_p=int(input("Enter timestamp : "))
		for p in range(n):
			if p!=proc:
				print("REQ forwarded to ",p)
				ans=int(input(str(p)+" -> You want to go to CS ? (0/1)"))
				if ans==0:
					res.append(1)
				else:
					ts=random.randint(1,5)
					print(str(p)+" - timestamp : "+str(ts))
					if ts<time_p:
						res.append(0)
						print("Wait Please !!")
						break
					else:
						res.append(1)
		if len(set(res))==1:
			print("!! Request Granted !!")
			print(str(proc)+" is in CS")
			time.sleep(3)
			print(str(proc)+" exits CS")
			print("process "+str(proc)+" announces to all that it has completed its CS.")
		else:
			print("Wait Please !!")
	if choice==0:
		break

