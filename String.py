text = input("Enter a string: ")
print("Characters in the string:")
for ch in text:
    print(ch)
vowels="aeiouAEIOU"
count=0
for ch in text:
    if ch in vowels:
        count=count+1
print("Number of vowels:",count)
reverse=""
for ch in text:
    reverse=ch+reverse
print("Reversed string:",reverse)
upper_text=text.upper()
print("\nUppercase:",upper_text)
lower_text=text.lower()
print("Lowercase:",lower_text)
if text==reverse:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
