import Pyro4
from math import factorial as fact

@Pyro4.expose
class Factorial(object):
    def computefactorial(self,num_list):
        x = [float(fact(num)) for num in num_list]
        return x

daemon = Pyro4.Daemon()
uri = daemon.register(Factorial)

print("Ready. Object uri =", uri)
daemon.requestLoop()


