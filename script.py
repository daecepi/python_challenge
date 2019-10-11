'''
Main functionality that contains the application's main funtional requirement
'''
def queen_calculation(board_size, queen_pos, obstacles):
    
    #Get all the obstacle
    closest_obstacles = get_first_obstacles(obstacles)

'''
Function that finds the obstacles of the eight possition
    @Param list(tuples) : 
'''
def get_first_obstacles(obstacles):
    closest_obstacles = []
    #Get first four obstacles (the cross ones)


    return closest_obstacles
    

'''
Modularizing the reading of the file since the responsability of reading the file
does not necesarily belong to the queen calculator.
    @returns inputs : the inputs organized orginized as a list of tuples
'''
def get_file_inputs_for_analisis():
    fileText = []
    with open('./InputsQueenBoard.txt', 'r') as f:
        fileText = f.read()
    
    #Pythonic way of spliting strings into lists with data
    #Also the raw inputs will contain the different outputs
    rawInputs = fileText.split("\n")

    #Treating the raw input to a more managable data structure (tuples given the nature of the data)
    treatedInputs = [tuple(map(int, inputPair.split(' '))) for inputPair in rawInputs]

    return treatedInputs

#Checking entrypoint to prevent execution if this set of functions are imported as any python module
if __name__ == "__main__" :

    #Getting the inputs for the main function
    inputs = get_file_inputs_for_analisis()

    #Calling the main algorithm
    queen_calculation(inputs[0], inputs[1], [])