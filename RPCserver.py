#from SimpleXMLRPCServer import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCServer
from math import factorial

def computefactorial(num_list):
    x = [float(factorial(num)) for num in num_list]
    return x

server = SimpleXMLRPCServer(('localhost',8000),allow_none = True)
server.register_function(computefactorial)
server.register_introspection_functions()
server.serve_forever()
