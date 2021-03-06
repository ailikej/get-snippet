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

def get_snippet(description, kw1, kw2):
	
	# clean the input string by exluding the puntuation characters and make the string lowercase.  
	# Time Complexity O(n), where n == number of charaters
	wordList = description.split()
	wordListCopy = wordList[:]
	
	for i in range(len(wordList)):
		for c in string.punctuation:
			wordList[i] = wordList[i].replace(c, "").lower()

	# lowercase the tow key words to be searchable in the lowercased input string
	kw1 = kw1.lower()
	kw2 = kw2.lower()

	# check if either kw1 or kw2 exist, if one of them or both missing, return empty string
	# Time Complexity O(n)
	kw1Exists = False
	kw2Exists = False
	for word in wordList:
		if word == kw1:
			kw1Exists = True
		if word == kw2:
			kw2Exists = True

	if not (kw1Exists and kw2Exists):
		return ""

	min_length = float("inf")
	substringIndices = [0, 0]

	# locate the first key word's index
	start = 0
	while wordList[start] != kw1 and wordList[start] != kw2:
		start += 1

	# define which key word is found first and second, later these two will be switched
	kwFirstFound = wordList[start] 

	if kwFirstFound == kw1:
		kwSecondFound = kw2
	else:
		kwSecondFound = kw1

	'''Use two-pointer method to iterate the word list to locate the indices [left, right] of the substring between the two key words
	The indcies will update once the next different key word is found and the length of the new substring is shorter
	The key words will switch and the iteration continues till the end of the word list.
	The final resulted indices will be used to slice the original wordlist, with the puncturation and capitalization of characters
	Fianlly, the substring words will join together and return as a string
	Time Complexity O(n)

	'''
	left = start
	for right in range(start + 1, len(wordList)):
		if wordList[right] == kwFirstFound:
			left = right
		if wordList[right] == kwSecondFound:
			if right - left < min_length:
				substringIndices = [left, right] 
				min_length = min(min_length, right - left)
				kwFirstFound, kwSecondFound = kwSecondFound, kwFirstFound
			left = right
	return ' '.join(wordListCopy[substringIndices[0]:substringIndices[1]+1])

	'''	Overall Time Complexity is also O(n) since all the sub methods are O(n).
	Space Complexity will be O(n) becasue it takes n space to store the copy of the original word list, and the return string
	can be the entire string by slicing.'''


# Sample test case  
# (More test cases are in the test_get_snippet.py file)
# print(get_snippet("Today we are talking about coding with Java. Also want to talk about python. But I like Java more.", "Java", "python"))


# Runtime calculator
start = timeit.default_timer()
for i in range(10000):
	get_snippet("Today we are talking about coding with Java. Also want to talk about python. But I like Java more.", "Java", "python")
stop = timeit.default_timer()
print('Time: ', stop - start)  # 1.358 

# comparing 1.358 sec with the runtime of the get_snippet_extension1 with using constructor 0.05575 sec , 
# the extention 1 method is much faster!!
