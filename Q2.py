name = input("Enter the string")

count = 0
for char in name :
    if char.lower() in "aeiou":
        count+=1

print("Number of vowels:",count)    