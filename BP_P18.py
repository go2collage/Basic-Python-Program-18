# Basic Python Program

# Calculate Factorial of a number

num = int(input("Enter a number: "))
fact = 1

if num <= 0:
    print("Number is not positive.")

else:
    for i in range(1, num + 1):
        fact = fact * i                 # 1 * 0 + 1 * 2 + .... + 1 * 5 = 120
    print("The Factorial of", num, "is: ",fact)


