# def is_palindrome(text):
#     text = text.replace(" ","").lower()
#     for char in text :
#         if text[::1] == text[::-1] :
#             return True
#         else :
#             return False

# text = input("Enter the string: ")
# print(is_palindrome(text))

def is_palindrome(text):
    text = text.replace(" ","").lower()

    return text[::] == text[::-1]

text = input("Enter the string: ")
print(is_palindrome(text))