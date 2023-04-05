# Quiz
x=5;
if  x == 5 :
    print('Is 5')
    print('Is Still 5')
    print('Third 5')
    
    
x=5;
if  x == 5 :
     print('Is 5')
     print('Is Still 5')
     print('Third 5')
        

x=2.0;
if x < 2 :
    print('Below 2')
elif x >= 2 :
     print('Two or more')
else :
    print('Something else')


astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1
print(istr)









# Assignment - Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.

#hrs = input("Enter Hours: ");
#h = float(hrs);
#rate=input("Enter rate: ");
#r=float(rate);
#if h>40:
#    pay = 40*r + (h-40)*1.5*r;
#else:
#    pay = h*r;
#print(pay)





#Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

score = input("Enter Score: ");
score=float(score);
if score >= 0.9:
    print('A');
elif score >= 0.8:
    print('B');
elif score >= 0.7:
    print('C');
elif score >= 0.6:
    print('D');
else:
    print('F');
    
    