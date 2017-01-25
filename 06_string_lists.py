'''
http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

EXERCISE 6
STRING LISTS

Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
'''
palindrome = True

userString = raw_input("Enter a word: ")

for letter in range(0, len(userString)//2 + 1):
    if (userString[letter] != userString[-1 * (letter + 1)]):
        palindrome = False
        break
        
if(palindrome == True):
    print("It is a palindrome")