#1. Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
'''a=int(input("input the first number  "))
b=int(input("input the second number  "))

if a==b:
    print("1")
elif a>b:
    print("2")
else:
    print("3")'''


#2.  Print "Hello" if a is equal to b, or if c is equal to d.
'''a=int(input("input the first number  "))
b=int(input("input the second number  "))
c=int(input("input the third number  "))
d=int(input("input the fourth number  "))
if a==b or c==d :
    print("Hello")'''



#3. Print "Hello" if a is equal to b, and c is equal to d.
'''a=int(input("input the first number  "))
b=int(input("input the second number  "))
c=int(input("input the third number  "))
d=int(input("input the fourth number  "))
if a==b and c==d :
    print("Hello")'''


#4. For given integer x, print ‘True’ if it is positive, print ‘False’ if it is negative and print ‘zero’ if it is 0.
'''x=int(input("input a integer  "))
if x>0:
    print("true")
elif x<0:
    print("false")
else:
    print("zero")
'''


#5. Check whether the user input number is even or odd and display it to user.
'''x=int(input("input a number  "))
if x%2==0:
    print("even")
else:
    print("odd")
'''

#6. WAP which accepts marks of four subjects and display total marks, percentage and grade.
# Hint more :than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail
'''a=float(input("input the marks of first subject  "))
b=float(input("input the marks of second subject  "))
c=float(input("input the marks of third subject  "))
d=float(input("input the marks of fourth subject  "))
total=a+b+c+d
print ("The Total marks is:   ", total, "/ 400")
percentage= ((total) / 400. * 100)
print ("The percentage is:   ", percentage, "%")
if percentage >= 70:
    grade = 'distintion'
    print ('the grade division is ', grade)
elif percentage >= 60 and percentage < 70:
    grade = 'first'
    print ('the grade division is ', grade)
elif percentage >= 40 and percentage < 60:
    grade = 'pass'
    print ('the grade division is ', grade)
else:
    print ('the grade division is fail')'''

#7. What is the output of ‘APPLE’ > ‘apple’?
'''false'''

#8 Write a Python program to display your details like name, age, address in three different lines.
'''name=input("enter your name")
age=input("enter you age")
address=input("enter you address")
print (name)
print (age)
print (address)'''

#9 Write a python program which accepts the radius of circle from user and compute the area.
'''radius=int(input("enter the radius of a circle"))
area=(22/7)*(radius**2)
print("the area of the circle is " ,area)'''

# 10 A school decided to replace the desks in three classrooms. Each desk sits two students. 
# Given the number of students in each class, print the smallest possible number of desks that can be purchased.
#  The program should read three integers: the number of students in each of the three classes, a, b and c respectively.

#Hint.  first testIn the there are three groups. The first group has 20 students and thus needs 10 desks.
#  The second group has 21 students, so they can get by with no fewer than 11 desks. 
# 11 desks are also enough for the third group of 22 students. So, we need 32 desks in total.

'''c1=int(input("enter the number of student in a "))
c2=int(input("enter the number of students in b "))
c3=int(input("enter the number of students in c "))
desk=int((c1+c2+c3)/2 ) + 1
print ("the number of desks are :",desk)
'''

#11Write a python program which calculates tax of an employee with given condition:
#  Salary            	       Tax Rate
#  Below 20000                  15%
#  20000 to 50000               25%
#  50000 to 100000              30%
#  Above 100000                 35%

'''salary=int(input("enter the salay"))
if salary < 20000 :
    tax = (15/100) * salary
    print ("your tax amount is ",tax)
elif salary > 20000 and salary >=50000:
    tax = (25/100) * salary
    print ("your tax amount is ",tax)
elif salary > 50000 and salary >=10000:
    tax = (30/100) * salary
    print ("your tax amount is ",tax)
else:
    tax = (35/100) * salary
    print ("your tax amount is ",tax)'''

#122 Given three integers, print the smallest one. (Three integers should be user input)
'''a=int(input("input the first number"))
b=int(input("input the second number"))
c=int(input("enter the third number"))
if ((a<=b) and (a<=c)) :
    print (a)
elif (b<=a) and (b<=c) :
    print (b)
else:
    print (c)'''

#13 N students take K apples and distribute them among each other evenly.
#  The remaining (the undivisible) part remains in the basket. 
# How many apples will each single student get? How many apples will remain in the basket? 
# The program reads the numbers N and K. It should print the two answers for the questions above.

'''n=int(input("enter the number of student "))
a=int(input("enter the number of apples "))
d=int(a/n)
print ("each student will get" ,d,"apples")
rem=a-(d*n)
print (rem,"apples remain in basket")'''



