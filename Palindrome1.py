inputStr = input("Enter the String:")
inputStr_edit = inputStr.replace(" ", "").replace("/t", "")
inputStr_reversed = inputStr_edit[::-1]
print(inputStr_reversed)
if(inputStr_edit == inputStr_reversed):
    print("The string is a Palindrome")
else:
    print("The string is not a Palindrome")
