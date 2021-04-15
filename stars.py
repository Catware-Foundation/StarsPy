from random import randint, choice
from termcolor import colored
from time import sleep

class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)

import sys
sys.stdout = Unbuffered(sys.stdout)

stars = ["*", ".", "~", "`", "'", "☆"]
coef = 50
try:
        while True:
                sleep(0.0000000000000001)
                if str(coef).startswith("-") or coef == 0:
                        coef += 50
                if coef < 10:
                        coef += 10
                if randint(1, coef) == 1:
                        print(colored(choice(stars), choice(["blue", "white"])), end="")
                else:
                        print(" ", end='')
                if choice([True, False]):
                        coef += 1
                else:
                        coef -= 1
except KeyboardInterrupt:
        print(" ~ starspy is terminating ~ ")

except BrokenPipeError:
        print(" ~ broken pipe error ~ ")
