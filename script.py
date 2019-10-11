import math

'''
MODULE CONSTANTS: NECESSARY IF EXPORTING FUNCTIONALITIES
'''
X = 0
Y = 1

TOP_POINT = 0
BOTTOM_POINT = 1
RIGHT_POINT = 2
LEFT_POINT = 3
BOTTOM_LEFT_POINT = 4
TOP_LEFT_POINT = 5
BOTTOM_RIGHT_POINT = 6
TOP_RIGHT_POINT = 7


'''
Main functionality that contains the application's main funtional requirement
    @Param {list} board_size: list with x lenght and y lenght of the board (being first x)
    @Param {list} queen_pos: with the position of the queen
    @Param {list(list)} obstacles: the array that contains in the board
    @returns {int} with the number of paths to takes
'''
def queen_calculation(board_size, queen_pos, obstacles):
    #Catching base escenarios
    if board_size == [0,0]:
        return 0
    elif board_size == [1,1]:
        return 1

    #Get closest obstacles in all directions
    closest_obstacles = get_first_obstacles(board_size,queen_pos,obstacles)

    numberOfMoves = 0

    #Counting the moves in eight directions
    for obstacle in closest_obstacles:
        distance = movesBetweenTwoPoint(obstacle[X], obstacle[Y], queen_pos[X], queen_pos[Y])
        numberOfMoves = numberOfMoves + distance

    return numberOfMoves

'''
Function that filters only the closest obstacles of the eight paths (if part of a library by now is recommended to be private)
    @Param {list} limits: list with x lenght and y lenght of the board (being first x)
    @Param {list} queen: with the position of the queen
    @Param {list(list)} obstacles: the array that contains in the board 
    @Returns {list(list)} that contains the closest obstacles i the 8 directions thus the ones that limit her
'''
def get_first_obstacles(limits, queen, obstacles):
    obstacles_copy = obstacles.copy()
    #Initialize with the position each  list is going to be in
    closest_obstacles = [ [] for i in range(8)]

    #Setting the limits
    bestTop = limits[1]
    bestRight = limits[0]
    bestLeft = 0
    bestBottom = 0

    #Get closest obstacles in the cross (the cross ones)
    for obstacle in obstacles:
        if obstacle[X] == queen[X]:# this obstacle is at the right of the queen
            if bestTop >= obstacle[Y]:# verifing that this obstacle is even closer to the queen
                bestTop = obstacle[Y]
                closest_obstacles[TOP_POINT] = obstacle
            obstacles_copy.remove(obstacle)# Taking out positions in the cross
        
        elif obstacle[X] == queen[X]:# this obstacle is at the left of the queen
            if bestBottom <= obstacle[Y]:# verifing that this obstacle is even closer to the queen
                bestBottom = obstacle[Y]
                closest_obstacles[BOTTOM_POINT] = obstacle
            obstacles_copy.remove(obstacle)# Taking out positions in the cross

        elif obstacle[Y] == queen[Y]:# this obstacle is down the queen
            if bestRight >= obstacle[X]:# verifing that this obstacle is even closer to the queen
                bestRight = obstacle[X]
                closest_obstacles[RIGHT_POINT] = obstacle
            obstacles_copy.remove(obstacle)# Taking out positions in the cross

        elif obstacle[Y] == queen[Y]:# this obstacle is  of the queen
            if bestLeft <= obstacle[X]:# verifing that this obstacle is even closer to the queen
                bestLeft = obstacle[X]
                closest_obstacles[LEFT_POINT] = obstacle
            obstacles_copy.remove(obstacle)# Taking out positions in the cross
    
    #Get closest obstacles in the diagonals
    print(obstacles_copy)
    print(closest_obstacles)


    best_t_r = max(limits); #Best of top right (max is the maximun limit thus maximun distance possible from points)
    best_t_l = max(limits); #Best of top left (max is the maximun limit thus maximun distance possible from points)
    best_b_r = max(limits); #Best of bottom right (max is the maximun limit thus maximun distance possible from points)
    best_b_l = max(limits); #Best of bottom left (max is the maximun limit thus maximun distance possible from points)

    '''
        If you treat the ramaining point as points in a 2D math space and calculate the slope
        of the straight line formed by the queen and a obstacle and obtain 1.0/-1.0 as the slope
        the obstacle is in its diagonal, resuming a math function can make sure of the diagonal
    '''
    
    for obstacle in obstacles_copy:
        print(((queen[Y]-obstacle[Y])/(queen[X]-obstacle[X])))
        if  abs((queen[Y]-obstacle[Y])/(queen[X]-obstacle[X])) == 1.0: #Making sure only the points in the diagonal pass
            #Clasifing the diagonal where the point is located
            if obstacle[X] < queen[X]: 
                if obstacle[Y] < queen[Y]:# Bottom left
                    distance = movesBetweenTwoPoint(obstacle[X], obstacle[Y], queen[X], queen[Y])
                    if distance < best_b_l:
                        best_b_l = distance
                        closest_obstacles[BOTTOM_LEFT_POINT] = obstacle

                elif obstacle[Y] > queen[Y]: #Top left
                    distance = movesBetweenTwoPoint(obstacle[X], obstacle[Y], queen[X], queen[Y])
                    if distance < best_t_l:
                        best_t_l = distance
                        closest_obstacles[TOP_LEFT_POINT] = obstacle

            elif obstacle[X] > queen[X]:
                if obstacle[Y] < queen[Y]: # Bottom right
                    distance = movesBetweenTwoPoint(obstacle[X], obstacle[Y], queen[X], queen[Y])
                    if distance < best_b_r:
                        best_b_r = distance
                        closest_obstacles[BOTTOM_RIGHT_POINT] = obstacle

                elif obstacle[Y] > queen[Y]: # Top right
                    distance = movesBetweenTwoPoint(obstacle[X], obstacle[Y], queen[X], queen[Y])
                    if distance < best_t_r:
                        best_t_r = distance
                        closest_obstacles[TOP_RIGHT_POINT] = obstacle

    print(closest_obstacles)
    #retuning the obstacle
    return closest_obstacles
    
'''
Makes use of the 
'''
def movesBetweenTwoPoint(x1, y1, x2, y2):
    x_differences = x2 - x1
    y_differences = y2 - y1
    distance = math.sqrt(math.pow(x_differences,2)+math.pow(y_differences,2))
    return distance

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
    result = queen_calculation(inputs[0], inputs[1], inputs[2:])

    print(result)