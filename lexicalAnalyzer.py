import sys
import re
def main():
	inFile = "inputTextFiles/sample1.txt"

	with open(inFile, 'r') as file:
		for line in file:
			lexicalAnalyzer(line)

# helper function to check if word is within token
# returns True if the word is within token
def lexicalHelper(word, token, tokenType):
	if word in token:
		if tokenType == "keyword":
			print("KEYWORD = ", word)
		elif tokenType == "operator":
			print("OPERATOR = ", word)
		return True

# [DONE]: helper function to check if the word is a valid identifier
# returns True if word is a valid identifier
def identifierCheck(word):
	# checks if the first letter is a alpha letter, otherwise it is an invalid identifier
	if word[0].isalpha():
		return True
	else:
		return False

# [DONE] check is the string is a integer or a float
def numberCheck(word):
	if word.isnumeric():
		return True
	else:
		try:
			float(word)
			return True
		except:
			return False


def lexicalAnalyzer(line):
	comments = "!"
	keywords = {"int", "float", "bool", "true", "false", "if", "else", "then", "endif", "while", "whileend", "do", "doend", "for", "forend", "input", "output", "and", "or", "not"}
	separators = {"'", "(", ")", "{", "[", "[", "]", ",", ".", ":", ";", "sp"}
	operators = {"*","+","-","=","/",">","<","%"}

	# case to check if line is a comment, which if it is we do nothing
	if comments in line:
		return

	# [TODO]: figure out some way to split with separators as well
	# for char in word:
	# 	if char in token:
	#		word, separator = word.split(char)

	# testingLine = "if (num1 > num2)"
	# GOAL: to get ['if', '(', 'num1', '>', num2, ')']
	# CURRENTLY: we have ['if', '(num1', '>', 'num2)']
	# print(re.split("(", testingLine))


	# split lines using space as a delimiter
	imbored = line.split(' ')
	print(f'parsed words: {imbored}')

	# Assumes the the list is parsed as such:
	# ['if', '(', 'num1', '>', num2, ')']
	# ['int', 'number', '=', '9', ';']
	for word in imbored:
		#print(word)
		# [DONE] Case 1: Check if the word is token key word
		if lexicalHelper(word, keywords, "keyword") == True:
			continue

		# [TODO] Case 2: Check if the word is an separator

		# [DONE] Case 3: Check if the word is a operator
		if lexicalHelper(word, operators, "operator") == True:
			continue

		# [DONE] Case 4: Check if the word is an integer or a float
		if numberCheck(word) == True:
			continue

		# [DONE] Case 5: Check if the word is a valid identifer
		if identifierCheck(word) == True:
			continue



if __name__ == "__main__":
	main()
