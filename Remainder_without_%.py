print("Program to write remainder without using modulus")
a , b =map(int,input("Write the numbers in one line with space in between them \n").split())
# split map is used to take and assign different variable in on line if the inputs have space in betweeen them
c = 0
while a>=b:
    a = a-b
    c = c+1
print(f"Remainder = {a},Quotient = {c}")
input()