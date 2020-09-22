import sys
import re

comments = "!"
keywords = {"int", "float", "bool", "true", "false", "if", "else", "then", "endif", "while", "whileend", "do", "doend", "for", "forend", "input", "output", "and", "or", "not"}
separators = {"'", "(", ")", "{", "[", "[", "]", ",", ":", ";", "sp"}
operators = {"*","+","-","=","/",">","<","%", "$"}
formatters = ['\n', '\t']

#reads text file into buffer
#in the future will probably need to read the file in batches to avoid memory buffer overload
#for now it should be fine though

#@param fileName - string of file name of text file to read in
def readFileToBuffer(fileName, aBuffer):

	with open(fileName, 'r') as file:
		for line in file:
			if comments not in line:
				splitLine = line.split(' ')
				for token in splitLine:
					aBuffer.append(token)

#@param aBuffer - a buffer to parse. Buffer should contains tokens with operators in them
# Function should separate the tokens by operators
def parseBufferForOperators( aBuffer ):
	bufferIter = 0
	while( bufferIter != len( aBuffer ) ):
		line = aBuffer[bufferIter]
		
		operatorParsed = False

		for operator in operators:
			if operator == line:
				continue
			if operator in line:
				aBuffer.remove(line)
				operatorParsed = True

				splitLine = line.split( operator )
				splitLineWithOperator = []

				for item in splitLine:
					if( item != '' ):
						splitLineWithOperator.append( item )
					splitLineWithOperator.append( operator )
				splitLineWithOperator.pop()

				for token in reversed(splitLineWithOperator):
					aBuffer.insert( bufferIter, token )
				break
		
		if( not( operatorParsed ) ):
			bufferIter = bufferIter + 1

#@param aBuffer - a buffer to parse. Buffer should contains tokens with Separators in them
# Function should separate the tokens by separator
def parseBufferForSeparators( aBuffer ):
	bufferIter = 0
	while( bufferIter != len( aBuffer ) ):
		line = aBuffer[bufferIter]
		
		separatorParsed = False

		for separator in separators:
			if separator == line:
				continue
			if separator in line:
				aBuffer.remove(line)
				separatorParsed = True

				splitLine = line.split( separator )
				splitLineWithSeparator = []

				for item in splitLine:
					if( item != '' ):
						splitLineWithSeparator.append( item )
					splitLineWithSeparator.append( separator )
				splitLineWithSeparator.pop()

				for token in reversed(splitLineWithSeparator):
					aBuffer.insert( bufferIter, token )
				break
		
		if( not( separatorParsed ) ):
			bufferIter = bufferIter + 1

def parseBufferForFormatters( aBuffer ):
	bufferIter = 0
	while( bufferIter != len( aBuffer ) ):
		line = aBuffer[bufferIter]
		
		formatterParsed = False

		for formatter in formatters:
			if formatter == line:
				continue
			if formatter in line:
				aBuffer.remove(line)
				formatterParsed = True

				splitLine = line.split( formatter )
				splitLineWithFormatter = []

				for item in splitLine:
					if( item != '' ):
						splitLineWithFormatter.append( item )
					splitLineWithFormatter.append( formatter )
				splitLineWithFormatter.pop()

				for token in reversed(splitLineWithFormatter):
					aBuffer.insert( bufferIter, token )
				break
		
		if( not( formatterParsed ) ):
			bufferIter = bufferIter + 1

def printBuffer( aBuffer ):
	for line in aBuffer:
		print(line)
	print("========================")

#@param aFileName - filename of the file to parse
#parses the given file and returns a buffer of the separated tokens
def separateTokens(aFileName):
	retBuffer = []
	readFileToBuffer(aFileName, retBuffer)
	parseBufferForOperators( retBuffer )
	parseBufferForSeparators( retBuffer )
	parseBufferForFormatters( retBuffer )
	return retBuffer

