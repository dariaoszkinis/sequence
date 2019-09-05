n = int(input("Enter the length of the sequence:  "))
count_number = 0
num1 = 1
num2 = 2
num3 = 3
sum = 0

while count_number <= n:

    if count_number == 0:
            sum = num1
            print(sum)
    elif count_number == 1:
            sum = num1 + 1    
            print(sum)
    elif count_number == 2:    
        sum = num1+num2
        print(sum)
    else:
        sum = num1+num2+num3
        num1 = num2
        num2 = num3
        num3 = sum 
        print(sum)
    count_number += 1