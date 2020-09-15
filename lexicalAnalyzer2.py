import sys
import re

def main():
	# specify the input file needed for this program
	directory = "inputTextFiles/"
	inFile = "sample2.txt"
	try:
		userFile = input("input filename here(will draw from inputTextFiles directory): ")
		with open(directory + userFile, 'r') as file:
			lexicalAnalyzerTest(file)
	except FileNotFoundError:
		print("invalid file... will use default file\n")
		with open(directory + inFile, 'r') as file:
			lexicalAnalyzerTest(file)

def lexicalAnalyzerTest(file):
	comments = "!"
	keywords = {"int", "float", "bool","void", "true", "false", "if", "else", "then", "endif", "while", "whileend", "do", "doend", "for", "forend", "input", "output", "and", "or", "not"}
	separators = {"'", "(", ")", "{", "}", "[", "]", ",", ".", ":", ";", "sp"}
	operators = {"*","+","-","=","/",">","<","%"}
	newStr = ""
	print("TOKENS\t\t\tLexemes\n")
	for line in file:
		# skip for all comments
		if comments in line:
			continue
		for letter in line:
			# skip new lines and spaces
			if letter == " " or letter == "\n":
				continue
			# check for non numeric and non alpha characters meaning it
			# can't be a part of the identifiers unless it's a '$'
			if not letter.isalpha() and not letter.isnumeric():
				if newStr:
					# check for '$' meaning it can still be an IDENTIFIER
					if letter == "$":
						newStr += letter
					# will print IDENTIFIER here because once you reach a 
					# non numeric and non alpha character, we will have a 
					# string containing the identifier
					print("IDENTIFIER\t=\t" + newStr)
					newStr = ""
				if letter in separators:
					print("SEPARATOR\t=\t" + letter)
				elif letter in operators:
					print("OPERATOR\t=\t" + letter)
			else:
				if newStr in keywords:
					# check to see if it's a reserved keyword
					print("KEYWORD\t\t=\t" + newStr)
					newStr = ""
				newStr += letter

if __name__ == "__main__":
	main()
