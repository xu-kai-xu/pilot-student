## bot.py
import random
import re
import time
from termcolor import colored
from simpleeval import simple_eval

class Bot:
    
    wait = 1
    
    def __init__(self):
        self.q = ''
        #self.a = ''
    
    def _think(self, s):
        return s
    
    def _say(self, s):
        #time.sleep(wait)  # NameError: name 'wait' is not defined
        time.sleep(Bot.wait)  
        print(colored(s, 'blue'))
        #return s
    
    def run(self):
        self._say(self.q)
        self.a = input()
        self._say(self._think(self.a))
        
class HelloBot(Bot):
    
    def __init__(self):
        self.q = "Hi, what's your name?"
        
    def _think(self, s):
        return(f"Hello, {s}!")


class GreetingBot(Bot):
   
    def __init__(self):
        self.q = "How are you today?\n你今天怎么样呀？"
 
    def _think(self, s):
        feeling = s.lower()
        test = re.search('goo+d', feeling) or \
               re.search('nice', feeling) or \
               re.search('excellent', feeling)
        if test:
            return("I am feeling good, too!")
        else:
            return("Sorry to hear that.")


class FavoriteColorBot(Bot):
   
    def __init__(self):
        self.q = "What is your favorite color？"
 
    def _think(self, s):
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
        return (f"You like {s}? Tha's great color. My favorite color is {random.choice(colors)}.")

    
class CalcBot(Bot):
    
    def __init__(self):
        self.q = 'Through recent upgrade, I can do calculation now. Input some arithmetic expression to try.'
    
    def _think(self, s):
        result = simple_eval(s)
        return f"Done. Result = {result}"
        

    
if __name__ == '__main__': 
    h = HelloBot()
    g = GreetingBot()
    f = FavoriteColorBot()
    
    h.run() 
    g.run()
    f.run()