#Write a Python program to test whether a passed letter is a vowel or not.
  
# user input  
character = input("Enter a character: ")  
  
# list of vowels  
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  
  
# Check if the character is a vowel or not  
if character in vowels:  
    print(f"The character '{character}' is a vowel!")  
else:  
    print(f"The character '{character}' is a consonant!")  