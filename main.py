#add
def add(n1, n2):
    return n1 + n2

#subtract
def subtract(n1, n2):
    return n1 - n2
    
#multiply
def multiply(n1, n2):
    return n1 * n2

#divide
def divide(n1, n2):
    return n1 / n2

operations = {
"+": add,
"-": subtract,
"*": multiply,
"/": divide,
}


num1 = int(input("What's the first number? \n"))
num2 = int(input("What's the second number? \n"))


for symbols in operations:
    print(symbols)

operation_symbol = input("Pick an operator from the line above: ")

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)
    
print(f"{num1} {operation_symbol} {num2} = {answer}")

    