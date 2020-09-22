from westinSeparateFunc import separateTokens
from westinSeparateFunc import keywords

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

# @param aToken - token to identify. Token should be of type string

# Identifies if token is a keyword
def identifyKeywords(aToken):
    if aToken == '':
        return False

    initialState = 0
    acceptedStates = [1]
    states = [
        [1,2,2],        #State 0: Initial
        [1,2,2],        #State 1: letters
        [2,2,2]         #State 2: digits and symbols
    ]
    letters = 0
    digits = 1
    state = initialState
    temp = ''
    for char in aToken:
        temp += char
        if char.isalpha():
            state = states[state][letters]
        elif char.isnumeric() or not char.isalpha() and not char.isnumeric():
            state = states[state][digits]

    if state in acceptedStates and temp in keywords:
        print("identifier:", temp)
        return  True
    else:
        print("identifyKeywords: state was not in acceptedStates for token ", aToken)
        return False

# @param aToken - token to identify. Token should be of type string

# identifies if token is an identifier
def identifyIdentifiers(aToken):
    if aToken == '':
        return False

    initialState = 0
    acceptedStates = [1,2]
    states = [
        [1,3,3],
        [1,1,3],
        [3,3,3],
        [3,3,3]
    ]
    letter = 0
    digit = 1
    symbol = 2
    epsilon = 2 # special case, make row = epsilon
    state = initialState
    temp = ''
    for char in aToken:
        temp += char
        if char.isalpha():
            state = states[state][letter]
        elif char == '$':
            # we check for this to see if we were already in an epsilon state
            if state == epsilon:
                state = states[state][epsilon]
            else:
                state = epsilon
        elif char.isnumeric():
            state = states[state][digit]
        elif not char.isalpha() and not char.isnumeric():
            state = states[state][symbol]
    if state in acceptedStates:
        print("keywords:", aToken)
        return True
    else:
        print("identifyIdentifiers: state was not in acceptedStates for token ", aToken)
        return False;



l = separateTokens("inputTextFiles/sample2.txt")

print(l)
identifyKeywords("int")
identifyKeywords("while")
identifyKeywords("while3")
identifyIdentifiers("ogabo23oga123")
identifyIdentifiers("ogabo23oga123$")
identifyIdentifiers("ogabo$23oga123")
identifyIdentifiers("59gabo23oga123")
print( identifyFloat( '.223' ) )