#14 Check whether 5 is in list of first 5 natural numbers or not. Hint: List => [1,2,3,4,5]
'''x=(5)
print(0 < int(x) <= 5)'''



#15Write a program that asks the user for a number in the range of 1 to 12. 
# The program should display the corresponding month, where 
#1=january, 2=february,3=march,4=april,5=may,6=june,7=july, 8=august,9=september,10=october,11=november,12=december. 
# The program should display an error message if the user enters a number that is outside the range of 1 to 12.

'''n=int(input("input a number"))
if n==1:
    print ("januay")
elif n==2:
    print ("febuary")
elif n==3:
    print ("march")
elif n==4:
    print ("april")
elif n==5:
    print ("may")
elif n==6:
    print ("june")
elif n==7:
    print ("july")
elif n==8:
    print ("august")
elif n==9:
    print ("september")
elif n==10:
    print ("october")
elif n==11:
    print ("november")
elif n==12:
    print ("december")
else:
    print ("enter a num between 1 to 12")'''

#16. Given x = 5, what will be the value of x after we run x+=3?



# 17 A school has following rules for grading system:
#a. Below 25 - F
#b. 25 to 45 - E
#c. 45 to 50 - D
#d. 50 to 60 - C
#e. 60 to 80 - B
#f. Above 80 - A
#Ask user to enter marks and print the corresponding grade.

'''m=int(input("enter the marks"))
if m < 25 :
    print  ("F")
elif m>=25 and (m<45):
    print ("E")
elif m>=45 and (m<50):
    print ("D")
elif m>=50 and (m<60):
    print ("C")
elif m>=60 and (m<80):
    print ("B")
else:
    print ("A")
    '''


# 18 take input of age of 3 people by user and determine oldest and youngest among them
'''a=int(input("input the first age "))
b=int(input("input the second age "))
c=int(input("enter the third age "))
if ((a<b) and (a<c)) :
    print (a, "a is youngets")
elif a==b and a<c:
    print (a,"a and b are youngest")
elif (b<a) and (b<c) :
    print (b ,"b is youngets")
elif b==c and b<a :
    print (b, " b and c are youngest")
elif c==a and c<b:
    print (c ,"c and are youngets")
else :
    print (c ,"c is youngest ")

if ((a>b) and (a>c)) :
    print (a, "a is oldest")
elif a==b and a>c:
    print (a,"a and b are oldest")
elif (b>a) and (b>c) :
    print (b ,"b is oldest")
elif b==c and b>a :
    print (b, " b and c are oldest")
elif c==a and c>b:
    print (c ,"c and are oldest")
else :
    print (c ,"c is oldest ")'''


# 19 Write a program to check whether a person is eligible for voting or not. (accept age from user)
'''age=int(input("enter the age  "))
if age >= 18 :
    print ("you are eligibel for voting")
else:
    print("you are not eligible for voting ")
'''


# 20 Write a program to check whether a number is divisible by 7 or not.
'''num=int(input("enter a number "))
if (num%7)==0 :
    print (num,"is divisible by 7")
else :
    print (num,"is not divisible by 7")'''

# 21 Accept any city from the user and display monument of that city.
#                  City                                 Monument
#                  Delhi                               Red Fort
#                  Agra                                Taj Mahal
#                  Jaipur                              Jal Mahal
'''city=input("enter a city  ")
cit=city.lower()
if cit=="jaipur":
    print ("Jal Mahal")
elif cit=="delhi":
    print ("Red Fort")
elif cit=="agra":
    print ("Taj Mahal")'''


# Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.
'''num=int(input("enter a number "))
if (num%2)==0 and (num%3)==0:
    print (num,"is divisible by both 2 and 3")
else:
    print (num,"is not divisible by both 2 and 3")'''


#Write a program to accept two numbers and mathematical operators and perform operation accordingly.
#Like:
#Enter First Number: 7
#Enter Second Number : 9
#Enter operator : +
#Your Answer is : 16
'''n=int(input("input the first number "))
m=int(input("input the second number "))
o=input("input a operator ")
if o=="+":
    print (n+m)
elif o=="-":
    print (n-m)
elif o==("*"):
    print (n*m)'''


# Write a program to display "Hello" if a number entered by user is a multiple of five, otherwise print "Bye".
"""n=int(input("enter a number "))
c= n%5
if c==0:
    print("hello")
else :
    print("bye")
"""


# Write a program to accept a number from 1 to 7 and display the name of the day like 1 for sunday, 
# 2 for monday and so on.



#Write the logical expression for the following:
#A is greater than B and C is greater than D
#    ANS= A>(B AND C) >D

#Write a program to check whether a number entered is three digit number or not.
'''n=int(input("enter a num  "))
if n<100:
    print (n," is not a three digit num")
elif n==100:
    print (n,"is a three digit num")
else :
    print (n," is a three digit num")'''



