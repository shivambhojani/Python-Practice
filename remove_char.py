def remove(str, char):
    new_str = ""
    for i in range(0, len(str)):
        if i != char:
            new_str = new_str + str[i]
    return new_str


a = input("String: ")
b = int(input("which Character you want to remove: "))
b = b-1
new_string = remove(a, b)
print(new_string)

