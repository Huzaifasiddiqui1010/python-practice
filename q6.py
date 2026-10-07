def check_password(password): 
    length = len(password)
    has_upper = False
    has_digit = False
    if length >= 8:
        for char in password:
            if char.isupper() :
                has_upper = True
            if char.isdigit() :
                has_digit = True
        return has_upper and has_digit         
    else:
        return False
                
# input = Umar1234
password = input("Enter the password : ") 
print(check_password(password))   