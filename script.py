'''
Main functionality that contains the application's main funtional requirement
'''
def queen_calculation(board_size, queen_pos, obstacles):


    #Get all the obstacle
    closest_obstacles = get_first_obstacles(board_size,queen_pos,obstacles)

'''
Function that filters only the closest obstacles of the eight paths
    @Param {list(tuples)}  obstacles: the array that contains the 
'''
def get_first_obstacles(limits, position, obstacles):
    obstaclesCopy = obstacles.copy()
    #Initialize with the position each  list is going to be in
    closest_obstacles = [ [] for i in range(8)]

    #Setting the limits
    bestTop = limits[1]
    bestRight = limits[0]
    bestLeft = 0
    bestBottom = 0

    #Get closest obstacles in the cross (the cross ones)
    for obstacle in obstacles:
        if obstacle[0] == position[0]:# this obstacle is at the right of the queen
            if bestTop >= obstacle[1]:# verifing that this obstacle is even closer to the queen
                bestTop = obstacle[1]
                closest_obstacles[0] = obstacle
            obstaclesCopy.remove(obstacle)# Taking out positions in the cross
        
        elif obstacle[0] == position[0]:# this obstacle is at the left of the queen
            if bestBottom <= obstacle[1]:# verifing that this obstacle is even closer to the queen
                bestBottom = obstacle[1]
                closest_obstacles[1] = obstacle
            obstaclesCopy.remove(obstacle)# Taking out positions in the cross

        elif obstacle[1] == position[1]:# this obstacle is down the queen
            if bestRight >= obstacle[0]:# verifing that this obstacle is even closer to the queen
                bestRight = obstacle[0]
                closest_obstacles[2] = obstacle
            obstaclesCopy.remove(obstacle)# Taking out positions in the cross

        elif obstacle[1] == position[1]:# this obstacle is  of the queen
            if bestLeft <= obstacle[0]:# verifing that this obstacle is even closer to the queen
                bestLeft = obstacle[0]
                closest_obstacles[3] = obstacle
            obstaclesCopy.remove(obstacle)# Taking out positions in the cross
    
    #Get closest obstacles in the diagonals
    print(obstaclesCopy)
    print(closest_obstacles)

    bestTopRight = 0;
    bestTopLeft = 0;
    bestBottomRight = 0;
    bestBottomLeft = 0;

    for obstacle in obstaclesCopy:
        if obstacle == True:
            print('done')

    #retuning the obstacle
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

    #Treating the raw input to a more managable data structure (list of [x,y])
    treatedInputs = [list(map(int, inputPair.split(' '))) for inputPair in rawInputs]

    return treatedInputs

#Checking entrypoint to prevent execution if this set of functions are imported as any python module
if __name__ == "__main__" :

    #Getting the inputs for the main function
    inputs = get_file_inputs_for_analisis()

    #Calling the main algorithm and passing the right proportions
    queen_calculation(inputs[0], inputs[1], inputs[2:])