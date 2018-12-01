original = input("Please input a string?")
reverse = original[-1::-1]

if reverse == original:
    print("Its a palindrome .")
else:
    print("Its not a palindrome")
