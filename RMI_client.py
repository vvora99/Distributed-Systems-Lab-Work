import Pyro4
import time

num_list = [15,33,23,12,9]

uri = input("What is the Pyro uri of the greeting object? ").strip()

Factorial = Pyro4.Proxy(uri)
start_time = time.time()
print(Factorial.computefactorial(num_list))
end_time = time.time() - start_time


#f = open("D:\Boring Stuff\Study Material\Sem VI\Distributed Systems\Lab\compare.txt", "a+")
temp = "RMI: " + str(end_time)
print(temp)
#f.write(temp)
#f.close()
