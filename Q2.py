name = input("Enter the string").lower()

count = 0
for char in name:
    if char in "aeiou":
        count+=1

print("Number of vowels:",count)    