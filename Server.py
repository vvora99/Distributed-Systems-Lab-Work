import socket                

s = socket.socket()

port = 12345                
  
s.bind(('', port))         
print("socket binded to "+str(port))

s.listen(5)      
print("socket is listening")
  
while True:
	c, addr = s.accept()
	print('Got connection from '+str(addr))
	str1=c.recv(1024)
	str1=str1.decode()
	list_t=str1.split()
	list1=[]
	for num in list_t:
		list1.append(float(num))
	list1.sort()
	string=''
	for num in list1:
		string=string+str(num)+" "
	c.send(string.encode())
	c.close() 
