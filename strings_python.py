# Print

message = "Hello, World!"
#print(message)

#print("Any message we can pass to the print function will be printed to the console.")

message = 'Single quote message'
#print(message)

message = 'Single "quote with double quote" message'
#print(message)

message = "Double 'quote with single quote' message"
#print(message)

# Print the length of the message
#print(len(message))  

# Print the 10th character of the message
#print(message[10])

# Print the first 10 characters of the message
# Will start at 0 till 9, 10 is not included
#print(message[0:10])  

#   Print the characters from the 10th character to the end of the message
# Also called slicing
#print(message[10:])  

#print(message.lower())  # Print the message in lower case
#print(message.upper())  # Print the message in upper case

#print(message.count("e")) # Print the number of occurrences of the letter "e" in the message
#print(message.count('o')) # Print the number of occurrences of the letter "o" in the message

#print(message.find("quote")) # Print the index of the first occurrence of the word "quote" in the message
#print(message.find("notInMessage")) # Print -1 if the word is not found in the message

#Error: TypeError: count() takes at least 1 argument (0 given)
#print(message.count()) # Print the number of characters in the message

message.replace('quote', 'Universe') # Replace the word "quote" with "Universe" in the message
#print(message) # Print the message after the replacement
# NO CHANGE, WE SHOULD ASSIGN TO NEW VARIABLE OR REASSIGN TO THE SAME VARIABLE
# Double 'quote with single quote' message

message = message.replace('quote', 'Universe') # Reassign the replaced message to the same variable
#print(message) # Print the message after the replacement

greeting = 'Hello'
name = 'Alice'
message = greeting + ', ' + name + '! Welcome to Python programming.' # Concatenate the greeting and name to create a message
#print(message) # Print the message after the replacement

# Using f-string to format the message, instead of +
# Only in Python 3.6 and above
message = f'{greeting}, {name}! Welcome to my programming.'
#print(message) # Print the message after the replacement

# Using format method to format the message, instead of +
message = '{}, {}! Welcome to format programming.'.format(greeting, name) # Using format method to format the message
#print(message) # Print the message after the replacement

# dir method will list all the attributes and methods of the message variable
#print(dir(message)) # Print the attributes and methods of the message variable

# Will return 'None' in this case, as if the attribute or method is not found
#print(help(message)) # Print the help documentation for the name variable
#Error: AttributeError: 'str' object has no attribute 'help'
#print(message.help()) # Print the help documentation for the message variable

#print(help(str)) # Print the help documentation for the str class

# help for the lower method of the str class
print(help(str.lower)) # Print the help documentation for the lower method of the str class

