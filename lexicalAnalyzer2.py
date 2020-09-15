import sys
import re
def main():
	inFile = "inputTextFiles/sample2.txt"

	with open(inFile, 'r') as file:
		# changed it to pass as file
		lexicalAnalyzerTest(file)


# just made this function randomly to see if it works 
# and I guess I finished making the project somehow
def lexicalAnalyzerTest(file):
	comments = "!"
	keywords = {"int", "float", "bool", "true", "false", "if", "else", "then", "endif", "while", "whileend", "do", "doend", "for", "forend", "input", "output", "and", "or", "not"}
	separators = {"'", "(", ")", "{", "}", "[", "]", ",", ".", ":", ";", "sp"}
	operators = {"*","+","-","=","/",">","<","%"}
	newStr = ""
	for line in file:
		if comments in line:
			continue
		for letter in line:
			if letter == " " or letter == "\n":
				continue
			if not letter.isalpha() and not letter.isnumeric():
				if newStr:
					if letter == "$":
						newStr += letter
					print("IDENTIFIER\t=\t" + newStr)
					newStr = ""
				if letter in separators:
					print("SEPARATOR\t=\t" + letter)
				elif letter in operators:
					print("OPERATOR\t=\t" + letter)
			else:
				if newStr in keywords:
					print("KEYWORD\t\t=\t" + newStr)
					newStr = ""
				newStr += letter



if __name__ == "__main__":
	main()
