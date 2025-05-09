# Day 10 - continous calculator

def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

def get_calculation(operation_choice):
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    for operation_choice in operations:
        return operations[operation_choice]

def format_result(r, n1, n2):
    return f"{n1} {select_operation} {n2} = {r}"

number1 =  float(input("Provide first number: "))

while True:
    select_operation = input("Provide the operation to perform: [choice of '+', '-', '*' or '/'] ")
    number2 = float(input("Provide second number: "))
    result = get_calculation(select_operation)(number1, number2)
    print(format_result(result, number1, number2))
    choose_continue = input(f"Would you like to continue with {result} - type 'y', type 'n' for NEW calculation"
                            f" - any other letter to stop the program (y/n/other?) ")
    if choose_continue == "y":
        number1 = result
    elif choose_continue == 'n':
        print("\n" * 20) # clean screen
        number1 =  float(input("Provide first number: "))
    else:
        print("Exiting..")
        break
