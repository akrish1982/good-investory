# str reverse
yorn= input('do u want to reverse a string ? type y or n : ')
newstr = ""
if yorn == 'y':
    str=str(input('enter the string to reverse: '))
    for i in range(len(str)-1, 0-1, -1):
        print (str[i])
        newstr += str[i]
    print(newstr)
# palindrome
yorn= input('do u want to check a string for palindrome? type y or n : ')
#if yorn == 'y':