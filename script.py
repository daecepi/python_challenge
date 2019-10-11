'''
Main functionality that contains the application
'''
def queenCalculator(matt):
    print(1)


def getFirstObstacles():
    print(2)

def getFileInfo():
    finalInfo = []
    data = []
    with open('./InputsQueenBoard.txt', 'r') as f:
        data = f.read()
    print(type(data))

if __name__ == "__main__" :
    getFileInfo()