#Write a program to check whether a person is senior citizen or not.
'''age=int(input("enter the age  "))
if age>65:
    print ("the person is a senior citizen")
else :
    print ("the person is a not senior citizen")'''


#Write a program to find the lowest number out of two numbers expected from user.
'''a=int(input("input the first number  "))
b=int(input("input the second number  "))
if a<b or a==b:
    print (a,"is the lowest")
else:
    print (b,"is the lowest")

'''


#Accept the following from the user and calculate the percentage of class attended:
#a. Total number of working days
#b. Total number of days for absent
#After calculating percentage show that:
#if the percentage is less than 75, than student will not be able to sit in exam.

'''wd=int(input("enter the num of working days  "))
ab=int(input("enter the num of absent days  "))
p= wd-ab
percentage= (p/wd)*100
print ("present percentage is ", percentage,"%")
if percentage <75:
    print ("you are not able to sit in exam")
if percentage >=75:
    print ("you are able to sit in exam")
'''

#Write a program to accept percentage and display the category according to the following criteria:
#Percentage                Category
#<40		               Failed
#>=40 and <55              Fair
#>=55 and <65	           Good
#>=65		               Excellent

'''p=int(input("enter the percentage  "))
if p<100:
    if p<40 :
        print ("failed")
    elif p>=40 and p<55:
        print("fair")
    elif p>=55 and p<65	:
        print ("good")
    else :
        print ("excellent")
else:
    print("percentage should be 100 or below")
'''



# Accept the age, sex('M', 'F'), number of days and display the wages accordingly.
#Age		    Sex	 Wage/day
#>=18 and <30	M	 700
#		        F	 750
#>=30 and <=40	M	 800
#		        F	 850 
     
'''a=int(input("enter the age "))
g=(input("enter the gender "))
n=int(input("enter the num of days "))

if a>=18 and a<30 and g=="m":
    print ("total wage is",n*700)
elif a>=18 and a<30 and g=="f":
    print ("total wage is",n*750)
elif a>=30 and a<=40 and g=="m":
    print ("total wage is",n*800)
else:
    print ("total wage is",n*850)'''

#Accept three numbers from the user and display the second largest number.
'''num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
num3 = int(input("Enter third number :"))
 
if num1 > num2 and num1 > num3:
  if num2>num3:
    print("The second largest number is",num2)
  else:
    print("The second largest number is",num3)
elif num2 > num1 and num2 >num3:
  if num1 > num3:
    print("The second largest number is", num1)
  else:
    print("The second largest number is", num3)
else:
  if num1 > num2:
    print("The second largest number is",num1)
  else:
    print("The second largest number is", num2)'''



#Accept the number of days from the user and calculaye the charge for library according to following:
#Till five days: Rs 2/day
#Six to ten days: Rs 3/day
#11 to 15 days: Rs 4/day
#After 15 days: Rs 5/day

'''n=int(input("enter the num of days  "))
if n<=5:
    print ("the total charge is",n*2)
elif n>=6 and n<=10 :
    print ("the total charge is",n*3)
elif n>=11 and n<=15:
    print ("the total charge is",n*4)
else:
    print ("the total charge is",n*5)'''


#37. Evaluate the following statements:
'''a=True
b=True
c=True
d=True
1.print(c)
2.print(d)
3.print(not a)
4.print(not b)
5.print(not c)
6.print(not d)
7.print(a and b)
8.print(a or b)
9.print(a and b or c)
10.print(not a or b or c)
11. print(not a or not b or not c)
12.print(not(not a or not b or not c))'''

'''a=True
b=True
c=True
d=True

print(c)
print(d)
print(not a)
print(not b)
print(not c)
print(not d)
print(a and b)
print(a or b)
print(a and b or c)
print(not a or b or c)
print(not a or not b or not c)
print(not(not a or not b or not c))
print(not a or b or c)'''
'''
c1=int(input("enter the number of student in a "))
c2=int(input("enter the number of students in b "))
c3=int(input("enter the number of students in c "))
desk=((c1+c2+c3)/2 )
print (desk)
if desk%1==0:
    print (int(desk))
else:
    print (int(desk+1))


salary=int(input("enter the salay"))
if salary < 20000 :
    tax = (15/100) * salary
    print ("your tax amount is ",tax)
elif salary > 20000 and salary >=50000:
    tax = (25/100) * salary
    print ("your tax amount is ",tax)
elif salary > 50000 and salary >=10000:
    tax = (30/100) * salary
    print ("your tax amount is ",tax)
else:
    tax = (35/100) * salary
    print ("your tax amount is ",tax)'''


d=(input("enet the num")) 


days_list = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

for days in days_list:
    print(f"The day is {days}.")