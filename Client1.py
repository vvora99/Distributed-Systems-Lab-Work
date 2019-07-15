import socket                
import numpy as np

s = socket.socket()          

port = 12345                

s.connect(('127.0.0.1', port)) 

list1 = np.random.uniform(0,50,100)

string=''

for num in list1:
	string=string+str(num)+" "

s.send(string.encode())

string=s.recv(1024)
string=string.decode()

list1=string.split()

print("Sorted List : ")
print(list1)

s.close()
