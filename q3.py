def find_max(a,b,c):
    if(a>b and a>c):
        # print(a,"is the biggest number")
        return a
    elif(b>c):
        # print(b,"is the biggest number")
        return b
    else:
        # print(c,"is the biggest number")
        return c

# print({f}"The Biggest Value is",find_max(4,4,4))
print(f'The biggest {find_max(1, 2, 3)} value is')