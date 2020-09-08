import sys

def main():
	inFile = "inputTextFiles/sample1.txt"

	with open(inFile, 'r') as file:
		for line in file:
			lexicalAnalyzer(line)

# helper function to check if word is within token
def lexicalHelper(word, token):
	if word in token:
		print("KEYWORD = ", word)
	
def lexicalAnalyzer(line):
	comments = "!"
	keywords = {"int", "float", "bool", "true", "false", "if", "else", "then", "endif", "while", "whileend", "do", "doend", "for", "forend", "input", "output", "and", "or", "not"}
	separators = {"'", "(", ")", "{", "[", "[", "]", ",", ".", ":", ";", "sp"}

	# case to check if line is a comment, which if it is we do nothing
	if comments in line:
		return

	# split lines using space as a delimiter
	# TODO: figure out some way to split with separators as well
	imbored = line.split(' ')
	for word in imbored:
		lexicalHelper(word, keywords)

if __name__ == "__main__":
	main()