import sys
import re

comments = "!"
keywords = ["int", "float", "bool", "true", "false", "if", "else", "then", "endif", "while", "whileend", "do", "doend", "for", "forend", "input", "output", "and", "or", "not"]
separators = ["'", "(", ")", "{", "[", "[", "]", ",", ".", ":", ";", "sp"]
operators = ["*","+","-","=","/",">","<","%", "$"]
formatters = ['\n', '\t']

buffer = []
lexedList = []

testFile = "inputTextFiles/sample2.txt"

#reads text file into buffer
#in the future will probably need to read the file in batches to avoid memory buffer overload
#for now it should be fine though

#@param fileName - string of file name of text file to read in
def readFileToBuffer(fileName):

	with open(fileName, 'r') as file:
		for line in file:
			if comments not in line:
				splitLine = line.split(' ')
				for token in splitLine:
					buffer.append(token)

#@param aBuffer - a buffer to parse. Buffer should contains tokens with operators in them
# Function should separate the tokens by operators
def parseBufferForOperators( aBuffer ):
	bufferIter = 0
	while( bufferIter != len( buffer ) ):
		#print( len( buffer ) )
		line = buffer[bufferIter]
		#buffer.remove(line)
		
		operatorParsed = False

		for operator in operators:
			if operator == line:
				continue
			if operator in line:
				buffer.remove(line)
				operatorParsed = True

				splitLine = line.split( operator )
				splitLineWithOperator = []

				for item in splitLine:
					if( item != '' ):
						splitLineWithOperator.append( item )
					splitLineWithOperator.append( operator )
				splitLineWithOperator.pop()

				#print(splitLine)
				for token in reversed(splitLineWithOperator):
					buffer.insert( bufferIter, token )
				bufferIter = bufferIter + len( splitLineWithOperator )
				break
		
		if( not( operatorParsed ) ):
			bufferIter = bufferIter + 1

#@param aBuffer - a buffer to parse. Buffer should contains tokens with Separators in them
# Function should separate the tokens by separator
def parseBufferForSeparators( aBuffer ):
	bufferIter = 0
	while( bufferIter != len( buffer ) ):
		#print( len( buffer ) )
		line = buffer[bufferIter]
		#buffer.remove(line)
		
		separatorParsed = False

		for separator in separators:
			if separator == line:
				continue
			if separator in line:
				buffer.remove(line)
				separatorParsed = True

				splitLine = line.split( separator )
				splitLineWithSeparator = []

				for item in splitLine:
					if( item != '' ):
						splitLineWithSeparator.append( item )
					splitLineWithSeparator.append( separator )
				splitLineWithSeparator.pop()

				#print(splitLine)
				for token in reversed(splitLineWithSeparator):
					buffer.insert( bufferIter, token )
				bufferIter = bufferIter + len( splitLineWithSeparator )
				break
		
		if( not( separatorParsed ) ):
			bufferIter = bufferIter + 1

def parseBufferForFormatters( aBuffer ):
	bufferIter = 0
	while( bufferIter != len( buffer ) ):
		#print( len( buffer ) )
		line = buffer[bufferIter]
		#buffer.remove(line)
		
		formatterParsed = False

		for formatter in formatters:
			if formatter == line:
				continue
			if formatter in line:
				buffer.remove(line)
				formatterParsed = True

				splitLine = line.split( formatter )
				splitLineWithFormatter = []

				for item in splitLine:
					if( item != '' ):
						splitLineWithFormatter.append( item )
					splitLineWithFormatter.append( formatter )
				splitLineWithFormatter.pop()

				#print(splitLine)
				for token in reversed(splitLineWithFormatter):
					buffer.insert( bufferIter, token )
				bufferIter = bufferIter + len( splitLineWithFormatter )
				break
		
		if( not( formatterParsed ) ):
			bufferIter = bufferIter + 1

def printBuffer( aBuffer ):
	for line in aBuffer:
		print(line)
	print("========================")

readFileToBuffer(testFile)

parseBufferForOperators( buffer )

parseBufferForSeparators( buffer )

parseBufferForFormatters( buffer )

print(buffer)

# l = "cows,fdsa"
# print(l.split('cows'))
# print(l.split('cows,'))