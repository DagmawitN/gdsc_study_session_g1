for n in range(100):
    if n < 9:
        print(f"0{n} ,", end = " ")
    elif n == 99 :
          print ( n )
    else:
         print(n , ", ", end = " " )


def print_pattern(num , symbol):
    n = 1
    for i in range(num):
        for j in range(n):
            print(symbol, end="")
        print()
        n += 2


char = input ("Enter character to print : ")
line = int (input ("Number of lines to print : "))
print_pattern(line,char)



word = input ("Please enter the word to check : ")
check = ""
for n in word:
    check = n + check

if (check == word):
    print ("The word you enterd is paindrome.")
else : 
    print ("The word you entered is not palindrome.")  


sum = 0
count_three = 0
count_five = 0
for n in range(1,51) : 
    if n%2 == 0 :
        sum = sum + n
        if n%3 == 0 :
            print("Three")
            count_three +=1
        elif n%5 ==0 :
            print("Five")
            count_five +=1
        else :
            print(n)

print ("Sum of numbers 1 - 50 :" , sum)
print("Amount of even numbers which are multiple of three : " , count_three)
print("Amount of even numbers which are multiple of five : " , count_five)