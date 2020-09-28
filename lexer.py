from parser import separateTokens
from parser import keywords
from parser import operators
from parser import separators

def main():
    # specify the input file needed for this program
    # directory = "inputTextFiles/"
    # inFile = "sample2.txt"
    # try:
    #     userFile = input("input filename here(will draw from inputTextFiles directory): ")
    #     print(userFile)
    #     lexicalAnalyze(directory + userFile)
    # except FileNotFoundError:
    #     print("invalid file... will use default file\n")
    #     lexicalAnalyze(directory + inFile)
    lexicalAnalyze("inputTextFiles/sample2.txt")

def lexicalAnalyze(file):
    parsedOutFile = separateTokens(file)
    outputFile = open( 'output.txt', 'w' )
    outputFile.write("TOKENS\t\t\tLexemes\n\n")
    afterEqualSignSpaces = 10
    for lexeme in parsedOutFile:
        print("LEXEME IN QUESTION: " + lexeme)
        equalSignSpaces = 20
        if identifyKeywords( lexeme ):
            outputFile.write( 'KEYWORD' )
            equalSignSpaces = equalSignSpaces - len( 'KEYWORD' )
            outputFile.write( '=' )
            for _ in range( afterEqualSignSpaces ):
                outputFile.write(' ')
            outputFile.write( lexeme )
            outputFile.write( '\n' )
            continue
        elif identifyIdentifiers( lexeme ):
            outputFile.write( 'IDENTIFIER' )
            equalSignSpaces = equalSignSpaces - len( 'IDENTIFIER' )
            outputFile.write( '=' )
            for _ in range( afterEqualSignSpaces ):
                outputFile.write(' ')
            outputFile.write( lexeme )
            outputFile.write( '\n' )
            continue
        elif identifyOperators( lexeme ):
            outputFile.write( 'OPERATOR' )
            equalSignSpaces = equalSignSpaces - len( 'OPERATOR' )
            outputFile.write( '=' )
            for _ in range( afterEqualSignSpaces ):
                outputFile.write(' ')
            outputFile.write( lexeme )
            outputFile.write( '\n' )
            continue
        elif identifySeparators( lexeme ):
            outputFile.write( 'SEPARATOR' )
            equalSignSpaces = equalSignSpaces - len( 'SEPARATOR' )
            outputFile.write( '=' )
            for _ in range( afterEqualSignSpaces ):
                outputFile.write(' ')
            outputFile.write( lexeme )
            outputFile.write( '\n' )
            continue
        elif identifyFloat( lexeme ):
            outputFile.write( 'FLOAT' )
            equalSignSpaces = equalSignSpaces - len( 'FLOAT' )
            outputFile.write( '=' )
            for _ in range( afterEqualSignSpaces ):
                outputFile.write(' ')
            outputFile.write( lexeme )
            outputFile.write( '\n' )
            continue
        elif identifyInteger( lexeme ):
            outputFile.write( 'INTEGER' )
            equalSignSpaces = equalSignSpaces - len( 'INTEGER' )
            outputFile.write( '=' )
            for _ in range( afterEqualSignSpaces ):
                outputFile.write(' ')
            outputFile.write( lexeme )
            outputFile.write( '\n' )
            continue
        else:
            outputFile.write( 'INVALID' )
            equalSignSpaces = equalSignSpaces - len( 'INVALID' )
            outputFile.write( '=' )
            for _ in range( afterEqualSignSpaces ):
                outputFile.write(' ')
            outputFile.write( lexeme )
            outputFile.write( '\n' )


        outputFile.close()

def printToken(type, aToken):
    print(type + '\t=\t' + aToken)

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
        # print("keywords:", temp)
        printToken("KEYWORDS", aToken)
        return  True
    else:
        # print("identifyKeywords: state was not in acceptedStates for token ", aToken)
        return False

# @param aToken - token to identify. Token should be of type string

# identifies if token is an identifier
def identifyIdentifiers(aToken):
    if aToken == '':
        return False

    initialState = 0
    acceptedStates = [1]
    states = [
        [1,2,2,2],
        [1,1,2,1],
        [2,2,2,2]
    ]
    letter = 0
    digit = 1
    symbol = 2
    dollarSign = 3
    state = initialState
    temp = ''
    for char in aToken:
        temp += char
        if char.isalpha():
            state = states[state][letter]
        elif char == '$':
            state = states[state][dollarSign]
        elif char.isnumeric():
            state = states[state][digit]
        elif not char.isalpha() and not char.isnumeric():
            state = states[state][symbol]
    if state in acceptedStates:
        # print("Identifiers:", aToken)
        printToken("IDENTIFIERS", aToken)
        return True
    else:
        # print("identifyIdentifiers: state was not in acceptedStates for token ", aToken)
        return False

# @param aToken - token to identify. Token should be of type string

# identifies if token is a operator
def identifyOperators(aToken):
    if aToken == '':
        return False

    initialState = 0
    acceptedStates = [1]
    states = [
        [2,2,1],
        [2,2,2],
        [2,2,2]
    ]
    letter = 0
    digit = 1
    symbol = 2
    state = initialState
    temp = ''
    for char in aToken:
        temp += char
        if char.isalpha():
            state = states[state][letter]
        elif char.isnumeric():
            state = states[state][digit]
        elif not char.isnumeric() and not char.isalpha():
            state = states[state][symbol]

    if state in acceptedStates:
        if temp in operators:
            # print("operators:", aToken)
            printToken("OPERATORS", aToken)
            return  True
    else:
        # print("identifyOperators: state was not in acceptedStates for token ", aToken)
        return False

# @param aToken - token to identify. Token should be of type string

# identifies if token is a separator
def identifySeparators(aToken):
    if aToken == '':
        return False

    initialState = 0
    acceptedStates = [1]
    states = [
        [2,2,1,1],
        [2,2,2,2],
        [2,2,2,2]
    ]
    letter = 0
    digit = 1
    symbol = 2
    spce = 3
    state = initialState
    temp = ''
    for char in aToken:
        temp += char
        if char.isalpha():
            state = states[state][letter]
        elif char == ' ':
            state = states[state][spce]
        elif char.isnumeric():
            state = states[state][digit]
        elif not char.isnumeric() and not char.isalpha():
            state = states[state][symbol]

    if state in acceptedStates:
        if temp in separators:
            # print("separators:", aToken)
            printToken("SEPARATORS", aToken)
            return  True
    else:
        # print("identifySeparators: state was not in acceptedStates for token ", aToken)
        return False




if __name__ == "__main__":
    main()


# print(l)
# identifyKeywords("int")
# identifyKeywords("while")
# identifyKeywords("while3")
# identifyIdentifiers("ogabo23oga123")
# identifyIdentifiers("ogabo23oga123$")
# identifyIdentifiers("ogabo$23oga123")
# identifyIdentifiers("59gabo23oga123")
# identifyOperators("*")
# identifyOperators("abc")
# identifyOperators("**")
# identifyOperators("/")
# identifySeparators(";")
# identifySeparators("()")
# identifySeparators(")")
# identifySeparators("s[")
# identifySeparators("sp")
# identifySeparators(" sp")

# print( identifyFloat( '.223' ) )

