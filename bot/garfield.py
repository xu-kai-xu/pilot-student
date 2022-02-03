## garfield.py
from bot import *

class Garfield:
    
    def __init__(self):
        self.bots = []
    
    def add(self, bot):
        self.bots.append(bot)
    
    def run(self):
        print("Welcome to Garfield dialog system. Let's Talk!\n")
        
        for bot in self. bots:
            bot.run()

if __name__ == '__main__':
    garfield = Garfield()
    garfield.add(HelloBot())
    garfield.add(GreetingBot())
    garfield.add(CalcBot())
    garfield.add(FavoriteColorBot())
    garfield.run()

