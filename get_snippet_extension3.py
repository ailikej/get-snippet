'''
Problem
Given a description string, and 2 search strings, find a substring that starts with one of the keywords, and ends with another keyword.
Some clarifications we had:
# if not found, return “”
# if more than 1 possible result, return the shortest one 
# shortest of words
# shortestStr 
# Start with 1 of the keyword, end with another 1
# casing? To simplify, assume all input is in lower case
# Assume Input is always 2 keywords
# If (kw1/kw2/ or both) do not exist in description, return “”

'''

import string
import timeit

# create a class and store input string to its constructor and prepare the puncturation free lowercase word list there
class DecsriptionSearch:
	def __init__(self, description):
		self.wordList = description.split()
		self.wordListCopy = self.wordList[:]
		for i in range(len(self.wordList)):
			for c in string.punctuation:
				self.wordList[i] = self.wordList[i].replace(c, "").lower()

	def get_snippet(self, kwList):
		
		# convert key words to lowercase
		for i in range(len(kwList)):
			kwList[i] = kwList[i].lower()

		# check if there're at lest 2 key words exist in the input word list, if not, return empty string
		kwStack = [" "]
		kwCount = 0

		for word in self.wordList:
			if word in kwList:
				kwStack.append(word)
				if kwStack[-1] != kwStack[-2]:
					kwCount += 1
		if kwCount < 2:
			return ""


		min_length = float("inf")
		substringIndices = [0, 0]

		# locate the first key word's index
		start = 0
		while self.wordList[start] not in kwList:
			start += 1

		# define which key word is found first and second, later these two will be switched
		kwFoundStack = [self.wordList[start]]

		'''Use two-pointer method to iterate the word list to locate the indices [left, right] of the substring between two different key words
		The indcies will update once the next different key word is found and the length of the new substring is shorter
		The last found key word will update by using a stack to compare the new found one and the iteration continues till the end of the word list.
		The final resulted indices will be used to slice the original wordlist, with the puncturation and capitalization of characters
		Fianlly, the substring words will join together and return as a string
		Time Complexity O(n)

		'''
		left = start
		for right in range(start + 1, len(self.wordList)):
			if self.wordList[right] == kwFoundStack[-1]:
				left = right
			if self.wordList[right] in kwList and self.wordList[right] !=  kwFoundStack[-1]:
				kwFoundStack.append(self.wordList[right])
				if right - left < min_length:
					substringIndices = [left, right] 
					min_length = min(min_length, right - left)
					
				left = right
		return ' '.join(self.wordListCopy[substringIndices[0]:substringIndices[1]+1])

		'''	Overall Time Complexity is also O(n) since all the sub methods are O(n).
		Space Complexity will be O(n) becasue it takes n space to store the copy of the original word list, and the return string
		can be the entire string by slicing.'''


s1 = DecsriptionSearch("CSS Today we are talking about coding with Java. Also want to talk CSS about python. But I like Java more.")
s2 = DecsriptionSearch("Java 1 2 3 4 5 Java 1 2 3 4 JavaScrtip 1 2 3 CSS 1 CSS 1 Java 1 2 3 4 python")
print(s1.get_snippet(["Java", "python", "CSS"])) 
print(s2.get_snippet(["Java", "python", "CSS", "HTML", "JavaScrtip"])) 