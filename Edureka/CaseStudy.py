#1. Write a program which will find factors of given number and find whether the factor is even or odd.

x = int(input("Enter any number : "))
print("The factors of",x,"are:")
for i in range(1, x + 1):
    if x % i == 0:
        if i % 2 == 0:
            print(i," Even")
        else:
            print(i," Odd")

#2. Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically.

my_str = input("Enter a string: ")
words = [word.lower() for word in my_str.split()]
words.sort()
print("The sorted words are:")
for word in words:
   print(word)

#3.Write a program, whichwill find all the numbers between 1000 and 3000 (both included) such that each digit of a number is an even number. The numbers obtained should be printed in a comma separated sequence on a single line.
values = []
j = int(input("Enter first number : "))
k = int(input("Enter second number : "))
for i in range(j, k+1):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))

#4.Write a program that accepts a sentence and calculate the number of letters and digits.
s = input("Input a string : ")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)


#5.Design a code which will find the given number is Palindrome number or not
test_number = int(input("Enter a number : "))
print("The original number is : " + str(test_number))
result = str(test_number) == str(test_number)[::-1]
print("Is the number palindrome ? : " + str(result))