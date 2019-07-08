from random import randint

def algorithm(target_number, buffer_size):
 for j in range(buffer_size):
    flag1=1
    flag2=1
    random_number=[]
    for i in range(3):
        if i==0:
            number0=randint(0, 9)
            random_number.append(number0)
            total =random_number[i]
        elif  i==1:
            while flag1==1:
                number1=randint(0, 9)
                if random_number[0]!=number1:
                    random_number.append(number1)
                    total =total+random_number[i]
                    flag1=0
                    
        elif i==2:
             while flag2==1:
                number2=randint(0, 9)
                if random_number[0]!=number2 and random_number[1]!=number2:
                    random_number.append(number2) 
                    total =total+random_number[i]
                    flag2=0
    if total==21:
        print(random_number)
        print("total=21 (success)")
    else: 
        print(random_number)
        print("the total is not equal 21 (fail)")

total =21
size=15
algorithm(total,size)