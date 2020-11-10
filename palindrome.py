def isPalindrome(x):
    x = list(x)
    l = len(x)
    print(x, l)
    for i in range(0, int(l)):
        print(i,x[i], x[l-i-1])
        print(i)
        if x[i] != x[l-i-1]:
            return False
        return True


s = input("String= ")
result = isPalindrome(s)
if result:
    print("Yes")
else:
    print("No")
