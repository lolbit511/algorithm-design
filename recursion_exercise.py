# ask user to input interger and print each digit of the interger in seperate lines starting from the first digit to the last

def printDigit2(n):
    if n>10:
        printDigit2(int(n/10))
    print (n%10)

num = int(input("insert number: "))

printDigit2(num)