def sortingnum(numcount):

    list = []
    for _ in range(numcount):
       nums = int(input("Enter the value: "))
       list.append(nums)

    list.sort()
    sorted = set(list)
    return sorted

a = int(input("How Many Number: "))
print(sortingnum(a))
