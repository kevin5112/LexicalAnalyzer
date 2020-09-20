from westinSeparateFunc import separateTokens

#@param aToken - token to identify. Token should be of type string

#Identifies a token string and returns if it is a valid integer or not
def identifyInteger( aToken ):
    if( aToken == ''):
        return False

    states = [
        [0,1],      #State 0: Integer 
        [1,1]       #State 1: Not an Integer 
    ]             
    initialState = 0    
    acceptedStates = [0]

    state = initialState
    for char in aToken:
        if( char.isdigit() ):
            state = states[state][0]
        else:
            state = states[state][1]

    return (state in acceptedStates)

#@param aToken - token to identify. Token should be of type string

#Identifies a token string and returns if it is a valid Float or not
def identifyFloat( aToken ):
    if( aToken == ''):
        return False

    #Input 0: Digit
    #Input 1: Not a digit
    #Input 2: Decimal
    states = [
        [0,2,1],      #State 0: Integer 
        [1,2,2],      #State 1: Float
        [2,2,2],      #State 2: Not a Float
        [0,2,1]       #State 3: Initial
    ]             
    initialState = 3    
    acceptedStates = [1]

    state = initialState
    for char in aToken:
        if( char.isdigit() ):
            state = states[state][0]
        elif( char == '.'):
            state = states[state][2]
        else:
            state = states[state][1]

    return (state in acceptedStates)

l = separateTokens("inputTextFiles/sample2.txt")

print(l)

print( identifyFloat( '.223' ) )

