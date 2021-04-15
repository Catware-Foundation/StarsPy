from random import randint, choice
from termcolor import colored
from time import sleep

def writeeffect(pic):
        pic = colored(pic, choice(["white", "blue"]))
        marg = " " * randint(1, 115)
        for x in pic.split("\n"):
                sleep(speed * len(marg))
                print(marg, end="")
                for y in x:
                        sleep(speed)
                        print(y, end="")
                print("")

#
# Pictures zone
#

PICTURES = [
"""
         ,MMM8&&&.
    _...MMMMM88&&&&..._
 .::'''MMMMM88&&&&&&'''::.
::     MMMMM88&&&&&&     ::
'::....MMMMM88&&&&&&....::'
   `''''MMMMM88&&&&''''`
         'MMM8&&&'  """,
"""
    ,-:` \;',`'-,
  .'-;_,;  ':-;_,'.
 /;   '/    ,  _`.-\
| '`. (`     /` ` \`|
|:.  `\`-.   \_   / |
|     (   `,  .`\ ;'|
 \     | .'     `-'/
  `.   ;/        .'
    `'-._____.""",
"""                     .::.
                  .:'  .:
        ,MMM8&&&.:'   .:'
       MMMMM88&&&&  .:'
      MMMMM88&&&&&&:'
      MMMMM88&&&&&&
    .:MMMMM88&&&&&&
  .:'  MMMMM88&&&&
.:'   .:'MMM8&&&'
:'  .:'
'::'  """]
starss = 0

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

speed = 0.000001

stars = ["*", ".", "~", "`", "'", "☆"]
coef = 1
try:
        while True:
                sleep(speed)
                if str(coef).startswith("-") or coef == 0:
                        coef += 50
                if coef < 10:
                        coef += 10
                if randint(1, coef) == 1:
                        print(colored(choice(stars), choice(["blue", "white"])), end="")
                        starss += 1
                else:
                        print(" ", end='')
                if choice([True, False]):
                        coef += 1
                else:
                        coef -= 1
                if randint(1, 5000) == 500:
                        writeeffect(choice(PICTURES))
except KeyboardInterrupt:
        print(f" ~ звёзд: {str(starss)} ~ ")
