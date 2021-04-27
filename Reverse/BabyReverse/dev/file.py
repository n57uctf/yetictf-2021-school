from random import randint, seed
from os import getpid
from hashlib import sha256

pid = 123141
print("Running with pid: "+str(pid))
seed(pid)
salt = str(randint(10000000000,99999999999999999)).encode()
flag = str(sha256(salt + 'secret message here'.encode()).hexdigest())
if pid != 123141:
    print("yetiCTF{flag_was_here}") 
else:
    print ("yetiCTF{"+flag+"}")
