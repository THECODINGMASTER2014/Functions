def add(P, Q):
    return P + Q

def sub(P, Q):
    return P - Q

def mul(P, Q):
    return P * Q

def div(P, Q):
    return P / Q

print("Select the Operation")
print("Add")
print("Substract")
print("Multiply")
print("Divide")

choice = int(input("Please Enter your choice (1/2/3/4) :"))

num_1 = int(input("Enter Number 1 :"))
num_2 = int(input("Enter Number 2 :"))

if choice == 1 :
    print(add(num_1, num_2))
elif choice == 2 :
    print(sub(num_1, num_2))
elif choice == 3 :
    print(mul(num_1, num_2))
elif choice == 4 :
    print(div(num_1, num_2))
else :
    print("Invalid")