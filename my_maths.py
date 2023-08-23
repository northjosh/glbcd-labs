
 
def calculate(num1, num2, request):
    
    def add():
        return num1 + num2

    def subtract():
        return num1 - num2

    def multiply():
        return num1 * num2

    def divide():
        return num1 / num2


    if request.lower() == "add":
        return add()
    elif request.lower() == "subtract":
        return subtract()
    elif request.lower() == "multiply":
        return multiply()
    elif request.lower() == "divide":
        return divide(num1, num2)
    else:
        return "Wrong entry!"
    

print(calculate(25,50, "add"))
        


