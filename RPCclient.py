#import xmlrpclib
import xmlrpc.client as xmlrpclib
import time
from math import factorial
import math

def factorial(num_list):
	list1=[]
	for num in num_list:
		list1.append(math.factorial(num))
	return list1
    #return [factorial(num) for num in num_list]

num_list = [15,33,23,12,9]
fact = []

client = xmlrpclib.ServerProxy("http://localhost:8000")

start_time = time.time()
f = client.computefactorial(num_list)
end_time  = time.time() - start_time
print(f, "computed in", end_time, "seconds using Remote Procedure Call")


print()
print("WITHOUT RPC")
start_time1 = time.time()
ans=factorial(num_list)
end_time = time.time() - start_time1

print(ans, "computed in", end_time,"seconds using Simple Procedure Call")
