from bs4 import BeautifulSoup
import random, re

class raffle:

    def __init__(self):
        """
        ctor
        """
        self.favFile = r'./favlist.html'
        self.watchFile = r'./watchlist.html'
        self.watchList = self.getWatchers()
        self.favList = self.getFavs()

        self.winner = self.getWinner()
        print(f'Winner: {self.winner}')


    def getWatchers(self):
        """
        Gets the watchers from the target file.
        """ 
        watchPage = None
        with open(self.watchFile, 'r') as file:
            watchPage = BeautifulSoup(file, 'html.parser')

        expression = re.compile(r'>\w+</a>')
        watchList = expression.findall(str(watchPage))
        watchFiltered = []
        for name in watchList:
            name = name[1:-4]
            watchFiltered.append(name)
        return watchFiltered


    def getFavs(self):
        """
        Gets all the favs
        """
        favList = None
        with open(self.favFile, 'r') as file:
            favList = BeautifulSoup(file, 'html.parser')
            favList = ([item.get_text(strip = True) for item in favList.select("span.artist_name")])
        return favList


    def getWinner(self):
        """
        Picks a candidate from the favs, checks to see if they are in the watch list
        and if they are, it chooses them, if not, it chooses another.
        """
        #Incrementer set to 20. It will only try 20 times, if it gets no winner it exits. Prevents endless loops.
        i = 100 
        winner = None

        while i > 0:
            candidate = random.choice(self.favList)
            if candidate in self.watchList:
                return candidate
            i -= 1

        print("Exited early... no winner chosen")
            


if __name__ == '__main__':
    instance = raffle()
