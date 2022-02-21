# This code demonstrates some fancier forms of output

num1 = 3
num2 = 7
# Predict the output of this print (including proper spacing)
# Answer
print(num1,"+",num2,"=",num1 + num2)

# Predict the output of this print (including proper spacing)
# Answer
print(num1,"+",num2,"=",num1 + num2, sep='')


petName = "Misty"
petType = "Dog"
# Predict the output of this print (including proper spacing)
# Answer
print(petName,"is a",petType)

# Predict the output of this print (including proper spacing)
# Answer
print(petName,"is a",petType, sep='\n')

# Predict the output of this print (including proper spacing)
# Answer
print("Hello ", end='')
print("World!")

number = 3.2

# Predict the output of these 5 prints (including proper spacing)
# Answer
#
#
#
#
#
print("No numbers after the decimal point", format(number, ".0f"))
print("1 number after the decimal point", format(number, ".1f"))
print("2 numbers after the decimal point", format(number, ".2f"))
print("3 numbers after the decimal point", format(number, ".3f"))
print("4 numbers after the decimal point", format(number, ".4f"))

# Predict the output of this print (including proper spacing)
# Answer
print("This is a great way to print money $", format(number, ".2f"), sep='')
