print("Please enter amount in cents less than a dollar.")
num = int(input())
print("Your change will be:")
print("Q:", int(num/25))
num1 = num - (int(num/25)*25)
print("D:", int(num1 / 10))
num2 = num1 - (int(num1 / 10)*10)
print("N:", int(num2 / 5))
num3 = num2 - (int(num2 / 5)*5)
print("P:", int(num3 / 1))




