# Quiz
#print(98.6)

#print(42 % 10)

#x = 1 + 2 * 3 - 8 / 4
#print(x)

x = int(98.6)
print(x)








# Assignment - Write a program that uses input to prompt a user for their name and then welcomes them. Note that input will pop up a dialog box. Enter Sarah in the pop-up box when you are prompted so your output will match the desired output.

name = input("Enter your name: ")
print('Hello',name)


# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking or bad user data.

hrs = input("Enter Hours: ")
rate = input("Enter rate: ")
Pay = float(hrs)*float(rate)
print('Pay:',Pay)