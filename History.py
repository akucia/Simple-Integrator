import time
import os

class History(object):
    """
    log class implemented,but not documented
    """
    def __init__(self):
        self.storage = []

    def add(self,newItem):
        for item in newItem:
            self.storage.append(item)

    def show(self):
        print("History:")
        for item in self.storage:
            print(item)

    def saveToFile(self):
        directory = os.getcwd() + '/history'
        if not os.path.exists(directory):
            os.makedirs(directory)
        fileName = directory + '/'+ time.strftime("%H:%M:%S") + '.txt'

        logFile = open(fileName,'a')
        for item in self.storage:
            logFile.write(item)
            logFile.write('\n')

        print("Log saved to" + fileName)

    def loadFromFile(self):
        pass

    def isEmpty(self):
        if len(self.storage) == 0:
            return True
        else:
            return False


