#Ask the user for a string and print out whether this string is a palindrome or not.
userString = raw_input("Enter a word: ")

palindrome = True

for letter in range(0, len(userString)//2 + 1):
    if (userString[letter] != userString[-1 * (letter + 1)]):
        palindrome = False
        break
        
if(palindrome == True):
    print("It is a palindrome")
