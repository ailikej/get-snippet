Author: Eric Jiang
Email: ericjiangpsu@gmail.com
Date: 2/05/2021
Time spent on this project =~ 5 hours

# Introduction 
This folder includes python files:
get_snippet.py, test_get_snippet.py, get_snippet_extension1.py, get_snippet_extension2.py and get_snippet_extension3.py
The problem statement is written in the "Eric takehome.txt" file.

# Getting Started
To run each python program, simply type command in terminal accordingly such as:
python3 get_snippet.py

To run the unit test of the original method to the problem:
python3 test_get_snippet.py 
or 
python3 -m unittest test_get_snippet.py

Please open each Python file to review the codes and comments and the cases for the unit test. 

# Result
The original method is able to extract the shortest substring between the two key words in a case insensitive way and not being
affect by the punctuation characters adjasent to the key words. Two-pointer method is implemented to solve the problem. Please see the code comments for more explanation. The method passes all the unit test cases.

## Extension 1
The extention_1 method used class to construct the input string and process the data cleaning part. By doing so, it improves the runtime of calling 10000 times of the get_snippet method substantially from 1.34 sec (original method) to 0.055 sec.   

## Extension 2
The extention_2 method is able to extract the 3 more words before and after the substring between the two key words. It is implemented in a way that would not exceed the boundary of the input string.

## Extension 3
The extention_3 is also implemented.
The parameter of the get_snippet method changes from 2 key words (kw1, kw2) to a list of key words (kwList).
The function is able to return the shortest substring in the input string between any of two key words in keList.
The idea is to use stack to keep track of the last found key word is different to the new found one. Please review the codes for details.
