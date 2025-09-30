# Define a function that converts a string to uppercase manually
def to_upper_manual(s):
    # Initialize an empty string to store the result
    result = ""
    
    # Loop through each character in the input string
    for char in s:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert lowercase to uppercase by subtracting 32 from its ASCII value
            result += chr(ord(char) - 32)
        else:
            # If it's not a lowercase letter, keep it as is
            result += char
    
    # Return the final uppercase string
    return result

# Call the function with a sample string and print the result
print(to_upper_manual("ctrl alt elite")) # Output: CTRL ALT ELITE